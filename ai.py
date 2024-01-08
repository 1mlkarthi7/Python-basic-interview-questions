#################finding sum of 100###
# n = 100
# a = range(1,n+1)
# sum = sum(a)
# print(sum)
# ###########Missing numbers########
# a ={1,4,9}
# min = min(a)
# max =max(a)
# b = range(min, max)
# sum = set(b)-set(a)
# print(sum)
########Arrow dict formate#####
# a = {1:"apple", 2:"cat", 3:"rat"}
# for k, v in a.items():
#     print(f"{k}-> {v}")
######swaping of 2 numbers#########
# a=2
# b=5
# temp = []
# temp = a#2
# a = b #5
# b = temp
# print(a,b)
#######################
# a=2
# b=7
# a = a+b#7+2=9
# b = a-b#9-7=2
# a = a-b#9-2=5
# print(a,b)
###########reverse of a string######
# a = "karthika"
# b = a[::-1]
# print(b)
########
# a = '1234'
# b = str(a[::-1])
# print(b)
#####palendrome###
# a = 'abba'
# if a == a[::-1]:
#     print("palendrome")
# else:
#     print("its not a palendrome")
##################Factorial
# a = 50
# temp = 1
# for i in range(1,a+1):
#     temp = temp*i
# print(temp)
#######Prime number#
# n=7
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#         break
# else:
#     print("prime")
##########Amstrong number########
a = 100
l = len(str(a))#3
temp = a
result = 0
while temp != 0:
    num = temp%10 #3(reminder)
    result = result+pow(num,l)#9
    temp = temp//10 #15(qoeffient)
if result == a:
    print("amstrong")
else:
    print("not amstrong")
    





