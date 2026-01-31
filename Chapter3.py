###### Thuật toán trong slide

#========== Binary Search
def binarySearch(arr, k):
    left = 0 # dau mang
    right = len(arr) -1 # cuoi mang
    while left<=right:
        mid = (right+left)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]>k:
           right = mid-1
        else:
            left = mid +1
    return -1

array = [0,1,4,5,23,32,80]
# print(binarySearch(array,80))

def mergeSort(arr,p,r):
    # print(arr)
    if p < r:
        q = (p+r)//2
        mergeSort(arr,p,q)
        mergeSort(arr,q+1,r)
        merge(arr,p,q,r)

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    # Tạo mảng L và R (+1 để chứa sentinel)
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    # Copy dữ liệu
    for i in range(n1):
        L[i] = A[p + i]

    for j in range(n2):
        R[j] = A[q + 1 + j]

    # Sentinel (∞)
    L[n1] = float('inf')
    R[n2] = float('inf')

    i = j = 0

    # Trộn lại vào A[p..r]
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

A = [2, 4, 5, 7, 1, 2, 3, 6,9,33]
# mergeSort(A, 0, len(A) - 1)
# print(A)


#### Thuat toan trong exercise
#Cau 1
def findMax(arr,l, r):
    if l == r:
            return r
    m = (r+l)//2
    i = findMax(arr,m+1,r)
    j = findMax(arr,l,m)
    if arr[i]>arr[j]:
        return i
    else:
        return j
rs =findMax(A, 0, len(A)-1)
# print(rs)

##Brute-Force 
def findMax(arr):
    max = -float('inf')
    for i in range(len(arr)):
        if (arr[i]>max):
            max = arr[i]
    return max
# print(findMax(A))


#Cau 2
def pown(a,n):
    if n == 0:
        return 1
    half = pown(a, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return a * half * half

# print(pown(6,100))

def brute_force_pown(a,n):
    rs = 1
    for i in range(n):
        rs = rs*a
    return rs

# print(brute_force_pown(6,100))

#==================Cau 3
def rearrange_dc(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = rearrange_dc(a[:mid])
    right = rearrange_dc(a[mid:])

    neg = takePosOrNeg(left, True) + takePosOrNeg(right, True)
    pos = takePosOrNeg(right, False) + takePosOrNeg(left, False)
    return neg + pos


def takePosOrNeg(arr,isNeg=False):
    pos = []
    for i in range(len(arr)):
        if isNeg == False:
            if arr[i] >= 0:
                pos.append(arr[i])
        else:
            if arr[i] <0:
                pos.append(arr[i])
    return pos

def rearrange(a):
    i, j = 0, len(a) - 1

    while i < j:
        if a[i] < 0:
            i += 1
        elif a[j] >= 0:
            j -= 1
        else:
            a[i], a[j] = a[j], a[i]


a = [3, -1, 4, -5, 2, -6]
# print(rearrange_dc(a))

##==============Cau 4
def closest_pair(A, l, r):
    if r - l < 2:
        return float('inf'), None
    if r - l == 2:
        return A[l+1] - A[l], (l, l+1)

    mid = (l + r) // 2

    dL, pL = closest_pair(A, l, mid)
    dR, pR = closest_pair(A, mid, r)

    dBest, pBest = (dL, pL) if dL <= dR else (dR, pR)

    dCross = A[mid] - A[mid-1]
    if dCross < dBest:
        return dCross, (mid-1, mid)

    return dBest, pBest

a=  sorted(a)
print(a)
print(closest_pair(a,0,len(a)))

        