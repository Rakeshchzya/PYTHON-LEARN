colors=['red','green','blue','yellow','orange','purple']
print(f"length of colors : {len(colors)}")
print(f"First color : {colors[0]}")
print(f"last color : {colors[-1]}")
print(f"Colrs from index 1 to 3 : {colors[1:4]}")
print(f"reverse colors : {colors[::-1]}")



number = 1
while number<=10:
    print(number)
    number+=1

number=[20,30,50,60,70,90,100]
target = 121
for number in number:
 if number == target:
  print("Number is found")
  break
else:
  print("Number is not found")