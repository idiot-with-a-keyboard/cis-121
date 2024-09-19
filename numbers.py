def proper_divisors(num:int) -> list[int]:
    output = []
    [output.append(i) for i in range(1,num) if num % i == 0] #adds i to output if it is a divisor
    return output

abundant_numbers:int=0
deficient_numbers:int=0
perfect_numbers:int=0
upper_bound:int = int(input("Enter an upper bound for a check: "))

sum_of_divisors:int = 0

for i in range(1,upper_bound+1): #for some reason the example also checks the upper bound idk if its supposed to
    sum_of_divisors = sum(proper_divisors(i))
    if sum_of_divisors > i: #check if abundant
        abundant_numbers+=1
    elif sum_of_divisors < i: #check if deficient
        deficient_numbers+=1
    else:                   #set to perfect if neither
        perfect_numbers+=1
print(f"""Between 1 and 20 there are
 {deficient_numbers} deficient numbers
 {perfect_numbers} perfect numbers
 {abundant_numbers} abundant numbers""")
