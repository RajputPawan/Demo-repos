import sys
import random
print(sys.version)
print("Testing first script")

if 5<6:
    print("True statement")
    print("False statement")
    # Varibles in python
x=5
y=10
z="He who remains"
print(x,y,z)

print("-----------------------------------------------------------")

#type of varible 
a=int(3)   # It will return the int value 3.
b=str("he who remains")   # It will return the string as he who remains 
c=float(9) #It will return the float value as 9.0
print(a,b,c)
print("-----------------------------------------------------------")
#Varible assignment
a,b,c="Ram","Govind","Bharat"
print(a) #It will print Ram
print(b) #It will print Govind 
print(c) #It will print Bharat

#Unpacking List
Lot=["App-Ops","UHD","UAM","Infra","RDS","Ubuntu"]
m,n,o,p,q,r = Lot 
print(m,n,o,p,q,r)




a=b=c="Orange"  # It will print Orange for all the a,b,c.
print(a)
print(b)
print(c)

#Type function in python
m=4
n="he who remains"
o=0.0
print(type(m))  #It will return the int class as it belongs to int class
print(type(n))  #It will return the string class
print(type(o))   #It will return the float class as its float value.
print("-----------------------------------------------------------")


#testing print() function
#adding two integers
a=4
b=4
print("The output of adding a and b:", a+b)
#adding integer and string  It will give error 
#a=4
#b="Radhey"
#print(a+b)
#adding two strings without spach
a=" Radhey "
b=" Shyam "
print(a+b) #expected output RadheyShyam

#data types
a=4
print(type(a))  #integer class
b=10.5
print(type(b)) #float data type
c="hello"
print(type(c)) #string class 
d=1j
print(type(d)) #complex class data type
e=(2,3,5,5,6,)
print(type(e)) #tuple class data type
f=[4,5,6,7,0]
print(type(f)) #list type of data type
g={45,"hello",67.0}
print(type(g)) #set class data type
h=True
print(type(h))#boolean class

#Random module(function)
#need to import the random module at the begging of the programe.
print(random.randrange(1,10))


