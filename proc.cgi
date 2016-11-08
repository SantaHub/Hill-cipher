import random,string
import cgi

formData = cgi.FieldStorage()

# text=raw_input('Enter the text to encoded :').upper();
text = formData.getvalue('msg').upper();


# text="PIKACHU"
length=len(text);
key=''.join(random.choice(string.ascii_uppercase) for _ in range(length*length));
print 'auto Generated key : '+key;

km=[[0]*length for i in range(length)]
for a in range(length):
	for b in range(length):
		km[a][b]=int(ord(key[(a*length)+b]))-65;

tm=[[0] for i in range(length)]
for a in range(length):
	tm[a][0]=int(ord(text[a]))-65;

result=[[0] for i in range(length)]
for a in range(length):
	for b in range(length):
		# print str(tm[b][0])+" "+str(km[a][b])+" "+str(tm[b][0]*km[a][b])+"\n"	
		result[a][0]+=(tm[b][0]*km[a][b]);
	result[a][0]%=26;

print 'Encrypted text is  : '
enc="";
for i in result:
	enc+=chr(i[0]+65);
print enc;