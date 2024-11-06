import sys
print(sys.version)
#functions 
"""
upper()
lower()
strip()
replace()
split()
slice()
"""
#upper()
a="hello world"
print(a.upper())

#lower
a="Shri ram chandra kripal BHaj MaN"
print(a.lower())
#strip
a="                    Reunion , Reside, Recycle, Reduce , Reuse, Secret, Demo, Rachner"  
print(a.strip())       #It will remove the extra space at the beginning of the line
#replace
a="He Who Remains"
print(a.replace("H","W")) #It will replace H with W and the output will be We Who Remains.
#split
a="Sabrimala , GauriShankar, Rameshwaram ,Tirthankar"
print(a.split("$"))



#String concatenation
a="Hello"
b="World"
print(a+b)  #It will print HelloWorld without any spaces
print(a +" " +b) #It will print Hello World 


#Combining two things together int and string
a=24
print(f"Hello there I'm {a} years old") # It will return Hello there I'm 24 years old f---> means format function




