# ---------------------------A. gadamravlebit---------------------------------------------------------------------------

# import math
# x = input('Enter N & B : ')
# n_b = x.split()
#
# y = input('Enter numbers: ')
# lst = y.split()
#
# dict1 = {
#
# }
# for i in lst:
#     for a in lst:
#         B = int(i) * int(a)
#         if B == int(n_b[1]):
#             dict1.update({i:a})
#
# dict2 = {
#
# }
# if len(dict1) != 0:
#     a = 1
#     for key in dict1:
#         dict2.update({key:dict1[key]})
#         if a == math.ceil(len(dict1)/2):
#             break
#         a += 1
# elif len(dict1) == 0:
#     print('Impossible')
#
# index = len(lst)-1
# dict3 = {
#
# }
# for item in dict2:
#     i = lst.index(item) + 1
#     j = lst.index(dict2[item]) + 1
#     if j < index or j == index:
#         dict3.update({i:j})
#         index = j
#
# if len(dict3) == 1:
#     for a in dict3:
#         print(a, dict3[a])
# elif len(dict3) > 1:
#     key = sorted(dict3.items(), key= lambda item: item[1])
#     while True:
#         for tuple in key:
#             for num in tuple:
#                 print(num, end=' ')
#         break

# ---------------------------B. tanabari gamyofebi----------------------------------------------------------------------

# N = int(input('Enter Number : '))
# dividers = []
# if 1<=N<=10**12:
#     for i in range(1,N):
#         if N%i == N//i:
#             M.append(i)
#
# if len(dividers)!=0:
#     print(len(M))
# elif len(dividers) == 0:
#     print('None')
# else:
#     print('out of range')

# ---------------------------C. 0 tu 1----------------------------------------------------------------------------------

# T = int(input('Enter Number : '))
# str1 = input(f'Enter numbers 0 - {T} : ')
#
# Range = str1.split()
# lst=['1','0']
#
# if 1<=len(Range)<=10**18:
#     for i in range(1,len(Range)):
#         lst.append('1')
#         x = lst.count('1')
#         lst.append('0'*x)
# lst2 = ''.join(lst)
# lst3 = list(lst2)
#
# if len(lst3)==2 :
#     print('out of range')
# else:
#     for a in range(len(Range)):
#         print(lst3[a], end='')

# ---------------------------D. ganateba(daumtavrebeli)-----------------------------------------------------------------

# from math import factorial
#
# x = input('Enter : ')
# n_k = x.split()
#
# lst = []
# num = int(n_k[1])
#
# for a in range(1,int(n_k[1])+1):
#     fact1 = factorial(int(n_k[0]))
#     fact2 = factorial(int(n_k[0])-a)
#     var = factorial(int(n_k[0])-(int(n_k[0])-a))
#     print(fact1, fact2, var)
#     pos = fact1/(fact2*var)
#     lst.append(pos)
# print(lst)

# ---------------------------E. ertianebi ertad-------------------------------------------------------------------------

# num =  int(input("Enter Number : "))
# x = 0

# if 1<=num<=10**19:
#     newnum = str(bin(num))
#     newnum2 = newnum.split('0')
#     for i in newnum2:
#         if i.count('1')>x:
#             x = i.count('1')
#     print(x)
# else:
#     print('Out of range')

# ---------------------------F. sacnobaro sistema-----------------------------------------------------------------------


# --------------------------G. ricxvebi monakvetze----------------------------------------------------------------------


# --------------------------H. ogond martivebi ar iyos------------------------------------------------------------------


# --------------------------I. isev orobiti-----------------------------------------------------------------------------


# -------------------------------- MODA --------------------------------------------------------------------------------

# import math
# numbs = [30, 34, 43, 26, 109, 99, 26, 97, 26, 77, 69, 30, 30]
#
# x = sum(numbs)/len(numbs)
#
# print('sashvalo aritmetikuli -', x)
#
# if len(numbs)%2 == 0:
#     numbs.sort()
#     len_numbs = int(len(numbs)/2)
#     x = numbs[len_numbs+1]
#     y = numbs[len_numbs]
#     mediana = (y+x)/2
# else:
#     numbs.sort()
#     len_numbs = len(numbs)/2
#     x = math.ceil(len_numbs)
#     mediana = numbs[x]
#
# print('mediana -', mediana)
#
# x = 0
# moda = []
# moda1 = []
#
# for i in numbs:
#     count_i = numbs.count(i)
#     if count_i>x:
#         x = count_i
#         num = i
#     moda1.append(i)
#     if moda1.count(i)>1:
#         moda1.remove(i)
#     if len(moda1)==len(numbs):
#         num = 'ar aqvs'
#
# k = False
#
# for i in numbs:
#     count_i = numbs.count(i)
#     if count_i == x and count_i>1:
#          moda.append(i)
#          if moda.count(i)>1:
#              moda.remove(i)
#     if len(moda)>1:
#         k = True
#
# if k == False:
#     print('moda -', num)
# else:
#     print('{} moda - {}'.format(len(moda), moda))
