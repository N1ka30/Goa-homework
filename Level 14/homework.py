#დავალება 2
number=19
if number>10:
    print("more than 10")
else:
    print("less than 10")

#დავალება 3
number=int(input("pick the number:"))
if number==15:
    print("equals to 15")
else:
    print("not equal to 15")

#დავალება 4
group=input("pick the group")
if group=="group 92":
    print("you are correct")
else:
    print("you are not correct")

#დავალება 5
for i in range(50,100,5):
    print(i)

#დავალება 6
for i in range(1,10):
    print('nikoloz zurabiani')


#დავალება 7
count=20
while count <50:
    print(count)
    count+=1

#დავალება 8
for i in range(0, 100):
    print(i)

i = 0
while i < 100:
    print(i)
    i += 1


#დავალება 9

for i in range(0, 101):
    print(i)

i = 0
while i <= 100:
    print(i)
    i += 1


#დავალება 10

for i in range(10, 21):
    print(i)

i = 10
while i <= 20:
    print(i)
    i += 1


#დავალება 11
for i in range(100, 201, 5):
    print(i)

i = 100
while i <= 200:
    print(i)
    i += 5


#დავალება 12
for i in range(10, -1, -1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i -= 1


#დავალება 13
num = float(input("შეიყვანე რიცხვი: "))
if num > 0:
    print("ეს რიცხვი დადებითი რიცხვია")
elif num < 0:
    print("ეს რიცხვი უარყოფითი რიცხვია")
else:
    print("ეს რიცხვი ნულია")


#დავალება 14
age = int(input("შეიყვანე ასაკი: "))
if age < 0:
    print("არასწორი ინფო")
elif age <= 12:
    print("ბავშვი ხარ")
elif age <= 19:
    print("მოზარდი/თინეიჯერი ხარ")
elif age <= 64:
    print("ზრდასრული ხართ")
elif age <= 120:
    print("ხანში შესული ხართ")
else:
    print("გურუ ან ჯადოქარი")


#დავალება 15
num1 = float(input("შეიყვანე პირველი რიცხვი:"))
num2 = float(input("შეიყვანე მეორე რიცხვი:"))
num3 = float(input("შეიყვანე მესამე რიცხვი"""))
if num1 >= num2 and num1 >= num3:
    print("უდიდესი რიცხვია:", num1)
elif num2 >= num1 and num2 >= num3:
    print("უდიდესი რიცხვია:", num2)
else:
    print("უდიდესი რიცხვია:", num3)



#დავალება 16

day = int(input("შეიყვანე რიცხვი 1-დან 7-მდე: "))

if day == 1:
    print("ორშაბათი")

elif day == 2:
    print("სამშაბათი")

elif day == 3:
    print("ოთხშაბათი")

elif day == 4:
    print("ხუთშაბათი")

elif day == 5:
    print("პარასკევი")

elif day == 6:
    print("შაბათი")

elif day == 7:
    print("კვირა")

else:
    print("არ ვიცი ეგ ")
#დავალება 17
num = float(input("შეიყვანე რიცხვი: "))

if num > 50:
    print(num * 5)

else:
    print(num ** 2)


#დავალება 18

password = input("შეიყვანე პაროლი: ")

if password == "goa123":
    print("password is correct")

else:
    print("incorrect password")


#დავალება 19

num = int(input("შეიყვანე რიცხვი: "))

sum = 0

for i in range(1, num + 1):
    sum += i

print("ჯამი არის:", sum)
