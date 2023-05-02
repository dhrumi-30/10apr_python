string1="hello"
string2="world"

string1 = string1[1] + string2[1:] + " " + string2[1] + string1[1:]

print(string1)