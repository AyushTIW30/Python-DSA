
################    bubble sort    #############################

# def bubble_sort(l):# list l1
#     count = 0
#     n = len(l) # length nikali
#     for i in range(n-1): # range(0,6)
#         is_sorted = True
#         for j in range(n-i-1): # range(0,5)
#             if(l[j]>l[j+1]): # if j>j+1 then swap
#                 is_sorted = False
#                 l[j],l[j+1] = l[j+1],l[j]
#                 count+=1
#         if is_sorted :
#             break
#     print(count)
#     return l # list returned
# a=[5,4,3,2,1]
# print(bubble_sort(a))

##################################################################


# str = "ayush 70 ram 40 mohan 90 rohan 88 sohan 70 rama 65"
# x = 60
# def sort(str,x):
#     my_list = str.split()
#     n = len(my_list)
#     for i in range(n-1,0,-2):
#         if(int(my_list[i])<x):
#             del(my_list[i-1:i+1])

#     n = len(my_list)
#     for i in range(1,n,2):
#         for j in range(1,n-1,2):
#             if my_list[j] < my_list[j+2] or ( my_list[j-1] < my_list[j+1] and my_list[j] == my_list[j+2]):
#                 my_list[j],my_list[j+2] = my_list[j+2],my_list[j]
#                 my_list[j-1],my_list[j+1]=my_list[j+1],my_list[j-1]
#     return " ".join(my_list)
# print(sort(str,x))


##########################################################


# a = [1,0,2,0,5,0,0]
# count=0
# l = []
# for i in range(0,len(a)):
#     if a[i]==0:
#         count+=1
#     else:
#         l.append(a[i])
# for i in range(0,count):
#     l.append(0)

# print(l)


############### selection sort  ########################


def sel_sort(l):
    n = len(l)
    for i in range(n):
        min_val = i
        for j in range(i+1,n):
            if l[j]<l[min_val]:
                min_val=j
        l[i],l[min_val] = l[min_val],l[i]
    return l
l = [5,4,9,7,1]
print(sel_sort(l))









# l = [7,6,5,4,3,2,1]
# b = []
# for i in range(0,len(l)):
#     a = min(l)
#     b.append(a)
#     s = l.index(a)
#     del(l[s])
# print(b)




# def sel_sort(l):
#     n = len(l)


#     for i in range(n):
#         min_ind = i
#         for j in range(i+1,n):
#             if l[j]<l[min_ind]:
#                 min_ind = j
#             l[i],l[min_ind] = l[min_ind],l[i]

#     return l

# a = [5,4,3,2,1]
# print(sel_sort(a))


# def bub(l):
#     n = len(l)

#     for i in range(n-1):
#         is_sorted = True
#         for j in range(n-i-1):
#             if (l[j]>l[j+1]):
#                 is_sorted = False
#                 l[j],l[j+1] = l[j+1],l[j]
#         if is_sorted:
#             break
#     return l

# a = [9,7,5,4,2,1]
# print(bub(a))


#################   insertion sorting   ###################

def insertion_sorting(l):
    for i in range(1,len(l)):
        key = l[i]
        j=i-1
        while j >=0 and key<l[j]:
            l[j+1] = l[j]
            j-=1
        l[j+1] = key
    return l
a=[9,8,7,6,5,1]
print(insertion_sorting(a))























