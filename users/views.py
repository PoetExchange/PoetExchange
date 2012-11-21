from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from users.forms import *
from users.models import RegValidator, SiteUser

def initRegistration(request) :
	'''
	Checks if user is authenticated; redirects to home page if already authanticated. 
	If user is not authenticated, function checks if the request method is POST; if method is POST, assumes form data is being submitted and takes action to log and mail out activation link.
	If method is not POST, assumes form has not been completed and renders empty form for the user.
	'''
	if request.user.is_authenticated :  # User is already registered; redirect
		return HttpResponseRedirect('/admin/')
	elif request.method == 'POST' : # User is submitting form; send out activation link
		form = InitRegForm(request.POST) # Fill out new form object with data sent via POST method
		if form.is_valid(): # Use filled form to perform validity check
			regVal = RegValidator.objects.create(
								user=form.cleaned_data['uname'],
								valid_code=valCodeGenerator(), # TODO: write function
							)
			regVal.save()
			email = form.cleaned_data['uname'] + '@poets.whittier.edu'
			# TODO: Insert function which sends out email, including validation code as GET variable
			return render_to_response( # R2R page showing email which val code has been sent to
								'placeholder.html', 
								{'email':email}, 
								context_instance=RequestContext(request),
							)
		else :  # Return user to form with errors if not valid
			return render_to_response(
								'placeholder.html', 
								{ 'form':form}, 
								context_instance = RequestContext(request),
							)
	else :  # User is not registered and not submitting; render blank form
		form=InitRegForm()
		return render_to_response(
								'placeholder.html', 
								{'form':form}, 
								context_instance=RequestContext(request),
							)

# TODO: Move this function into a functions.py file, import into this file
def mainRegValidator(reqmethod, usr):
		'''
		This function is used inside of the mainRegistration function to check that the username/validation code pair checks out
		The first check is to ensure that a validation code was in fact submitted via the GET method
		The second check gets the RegValidator object associated with the registration code
		The third check,, contained in the if block, ensures that the username attempting to register is in fact the username associated with the registration code
		'''
		try :
			val_code = reqmethod['valid']
		except KeyError :
			return False
		try:
			valid = RegValidator.objects.get(valid_code=vcode)
		except RegValidator.DoesNotExist :
			return False
		if valid.user != uname :
			return False
		return True
	

def mainRegistration(request, user_slug) :
	'''
	Runs all the same checks as initRegistration function;
	Creates new user if form is submitted and valid
	'''
	# TODO: Find way for form to resubmit to itself while sending validation code -- UPDATE: Best potential solution would seem to be to send  as POST data passed in  hidden, prepopulated fields on form
	uname = user_slug
	if request.method != 'POST' :
		if not mainRegValidator(request.GET, uname) :
			return render_to_response( # Error page stating registration request does not exist
							'ERROR.html',
							context_instance=RequestContext(request),
						)
	else : # If request method is POST
		if not mainRegValidator(request.POST, uname) :
			return render_to_response(
							'ERROR.html',
							context_instance=RequestContext(request),
						)

	if request.user.is_authenticated :  # User is already registered; redirect
		return HttpResponseRedirect('/admin/')
	elif request.method == 'POST' : # User is submitting form; send out activation link
		if form.is_valid(): # Use filled form to perform validity check
			'''
			After user creation, Function should perform a redirect to part 3 of registration(or rather profile info page)
			Include success message somewhere in 3rd registration page
			'''
			user = User.objects.create_user(
								username=uname, # CRITICAL: uname input not sanitized if not coming from form; this is a potential security risk. Resolve ASAP.
								password=form.cleaned_data['passwd'],
								email=uname + '@poets.whittier.edu',
							)
			user.save()
			siteUser = SiteUser.objects.create(
								user = user,
									# NOTE: use JS validation to ensure all 3 phone fields are filled if any of them are filled
								area_code = form.cleaned_data['area_code'],
								phone_prefix = form.cleaned_data['phone_prefix'],
								phone_suffix = form.cleaned_data['phone_suffix'],
								residence = form.cleaned_data['residence'],
								major = form.cleaned_data['major'],
								user_photo = form.cleaned_data['user_photo'],
							)
			siteUser.save()
			valid = RegValidator.objects.get(valid_code = request.POST['valid']
			valid.delete() # Delete validation code when registration complete
			return HttpResponseRedirect('/admin/') # redirect to a profile page after successful user creation
		else : # If form is not valid
			return render_to_response(
								'mainReg.html',
								{ 'form':form},
								context_instance = RequestContext(request),
							)
	else :  # User is not authenticated or submitting form
			form=MainRegForm()
			return render_to_response(
								'mainReg.html',
								{'form':form}, 
								context_instance=RequestContext(request),
							)	
