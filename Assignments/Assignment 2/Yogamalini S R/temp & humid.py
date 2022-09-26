import random
temp=random.randint(35,60)
humid=random.randint(20,40)
print("temperature",temp)
print("humidity",humid)
if(temp>60):
    print("Temperature is detected")
else:
    print("Temperatue is within the range")
if(humid<40):
    print("normal humidity range")
else:
    print("humidity range exceed")
