import re

passwordElements = ('[A-Z]', '[a-z]', '[0-9]', '[-,!,#,$,%,^,&,@]')
print('Type a password to check:')
password = input()
if len(password) >= 8 and all(re.search(r, password) for r in passwordElements):
    print('Strong password, but \"correct horse battery staple\" would be better.')
elif password == 'correct horse battery staple':
    print('Very strong password')
else:
    print('Weak Password')