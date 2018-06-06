a = int(input("a=?"))
b = int(input("b=?"))
c = int(input("c=?"))
delta = b**2-4*a*c
candelta=delta**1/2
if delta<0:
     print("Vo Nghiem")
elif delta==0:
     print("x=",-b/(2*a))

else:
     print("x1=",(-b+candelta)/(2*a),",x2=",(-b-candelta)/(2*a))