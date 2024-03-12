import math
import base64
with open("transmission1.txt","rb")  as file1,open("transmission2.txt","rb") as file2:
	f1 = file1.read()
	f2 = file2.read()
	val = ""
	for a,b in zip(f1,f2):
		if chr(a) == '\\' and chr(b) == 'x' or chr(a) == '|' and chr(b) == '+':
			val+='1'
		if chr(a) == '/' and chr(b) == 'x' or chr(a) == '-' and chr(b) == '+':
			val+='0'

integ = int(val,2) # decimal value from binary

print(base64.b64decode(bytes.fromhex(hex(integ)[2:]).decode()[4:]).decode()) #from decimal to hex string, then  hex to char string(which was base64 encoded)



