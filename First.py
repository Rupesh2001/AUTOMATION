<<<<<<< HEAD
# print("hello")

# a= int(65)
# print("the number is a ",a)
# b = int(input("Enter number b: "))
# if a==b:
#     print("equal")
# else:
#     print("not equal")

# print("--------------------------")
# x=34
# y=45

# def addition(number):
#     sum= x+y
#     print("the sum is",sum)
#     print("number",number)

# def subtraction():
#     sub = x-y
#     return sub

# for i in range (5):
    
#     print("the sub is ", subtraction())
#     addition(78)
#     print("---------------------------")
    


# swap
'''for i in range(3):
    ab= int(input("Enter first number"))
    bc= int(input("Enter second number"))

    if ab != bc:
        print("the number before swap", ab , bc)

        temp = ab
        ab=bc
        bc =temp

        print("The number after swap", ab , bc)
    else:
        print("You enter same number")'''

# def Starprint():
#     rows = int(input("Enter rows \n"))

#     for i in range(1, rows+1):
#         print("*" * i)

# Starprint()

# import string
# import random
# namelen = int(input("Enter name length \t"))
# def generate_random_name():
   
#    return "MR"+" "+''.join(random.choices(string.ascii_letters,k=namelen))

# for i in range(4):
#     name = generate_random_name()
#     if name:
#         print("Hello name",name)
#     else:
#         print("NAME IS DISPLAYED")
# print("----------------------------------------")
# #phnlen= int(input("Enter phone length \t"))
# def generate_random_number():
#     return "+977-"+''.join(random.choices(string.digits, k=10))

# for i in range(4):
#     phone = generate_random_number()
#   #  if len(phone)==10:
#     print("number is ", phone)
#  #   else:
#    #     print("phone havnot length 10 digits")

# a= int(input("Enter first number \t"))
# b= int(input("Enter second number \t"))
# def calculator():
#     def add():
#         sum = a+b
#         print("the addition is ", a+b)
#         return sum
#     def sub():
#         sub=a-b
#         return sub
#     def mul():
#         mul = a*b
#         return mul
#     def div():
#         div= a/b
#         return div
#     print("addition",add())
#     print("subtraction",sub())
#     print("multiply",mul())
#     print("division",int(div()))

# print("The calculator is")
# calculator()

'''
Secret_nnumber = 78

guess = int(input("Enter a number between 0 to 100"))
while True:
    if guess > Secret_nnumber:
            print("Your guess number is  high")
            print("Please! Try again!!!")
    elif guess < Secret_nnumber:
            print("your guess number  is low")
            print("Please! Try again!!!")
    else:
            print("Congratulation! your guess is correct")
            print("you want to continue!!!")
    break
    '''
'''
user_input = input("Enter a palindrome word")

if isinstance(user_input, str):
    print("you enter string")
    if user_input == user_input[::-1]:
        print(f"'{user_input}' is palindrome")
    else:
        print(f"'{user_input}' is not palindrome")
else:
    print("Ohh!!")

'''
"""
text = input("Enter a text")
vowels = "aeiouAEIOU"
count =0
for char in text:
    if char in vowels:
        count = count+1
print(f"Number of vowels are '{count}'")
"""
"""
class dog:
    def dog_attribute():
        print("Dog bark")
        print("Dog eat")
    
    dog_attribute()

print("Outside function")
"""

=======
# print("hello")

# a= int(65)
# print("the number is a ",a)
# b = int(input("Enter number b: "))
# if a==b:
#     print("equal")
# else:
#     print("not equal")

# print("--------------------------")
# x=34
# y=45

# def addition(number):
#     sum= x+y
#     print("the sum is",sum)
#     print("number",number)

# def subtraction():
#     sub = x-y
#     return sub

# for i in range (5):
    
#     print("the sub is ", subtraction())
#     addition(78)
#     print("---------------------------")
    


# swap
'''for i in range(3):
    ab= int(input("Enter first number"))
    bc= int(input("Enter second number"))

    if ab != bc:
        print("the number before swap", ab , bc)

        temp = ab
        ab=bc
        bc =temp

        print("The number after swap", ab , bc)
    else:
        print("You enter same number")'''

# def Starprint():
#     rows = int(input("Enter rows \n"))

#     for i in range(1, rows+1):
#         print("*" * i)

# Starprint()

# import string
# import random
# namelen = int(input("Enter name length \t"))
# def generate_random_name():
   
#    return "MR"+" "+''.join(random.choices(string.ascii_letters,k=namelen))

# for i in range(4):
#     name = generate_random_name()
#     if name:
#         print("Hello name",name)
#     else:
#         print("NAME IS DISPLAYED")
# print("----------------------------------------")
# #phnlen= int(input("Enter phone length \t"))
# def generate_random_number():
#     return "+977-"+''.join(random.choices(string.digits, k=10))

# for i in range(4):
#     phone = generate_random_number()
#   #  if len(phone)==10:
#     print("number is ", phone)
#  #   else:
#    #     print("phone havnot length 10 digits")

# a= int(input("Enter first number \t"))
# b= int(input("Enter second number \t"))
# def calculator():
#     def add():
#         sum = a+b
#         print("the addition is ", a+b)
#         return sum
#     def sub():
#         sub=a-b
#         return sub
#     def mul():
#         mul = a*b
#         return mul
#     def div():
#         div= a/b
#         return div
#     print("addition",add())
#     print("subtraction",sub())
#     print("multiply",mul())
#     print("division",int(div()))

# print("The calculator is")
# calculator()

'''
Secret_nnumber = 78

guess = int(input("Enter a number between 0 to 100"))
while True:
    if guess > Secret_nnumber:
            print("Your guess number is  high")
            print("Please! Try again!!!")
    elif guess < Secret_nnumber:
            print("your guess number  is low")
            print("Please! Try again!!!")
    else:
            print("Congratulation! your guess is correct")
            print("you want to continue!!!")
    break
    '''
'''
user_input = input("Enter a palindrome word")

if isinstance(user_input, str):
    print("you enter string")
    if user_input == user_input[::-1]:
        print(f"'{user_input}' is palindrome")
    else:
        print(f"'{user_input}' is not palindrome")
else:
    print("Ohh!!")

'''
"""
text = input("Enter a text")
vowels = "aeiouAEIOU"
count =0
for char in text:
    if char in vowels:
        count = count+1
print(f"Number of vowels are '{count}'")
"""
"""
class dog:
    def dog_attribute():
        print("Dog bark")
        print("Dog eat")
    
    dog_attribute()

print("Outside function")
"""

>>>>>>> 8218050 (Selenium Automation)
