import random
temp=random.randint(25,100)
humid=random.randint(40, 60)
print("temperature ", temp)
print("Humidity: ",humid)
if(temp>100):
    print("High Temperature is detected")
else:
    print("Temperature is within the range")
if(humid<60):
    print("Normal humid")
else:
    print("Beyond the range")
    
