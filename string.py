from posixpath import join


a="python "
print(a[2]) #access the index value
print(a[1:4]) # start and end index(upto n-1)
print(a[::2]) # step size
print(a[::-1]) # reverse the string
b=a+" programming"
print(b) #concatenation of string
name="sathya"
print(len(name)) #length of string
print(name.upper()) #convert to uppercase
print(name.lower()) #convert to lowercase
print(name.capitalize()) #convert first character to uppercase
print(b.title()) #convert first character of each word to uppercase
print(name.count("a")) #count the number of occurrences of a character
print(name.swapcase()) #swap the case of each character
print(b.strip()) #remove leading and trailing whitespaces
print(name.lstrip()) #remove leading whitespaces
print(name.rstrip()) #remove trailing whitespaces
print(name.replace("s","S")) #replace a character with another character
print(name.startswith("s")) #check if the string starts with a specific character
print(name.endswith("a")) #check if the string ends with a specific character  
print(b.split()) #split the string into a list of words
print(name.split("a")) #split the string at a specific character
print(name.find("t")) #find the index of a specific character
print(name.find("U")) #find the index of a specific character that does not exist returns -1    
print(name.index("t")) #find the index of a specific character
#print(name.index("U")) #find the index of a specific character that does not exist returns error
list=["python","programming","language"]
print(join(*list)) #join the list of strings into a single string
print("".join(list)) #join the list of strings into a single string with a specific separator
print(name.isalpha()) #check if the string contains only alphabetic characters
print(name.isdigit()) #check if the string contains only digits
print(name.isalnum()) #check if the string contains only alphanumeric characters
print(name.islower()) #check if the string contains only lowercase characters
print(name.isupper()) #check if the string contains only uppercase characters   
print(name.count("a")) #count the number of occurrences of a specific character
print(" ".join(filter(str.isalnum, name))) #filter the string to contain only alphanumeric characters

s1="Tamilnadu"

s2=s1.replace("Tamilnadu","India") #replace a substring with another substring
print(s2)
s3=s1[::-1] #reverse the string
print(s3)   
print(sum(1 for c in s1 if c in "aeiou")) #count the number of vowelsin the string 
print(sorted(s1)) #sort the string in ascending order    