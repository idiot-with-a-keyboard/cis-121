human_to_dog_year = lambda years:years*7
#inline lambda function to multiply a number by 7, the factor that converts human years to dog years
input_age = float(input("Enter your age: "))
#gets input and converts it to float
print(f"Your age in dog years is: {human_to_dog_year(input_age):.3f}")
#prints the output using an f-string. said output is the previously input age multiplied using the conversion function
#said output is rounded to the nearest thousandth using the :.3f to avoid ugly floating point garbage output like 14.700000000000001
