# for x in range(1500,2701):
#     if(x%7==0 and x%5==0):
#         print (x)

# output:
# 1505
# 1540
# 1575
# 1610
# 1645
# 1680
# 1715
# 1750
# 1785
# 1820
# 1855
# 1890
# 1925
# 1960
# 1995
# 2030
# 2065
# 2100
# 2135
# 2170
# 2205
# 2240
# 2275
# 2310
# 2345
# 2380
# 2415
# 2450
# 2485
# 2520
# 2555
# 2590
# 2625
# 2660
# 2695
    
# ---------------------------------------------------------------------------
# print("Which temperature you want to calculate?")
# x=input("c for celcius and f for farenheit:")
# if(x=='c'):
#     f=input("Give the temp in farenheit")
#     x=(f-(32/9))*5
#     print(x,"degree celcius")
# if(x=='f'):
#     c=input("Give the temp in celcius")
#     x=((c/5)+(32/9))
#     print(x,"degree Farenheit")
# -----------------------------------------------------------------
# import random
# def guess_num():
#     num_to_guess=random.randint(1,9)
#     print("Welcome to the random guessing game!")
#     while True:
#      user_num=int(input("Enter a number to guess:"))
#      if(num_to_guess==user_num):
#         print("You have guessed correct!")
#         break
#      else:
#         print("try again!")
# guess_num()
# -------------------------------------------------------------------------------------
# rows = 5

# for i in range(1, rows + 1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# for i in range(rows - 1, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# ----------------------------------------------------------------------------------------
# word = input("Enter a word: ")
# reversed_word = word[::-1]
# print("Reversed word:", reversed_word)
# ----------------------------------------------------------------------------------------
# numbers=print("Enter a list of numbers")
# even_count=0
# odd_count=0
# num_list=list(map(int,(numbers.split())))
# for num in num_list:
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# -----------------------------------------------------------------------------------------
# num1=0
# num2=1
# print(num1," ",num2)
# while(num1+num2<=50):
#     temp=num2 
#     num2=num1+num2
#     num1=temp
#     print(num2," ")


# -----------------------------------------------------------------------------------------
# for x in range(0,6):
#     if x==3 or x==6:
#      continue
#     print(x)
# -----------------------------------------------------------------------------------------

# for i in range (51):
#     if(i==0):
#         continue
#     elif(i%3==0 and i%5!=0):
#         print("fizz")
#     elif (i%5==0 and i%3!=0):
#         print("Buzz") 
#     elif (i%3==0 and i%5==0):
#         print("FizzBuzz")
#     else:
#         print(i)

# -----------------------------------------------------------------------------------------

# m=int(input("number of rows:"))
# n=int(input("number of columns:"))

# nested_list = [[0] * n for _ in range(m)]  

# for i in range(m):
#     for j in range(n):
#         nested_list[i][j]=i*j

# print(nested_list)    

# -----------------------------------------------------------------------------------------
# str1=""
# str2=input("Enter a line:")
# while (str2!=""):
#     str1=str1+str2
#     str2=input("Enter a line:")

# print(str1.lower())    

# -----------------------------------------------------------------------------------------

# binary_numbers = input("Enter:").split(",")

# divisible_by_5=[]

# for binary in binary_numbers:
#     decimal=int(binary,2)
#     if (decimal % 5 == 0):
#         divisible_by_5.append(binary)
#     else:
#         pass

# print(",".join(divisible_by_5))        

# -----------------------------------------------------------------------------------------
# text = input("Enter a string: ")
# letters = 0
# digits = 0

# for char in text:
#     if char.isdigit():
#         digits += 1
#     elif char.isalpha():
#         letters += 1

# -----------------------------------------------------------------------------------------

# pswd=input("Enter your password:")
# if len(pswd) < 6 :
#     print("minimum length is 6")
# if(len(pswd) > 16) :
#    print("maximum length is 16")
# for char in pswd:
#     if char.isdigit()==True:
#         break
# else:
#     print("at least one digit is required")    
# for char in pswd:
#     if char.isalpha()==True:
#         if char.isupper()==True:
#             break
# else:
#     print("at least one uppercase letter is required")    
# for char in pswd:
#     if char.isalpha()==True:
#         if char.islower()==True:
#             break
# else:
#     print("at least one lowercase letter is required")    
# for char in pswd:
#     if char=='$' or char=='#' or char =='@':
#         break
# else:
#     print("at least one  special character (  $  or  #   or   @) is required")






   
    


