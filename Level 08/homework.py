#დავალება 2
#1 მეტობა 
print(5>3) #true
print(8>10) #false
print(12>13) #true
print(15>16) #true
print(17>18) #false
#ნაკლებობა
print(13<10) #false
print(10<15) #true
print(17<23) #true
print(11<8) #false
print(23<24) #true

#მეტობა ან ტოლობა
print(10>=10) #true
print(15>=16) #false
print(18>=17) #true
print(23>=23) #true
print(25>=28) #false

#ნალკლებობა ან ტოლობა
print(23<=25) #false
print(28<=25) #false
print(100<=100) #true
print(155<=166) #true
print(167<=168) #true

#მკაცრი ტოლობა
print(10==10) #true
print(155==155) #true
print(16789==12322) #false
print(11111==1899) #false
print(188==188) #true

# უტოლობა
print(10!=10) #false
print(3!=7) #true
print(5!=10) #true
print(155!=155) # false
print(15!=17) #true


#დავალება 3
#logitical operators არის ისეთი ოპერატორები რომელშიც გამოიყენება true და false ანუ მცდარი და ჭეშმარიტი და-ს შემთვევაში 2-ვე პირობა უნდა აკმაყოფილებდეს რომ მართალი აღმოჩნდეს ხოლო ან-ის შემთვევაში 1-1 ი მაინც უნდა აკმაყოფილებდეს

print(True and True) #true
print(True and False) #false
print(False and True) #false
print(False and False) #false

print(True or True) #true
print(True or False) #true
print(False or True) #true
print(False or False) #false

#დავალება 4

5>2 and 3<4 #true
10==10 and 5!=5 #false
7<9 and 2>3 #false
5>10 or 3<4 #true
7==8 or 2!=2 #false
10>=10 or 5<1 #true

#დავალება 5
number1=int(input("enter the number:"))
number2=8
print(number1>number2)

#დავალება 6
name=input('enter your name:')
myname="nikoloz"
print(name==myname)

#დავალება 7
age=int(input("enter your age:"))
print(age>18)