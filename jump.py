a =0
while a <=99:
    a = a + 1
    if a%7==0: #7的倍数
        continue
        print(a)
    elif (a%10)==7: #个位含7
        continue
        print(a)
    elif (a//10)==7: # 十位含7
        continue
        print(a)
    print(a)



# a =1
# while a <=100:
#     if a%7==0:
#         continue
#     elif (a%10)==7: #个位含7
#         continue
#     elif (a//10)==7: # 十位含7
#         continue
#     else:
#         print(a)
#     a = a+1