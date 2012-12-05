# Custom functions which are general to entire site

def whoAmI(userAgent, browserDic=None) :
	'''
	This function takes two arguments, the second being optional
	userAgent - http user agent
	regexDic - An optional dictionary to specify additional browsers to check. Defaults are IE, Opera, Firefox, and any webkit.
	This function tests each browser ID pattern against the user agent string to determine what browser the request is made from.
	It returns a dictionary where keys are all the browsers tested and the values are a boolean indicating whether the specified pattern for the browser was found in the user agant string.
	'''
	browserCheck = {'ie':r'Trident', 'opera':r'Opera', 'webkit':r'AppleWebKit', 'firefox':r'Firefox'}
	if browserDic :
		for browser in browserDic :
			browserChecks[browser] = browserDic[browser]
	for browser in browserCheck :
		if browserCheck[browser] in userAgent :
			browserCheck[browser] = True
		else :
			browserCheck[browser] = False
	return browserCheck
