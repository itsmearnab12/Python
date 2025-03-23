import time
Name = input("Enter Your Name: ")
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime("%H"))
if(hour>=0 and hour<12):
    print("Good morning", Name)
elif(hour>=12 and hour<17):
    print("Good After", Name)
elif(hour>=17 and hour<0):
    print("Good Night", Name)