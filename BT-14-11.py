#Tong day
#n = 5
#k = 4
#data = '1 2 3 4 5'
#data = list(map(int, data.split()))
#print(sum(data)%k)

#Chia het
# n = 5
# data = '7 14 91 6 26'
# data = list(map(int, data.split()))
# for i in data:
#     if i % 7 == 0 and i % 13 == 0:
#         print('both')
#     elif i % 7 == 0:
#         print('mod 7')
#     elif i % 13 == 0:
#         print('mod 13')
#     else:
#         print('none')

#Bo ba
# count = 0
# n = 5
# data = '1 2 3 4 5'
# data = list(map(int, data.split()))
# for i in range(0, n-2):
#     for j in range(i+1, n-1):
#         for t in range(j+1,n):
#             if (data[i] + data[j] + data[t]) % 5 == 0:
#                 count += 1
# print(count)

# GCD & LCM
# def gcd(a : int, b : int):
#     if a < b:
#         a, b = b, a
#     if b == 0:
#         return a
#     return gcd(b, a % b)
# def lcm(a : int, b : int):
#     return (a * b) // gcd(a, b)
# q = 3
# n = [[120, 140],[10213, 312],[10, 30]]
# for i in range(0, q):
#     print(gcd(n[i][0], n[i][1]), end=' ')
#     print(lcm(n[i][0], n[i][1]))

# LT
# def test(n,a,b,k):
#     count = 0
#     for i in range(1, n+1):
#         if i % a and not(i % b):
#             count += 1
#         if i % b and not(i % a):
#             count += 1
#     if count >= k:
#         return 'Yes'
#     else:
#         return 'No'
# q = 1
# data = [[6,2,3,3]]
# for i in range(0, q):
#     print(test(data[i][0],data[i][1],data[i][2],data[i][3]))