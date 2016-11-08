#! /usr/bin/python3

def htmltop():
	print """Content-type: text/html\n\n
		<!DOCTYPE html>
		<html>
		<head>
  		<title>Hellooo</title>
		</head>
		<body>""";
	
def htmlend():
	print """</body></html>""";

htmltop();
print ("hello world");
htmlend();