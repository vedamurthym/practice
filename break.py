l=input("Enter a list of items separated by commas: ").split(",")
def list(l):
    for i in l:
      print(i)

list(l)

n=input("enter the numbers separated by comma:").split(",")
s=0
def addnum(n):
    for i in n:
        s=s+i
    print(s)
addnum(n)
        
s=list(input("enter a string:"))

def numberofcharecters(s):
    c=0
    for i in s:
        c=c+1
    print("number of characters in the string:",c)
    
