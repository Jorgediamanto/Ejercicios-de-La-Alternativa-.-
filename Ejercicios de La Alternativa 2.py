from telnetlib import X3PAD


a = float(input("Introduzca el valor de a: "))
b = float(input("Introduzca el valor de b: "))

array_random = [a*b,a,b,a+b]
array_final=[]





for y in range(len(array_random)):
  minimo=array_random[0]
  for x in range(len(array_random)):
    if(array_random[x]<minimo):
      minimo=array_random[x]
      
  array_final.append(minimo)

  array_random.remove(minimo)

x1=1
x2=1
x3=1
x4=1

for x in range(4):
    if(array_final[x]==a*b and x1==1):
        print("a * b <")
        x1 = 0
        continue

    if(array_final[x]==a+b and x2 == 1):
        print("a + b <")
        x2 = 0
        continue

    if(array_final[x]==a and x3 == 1):
        print("a <")
        x3 = 0
        continue

    if(array_final[x]==b and x4 == 1):
        print("b <")
        x4 = 0
        continue

#print(array_final)

