import urllib.request as req
#import os

true= b'true'

def checkText(t):
    t=t.strip("\n")
    print("http://www.purgomalum.com/service/containsprofanity?text="+t)    
    return( req.urlopen("http://www.purgomalum.com/service/containsprofanity?text="+t).read())

def readText():
    textFile=input("Input text path: ")
    try:
         content=open(textFile).read()
         
    except FileNotFoundError:
           print("File "+textFile+" not found!")
           return ""
        
    return content

if __name__== '__main__':
    analyzedText=readText()
    if analyzedText=="":
        print("No text to check")
    else:
        if checkText(analyzedText)==true:
            print("Curse words found")
        else:
             print("Text is clean!")
    
     
