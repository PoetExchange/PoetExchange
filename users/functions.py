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

def valCodeGenerator() :
	'''
	This function is used to generate a random validation code for new user registration. It takes no arguments and checks against the database to ensure the generated code is unique
	'''
	# NOTE: '123' Is serving as a placeholder code until the function is written
	return '123'