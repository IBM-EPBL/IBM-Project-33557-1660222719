import random
temp=random.randint(30,100)
humid=random.randint(50,80)
print("temperature ", temp)
print("humidity: ",humid)
if(temp>100):
  print("Temperature is detected")
else:
  print("Temperature is within the range")
if(humid<60):
  print("Normal humid")
else:
  print("Beyond the range")
