# def func(num):
    
#     bin_num = bin(num)[2:]
#     sum_bin_num = bin_num.count('1')
#     if sum_bin_num % 2 == 0:
#         bin_num = "1" + bin_num[2:] + "0"
#     else:
#         bin_num = "11" + bin_num[2:] + "1"
#     return int(bin_num, 2)


# minN, minR = 100000, 1000000
# for N in range(1, 1000):
#     if func(N) > 49:
#         if func(N) <= minR:
#             minR = func(N)
#             minN = min(minN, N)

# print(minN)


# ans = list()
# for d in range(60, -10, -1):
#     if (d * 5) % ((3 - 1)*(5 - 1)) == 1:
#         ans.append(d)

# print(max(ans))


# print(~((~26|(67>>3))&(55<< 2)))


# def FF(x, y):  # Trajectory: exclude 14, include 10
#     if x == y:
#         return 1
#     if x > y or x == 13:
#         return 0
#     if x < y:
#         return FF(x + 1, y) + FF(x + 2, y) + FF(x * 3, y)


# print(FF(3, 8) * FF(8, 18))


# for ss in range(1000000):
#     s = ss // 10
#     n = 1
#     while s < 51:
#         s = s + 5
#         n = n * 2
#     if n == 64:
#         print(ss)


# with open("Вар1_13.txt") as f:
#     nums = list(map(int, f.readlines()))
#     min19 = 10000000
#     q, maxs = 0, 0
#     for num in nums:
#         if num % 19 == 0:
#             min19 = min(min19, num)
#     print(min19)
#     for i in range(9999):
#         a, b = nums[i], nums[i + 1]
#         if a % min19 == 0 or b % min19 == 0:
#             q += 1
#             maxs = max(maxs, a + b)


# print(q, maxs)