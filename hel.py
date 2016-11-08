import cgi
import cgitb

cgitb.enable();
formData=cgi.fieldStorage();
print("Content-type: text/html\n\n")
print(formData.getValue('searchbox'));
