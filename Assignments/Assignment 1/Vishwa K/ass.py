import random
temp=random.randint(31, 100) 
humid=random.randint(48, 60) 
print("Temperature is: ", temp) 
print(" Humidity is: ", humid) 
if(temp>100) :
    print(" temperature is detected ")
else:
    print(" Temperature is within the range") 
if(humid<60) :
    print("Normal humid") 
else:
    print("beyond the range")
