import os
print('Hi, How can i help you?')
s=input()
if s=='getcwd':
    print('This is present directory---->',os.getcwd())
else:
    print('Service Unavailable')
