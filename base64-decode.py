import base64
pwd = open('./pwd', 'r').read().strip()
for i in range (13):
	pwd=base64.b64decode(pwd)
print(pwd)