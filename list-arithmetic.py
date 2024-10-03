from itertools import chain
def tri_prob_1(A,B,C: list[int]) -> int:
    D:int = 0
    for i in range(3):
        D += (A[i] * B[i]) - C[i]
    return D

def tri_prob_2(A,B,C: list[int]) -> list[int]:
    D:list[int] = []
    for i in range(3):
        D.append((A[i] * B[i]) - C[i])
    return D

def interlace(lists): # must be of equal length
    return ([x for t in zip(*lists) for x in t])

#return the middle number or the average of the middle two if an even length
def median(A:list[int]) -> float:
    A = sorted(A)
    if len(A) <= 0:
        return -1 #error
    if len(A)%2==0:
        return A[len(A)//2]
    else:
        return sum(A[len(A)//2:(len(A)//2)+1])/2

mean = lambda x:sum(x)/len(x) if len(x)>0 else -1

def tri_prob_3(A,B,C: list[int]) -> list[list[float]]:
    meanA=mean(A)
    meanB=mean(B)
    meanC=mean(C)
    medianA=median(A)
    medianB=median(B)
    medianC=median(C)
    return [[meanA,medianA],[meanB,medianB],[meanC,medianC]]


print("input values for problem 1 and 2 must be integers and separated by spaces")
A=[*map(int,input("A = ").split())]
B=[*map(int,input("B = ").split())]
C=[*map(int,input("C = ").split())]
D=tri_prob_1(A,B,C)
print("====Problem 1====")
print("({} * {} - {}) + ({} * {} - {}) + ({} * {} - {}) =".format(*interlace([A,B,C])),D)


print("/n====Problem 2====")
D=tri_prob_2(A,B,C)
for i in range(3):
    print("({} * {} - {}) = {}".format(A[i],B[i],C[i],D[i]))

print("/n====Problem 3====")
print("enter D if you want to use thedefault lists given by the example code")
if input().upper() == "D":
    A=[3,2,1,4,5]
    B=[10, 8, 5, 3, 6, 8, 8, 6, 7, 3, 6, 4, 6, 10, 6, 6, 9, 6, 10, 8, 4, 6, 5, 7, 4, 5, 2, 4, 2, 6, 10, 3, 2, 5, 5, 6, 4, 3, 2, 9, 3, 5, 9, 9, 9, 6, 7, 5, 5, 6, 5, 8, 10, 4, 9, 3, 3, 10, 7, 8, 2, 6, 4, 7, 9, 9, 8, 8, 3, 9, 7, 4, 3, 9, 8, 4, 9, 3, 7, 2, 10, 10, 8, 6, 4, 7, 10, 8, 4, 4, 5, 4, 9, 3, 8, 2, 5, 8, 10, 5, 10, 7, 2, 3, 3, 5, 3, 4, 8, 10, 9, 7, 5, 9, 5, 5, 2, 6, 10, 9, 4, 2, 9, 10, 7, 10, 8, 4, 10, 6, 10, 10, 4, 2, 6, 2, 3, 5, 8, 5, 10, 8, 7, 5, 10, 7, 5, 9, 5, 5, 10, 5, 7, 2, 3, 2, 2]
    C=[]
else:
    print("input numbers separated by spaces")
    A=[*map(int,input("A = ").split())]
    B=[*map(int,input("B = ").split())]
    C=[*map(int,input("C = ").split())]
D=[*chain(*tri_prob_3(A,B,C))]
for i in range(0,6,2):
    print(f"Mean{(i//2)+1} = {round(D[i],3) if D[i]!=-1 else 'undef'}; Median{(i//2)+1} = {round(D[i+1],3) if D[i+1]!=-1 else 'undef'}")

