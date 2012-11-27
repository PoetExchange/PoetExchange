from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from users.forms import *
from users.models import RegValidator, SiteUser
from users.functions import mainRegValidator, valCodeGenerator
from django.contrib.auth import authenticate, login
# NOTE: All code snipets which have a comment readig **tmp** next to them are code which is present only for testing/debugging purposes, and will not remain in context during production

def initRegistration(request) :
	'''
	Checks if user is authenticated; redirects to home page if already authanticated. 
	If user is not authenticated, function checks if the request method is POST; if method is POST, assumes form data is being submitted and takes action to log and mail out activation link.
	If method is not POST, assumes form has not been completed and renders empty form for the user.
	'''
	if request.user.is_authenticated() :  # User is already registered; redirect
		return HttpResponseRedirect('/admin/')
	if request.method == 'POST' : # User is submitting form; send out activation link
		form = InitRegForm(request.POST) # Fill out new form object with data sent via POST method
		if form.is_valid(): # Use filled form to perform validity check
			regVal = RegValidator.objects.create(
								user=form.cleaned_data['uname'],
								valid_code=valCodeGenerator(), 
							)
			regVal.save()
			host = request.get_host()
			regUrl = request.get_host() + '/register/' + regVal.user + ('/?valid_code=%s' % regVal.valid_code)
			email = form.cleaned_data['uname'] + '@poets.whittier.edu'
			# TODO: Insert function which sends out email, including validation code as GET variable
			return render_to_response( # R2R page showing email which val code has been sent to
								'testing/testBase_initSubmit.html', 
								{
									'email':email,
								},
								context_instance=RequestContext(request),
							)
		else :  # Return user to form with errors if not valid
			return render_to_response(
								'testing/testBase_initReg.html', 
								{ 'form':form}, 
								context_instance = RequestContext(request),
							)
	else :  # User is not registered and not submitting; render blank form
		form=InitRegForm()
		return render_to_response(
								'testing/testBase_initReg.html',
								{
									'form':form,
									'hostname':request.get_host() + '/test/',
								},
								context_instance=RequestContext(request),
							)

def mainRegistration(request, user_slug) :
	'''
	Runs all the same checks as initRegistration function;
	Creates new user if form is submitted and valid
	'''
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

	if request.user.is_authenticated() :  # User is already registered; redirect
		return HttpResponseRedirect('/admin/')
	elif request.method == 'POST' : # User is submitting form; send out activation link
		form = MainRegForm(request.POST) 
		if form.is_valid(): # Use filled form to perform validity check
			'''
			After user creation, Function should perform a redirect to part 3 of registration(or rather profile info page)
			Include success message somewhere in 4rd registration page
			'''
			user = User.objects.create_user(
								password=form.cleaned_data['passwd'],
								email=uname + unicode('@poets.whittier.edu'),
							)
			user.save()
			siteUser = SiteUser.objects.create(
								user = user,
								area_code = form.cleaned_data['area_code'],
								phone_prefix = form.cleaned_data['phone_prefix'],
								phone_suffix = form.cleaned_data['phone_suffix'],
								residence = form.cleaned_data['residence'],
								major = form.cleaned_data['major'],
								user_photo = form.cleaned_data['user_photo'],
							)
			siteUser.save()
			valid = RegValidator.objects.get(valid_code = request.POST['valid'])
			valid.delete() # Delete validation code when registration complete
			return HttpResponseRedirect('/admin/') # redirect to a profile page after successful user creation
		else : # If form is not valid
			return render_to_response(
								'testing/testBase_mainReg.html',
								{ 
									'form':form,
									'vcode':request.POST['valid_code'],
									'uname':uname,
									},
								context_instance = RequestContext(request),
							)
	else :  # User is not authenticated or submitting form; render blank form
			form=MainRegForm()
			return render_to_response(
								'testing/testBase_mainReg.html',
								{
									'form':form,
								 	'vcode':request.GET['valid_code'],
									'uname':uname,
								}, 
								context_instance=RequestContext(request),
							)

def loginRequest(request) :
	if request.user.is_authenticated() : # User is already logged in, redirect
		return HttpResponseRedirect('/admin/')
	elif request.method == 'POST' : # User is requesting authentication
		form = LoginForm(request.POST)
		if form.is_valid :
			uname = form.cleaned_data['uname']
			passwd = form.cleaned_data['passwd']
			authUser = authenticate(username=uname, password=passwd)
			if authUser is not None :
				login(request, user)
				return HttpResponseRedirect('/admin/')
			else :
				return render_to_response(
									'login.html', 
									{ 'form':form, },
									context_instance=RequestContext(request)
	else : # User is not logged in or requesting authentication; render blank form
		form = LoginForm()
		return render_to_response(
								'login.html',
								{ 'form':form },
								context_instance=RequestContext(request),
							)

def logoutRequest(request) :
	logout(request)
	return HttpResponseRedirect('/')
