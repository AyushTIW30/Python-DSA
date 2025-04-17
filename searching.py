################    binary search   ####################

# def b_search(l,target):
#     low = 0
#     high = len(l)-1
#     while low<=high:
#         mid = (low+high)//2
#         if l[mid] == target:
#             return mid
#         elif l[mid]<target:
#             low = mid+1
#         else:
#             high = mid-1
#     return -1
# a = [1,2,3,4,5,6,7,8,9,10]
# print(b_search(a,target = 6))




#######################     lower bound     #######################
# by linear

# def low_bound(l,x):
#     for i in range(len(l)):
#         if l[i] >= x:
#             return l[:i]
#     return l[:i+1]
# a = [2,2,2,2,3,4,5,6]
# x = 4
# print(low_bound(a,x))

# by binary

# def low_bound(l,x):
#     low = 0
#     high = len(l)-1
#     while low<=high:
#         mid = (low+high)//2
#         if l[mid]==x:
#             return l[:mid]
#         elif l[mid]<x:
#             low = mid+1
#         else:
#             high = mid-1
#     return l

# a = [2,2,2,2,3,4,5,6]
# x = 40
# print(low_bound(a,x))

#######################   peak element    ########################
# by linear
# def get_peak(l):
#     n = len(l)
#     if l[0]>l[n-2]:
#         return 0
#     if l[n-1] > l[n-2]:
#         return n-1
#     if n==1:
#         return 0
#     for i in range(1,n-1):
#         if (l[i]>l[i+1]) & (l[i]> l[i-1]):
#             return i
#     return -1

# a=[3,4,5,10,6,7,8]
# print(get_peak(a))

###############################################################

# def first_last(l,x):
#     first =-1
#     last = -1
#     for i in range (len(l)):
#         if(l[i] != x):
#             continue
#         if(first ==-1):
#             first = i
#         last = i
#     return [first,last]

# a = [1,2,5,5,5,6,7]
# x = 5
# print(first_last(a,x))





###############################################################



def fac(n):
    if n == 0:
        return 1
    else:
        return n*fac(n-1)
print(fac(6))













































































