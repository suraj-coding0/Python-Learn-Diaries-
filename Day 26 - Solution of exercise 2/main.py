import time
Time_string = time.strftime("%H:%M:%S")
time = int(Time_string.split(":")[0])

if time == 0:
  print("mid night")
elif time < 12:
    print("good morning sir")
elif 12 <= time < 17:
    print("good afternoon")
elif 17 <= time < 23:
    print("good evening")
else:
    print("good night")
print("thie time is:", Time_string)