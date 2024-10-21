
def calc_toll(cur_hour:int, is_morning:bool, is_weekend:bool) -> float:
    if not(is_morning): #really could have just used 24h format :/
        cur_hour += 12
    h = cur_hour # to make typing and reading easier/faster
    if not(is_weekend):
        if h < 7:      return 1.15
        if h < 10:     return 2.95
        if h < 3  +12: return 1.90 #+12 means pm
        if h < 8  +12: return 3.95
        if h > 8  +12: return 1.10
    else: #again +12 = pm
        if h < 7:      return 1.05
        if h < 8  +12: return 2.15
        if h > 8  +12: return 1.10

    return -1 #error

def is_divisible(num,divisor:int) -> bool:
    return (num % divisor == 0)

def lowest_common_multiple(lower_num:int, higher_num:int) -> int:
    #assuming we can't just import math.lcm lol
    if higher_num>lower_num:
        lower_num,higher_num=higher_num,lower_num # y should be the higher number, this swaps the two if the lower is higher
    if higher_num==lower_num:
        return lower_num

    lkcm = lower_num * higher_num #least known common multiple
    for i in range(1,(lower_num * higher_num)+1):
        if not(is_divisible(lower_num,i) and is_divisible(higher_num,i)):
            continue #skip over setting the lcm if it isn't a common multiple
        if lkcm > i and i!=1:
            lkcm = i
    return lkcm

def factorial(num) -> int:
    output:int = 1
    for i in range(1,num+1):
        output *= i
    return output

def combination(m:int|float,k:int|float) -> float:
    return factorial(m)  /  (factorial(k) * factorial(m-k))

def pascal():
    buffer=""
    output=""
    for i in range(10):
        for j in range(i+1):
            buffer += f"{int(combination(i,j))} "
        output += buffer.center(30) + "\n" #magic number to make it look pretty
        buffer = ""
    print(output)


if __name__ == "__main__":
    print("Input two numbers for LCM:")
    x,y=map(int,[input("Number 1:"),input("Number 2:")])
    print("LCM=",lowest_common_multiple(x,y))
    
    print("Input an hour, and two 1's or 0's to determine whether or not it is morning or a weekend respectively.")
    x=int(input("Hour:"))
    y,z=map(bool,[input("Morning?:"),input("Weekend?:")])
    print("Toll:",calc_toll(x,y,z))

    pascal()
