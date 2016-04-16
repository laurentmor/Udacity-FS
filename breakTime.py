import time
import webbrowser
n=0
print ("Program started on: "+time.ctime)
while (n<3):
    time.sleep(10)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    n=n+1
