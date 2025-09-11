def TOH(n,source,aux,dest):
    if n==1:
        print(source,"-->",dest)
    else:
        TOH(n-1,source,dest,aux)
        print(source,"-->",dest)
        TOH(n-1,aux,source,dest)
n = int(input("enter no. of disc: "))
TOH(n,"A","B","C")
