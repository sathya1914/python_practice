#first unique character in a string question :387
'''s="leetcode"
class Solution:
    def unique(self,s):
        for i in range(len(s)):
            if s.count(s[i])==1:
                return s[i]
            return -1
        
s=input("Enter the string:")
obj=Solution()
print(obj.unique(s))    '''




#check if a string is a palindrome question :125
'''
class Solution:
    def isPa(self,s):
        s=s.lower()
        s=" ".join(filter(str.isalnum,s))
        return s==s[::-1]
s=input("Enter the string:")
obj=Solution()
print(obj.isPa(s))  '''


#lenth of the last word in a string question :58
'''class Solution:
    def lengthOfLastWord(self,s):
        s=s.strip()  #remove leading and trailing whitespaces
        print(s)
        s=s.split(" ")  #split the string into a list of words
        return len(s[-1])
s=input("enter the string:")
obj=Solution()
print("length of last word is: "+str(obj.lengthOfLastWord(s))) '''


#reverve a characters in a list question :344

class Solution:
    def reverseString(self,s):
        left=0
        right=len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        return s
s=input("Enter the list of characters: ").split()  #split the string into a list of characters
obj=Solution()
print("Reversed list of characters is: "+str(obj.reverseString(s)))