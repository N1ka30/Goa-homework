# დავალება 2
print(5>7 or 5>3) #true
print(5==5 or 10>3 ) #true
print(67>66 and 80>23) #true
print(1700>321 and 321<323) #true
print(756<777 or 777>888) #true

print(5!=7 and 10<3) #false
print(2>5 or 3>6) #false
print(373<366 )  #false
print(5>190) #false
print(100000000<1) #false

#დავალება 3

#იტეცია ნიშნავს კოდის გამეორებას
#სექუენცინგი ნიშნავს კოდის თანმიმდევრობას
#სელექშენი ნიშნავს კოდის არჩევას

#დავალება 4

x=1
y=2
x2=x+y
print(x2)

#დავალება 5

# loop  გამოიყენებ რაიმე კოდის რიცხვის ან წინადადების განმეორებაში მაგალითად
for i in range(1,100):
    print("hello world")


#დავალება 6

# range გადაეცემა  რაოდენობა თუ რამდენჯერ უნდა გაიმეოროს კოდი და ერთ ერთი მაგალითი მაღლა არის მოყვანილი


for i in range(1,100):
    print("hello world 2")

#დავალება 7

for i in range(1,101):
    print("porche 911 gt3 991")

#დავალება 8
for i in range(1,101):
    print("Zurabiani")


#დავალება 9

for i in range(1,47):
    print("red")

#დავალება 10

for i in range(1,33):
    print("N")


#დავალება 11


string1=input("გამარჯობა:")
string2=input("გაგიმარჯოს:")
string3=input("ისევ გამარჯობა:")
integer=int(input("ისევ გაგიმარჯოს:"))

all= string1+string2+string3+str(integer)
print(all)

#დავალება 12

a=12
b="gamarjoba"
c=True
d=3.2
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#დავალება 13

a=int(input("რიცხვი:"))
b=int(input("რიცხვი 2:"))
c=int(input("რიცხვი 3:"))
d=int(input("რიცხვი 4 :"))

all=a+b+c+d
print(all)



