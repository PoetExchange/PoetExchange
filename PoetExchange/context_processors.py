from objects.functions import whoAmI

def uagent(request) :
	return {
		'uagent':whoAmI(request.META['HTTP_USER_AGENT']),
	}
