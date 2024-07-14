import os
import re

enter="BPCC134 ENGLISH July 23- Jan 24.pdf"

flag=0

dir_name=[]

file_name=[]

for dirpath,dirname,filename in os.walk("C:/Users/Admin/Downloads"):
    dir_name.append(dirname)
    file_name.append(filename)

#print(file_name)



for i in file_name:
    if enter in i:
        flag=1
        
if flag==0:
    print("not working")


