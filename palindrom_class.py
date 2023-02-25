import sys

class Solution:
    # Write your code here
    def __init__(self) -> None:
        self.arr = []
        self.arr1= []

    def pushCharacter(self,i):
        self.i = i
        self.arr.append(self.i)
        
    def enqueueCharacter(self,i1):
        self.i1 = i1
        self.arr1.append(self.i1)
    
    def popCharacter(self):
        return self.arr.pop()
    
    def dequeueCharacter(self):
        return self.arr1.pop(0)
        

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    