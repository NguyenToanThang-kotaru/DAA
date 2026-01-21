# import math
# ===================== Cau 3================
# s = "CABAAXBYAB"
# def CountSubString(s) -> int:
#     total = 0 
#     for i in range(len(s)): 
#         if s[i]=="A": 
#             for j in range(i,len(s),1): 
#                 if s[j]=="B": 
#                     total +=1 
#     return total 

# # print(CountSubString(s)) 
# #Improve the CountSubString(s) 
# def CountSubStringImproved(s) -> int: 
#     A = 0
#     total = 0
#     for i in range(len(s)):
#         if s[i] == "A":
#             A +=1
#         if s[i] == "B":
#             total += A
#     return total

# print(CountSubStringImproved(s))

# ===================== Cau 4 ===================
# arr = [3, 9, 12, 18, 25, 31, 46, 58, 72, 90]

# def closet_pair(arr):
#     a,b = arr[1],arr[0]
#     best_d = arr[1]-arr[0]
#     for i in range(0,len(arr),1):
#         if (i == len(arr)-1):
#             break
#         else:
#             if(arr[i+1]-arr[i]<best_d):
#                 best_d = arr[i+1]-arr[i]
#                 a,b = arr[i],arr[i+1]
#     return best_d,a,b

# print(closet_pair(arr))

# ===================== Cau 5 ===================

# p = [
#     [2, 5, 23, 10, 29],
#     [8, 9, 10, 12, 100],
#     [23, 23, 120, 112, 1100]
# ]

# def closest_pair_k(P):
#     best_d = float("inf")
#     n = len(P)

#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             sum_sq = 0
#             for d in range(len(P[i])):
#                 sum_sq += (P[i][d] - P[j][d]) ** 2
#             dist = math.sqrt(sum_sq)

#             if dist < best_d:
#                 best_d = dist
#                 best_pair = (P[i], P[j])

#     return best_d, best_pair


# print(closest_pair_k(p))