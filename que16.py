str1=input("enter the first string:-")
str2=input("nter the second string:-")

x=str1[0:2]

str1=str1.replace(str1[0:2],str2[0:2])
str2=str2.replace(str2[0:2],str1[0:2])

print("enter string has become:",str1)
print("enter string has become",str2)