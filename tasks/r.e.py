import re
import os
file_re=open(r"C:\Users\Mohand\Desktop\re.txt"  )
file=file_re.read()
number_list=re.findall("\d{3}\s?-?\d{3}\s?-?\d{4}",file)
email_list=re.findall("[A-z0-9\.]+@[A-z0-9\.]+(net|com|org|eg)",file)
name_list=re.findall("[A-z0-9]+",file)
print(name_list)
print(number_list)
print(email_list)
