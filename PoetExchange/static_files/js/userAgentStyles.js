function appendAgentStyles(browserChecks) {
/* This function uses a user agent call to check the user agent and append custom stylesheets
 * for specific browsers depending on how the user agent identifies. It takes a single argument
 * which is an associative array in which the key is the pattern to search for in the user agent
 * line, and the value is the name of the stylesheet assumed to be under url '/static/'
 */
	for (browser in browserChecks) {
		var expr = new RegExp(browser, 'i'); // Browser is regex search pattern, i is modifier to run case insensitive search
		if (navigator.userAgent.match(expr)) {
			var style = document.createElement('link');
			style.setAttribute('rel', 'stylesheet');
			style.setAttribute('type', 'text/css');
			style.setAttribute('href', '/static/' + browserChecks[browser]);
			document.getElementsByTagName('head')[0].appendChild(style);
			break;
		};
	}
	return null;
}
