human_to_dog_year = lambda years:years*7 #inline lambda functions to convert from human to animal years
human_to_cat_year = lambda years:years/9
human_to_horse_year=lambda years:3*((((years**2)-47)/7)+12)
                            #weird ahh horse years function

def float_year_to_YMD(year: float) -> list[float]: #type hinting we love to see it
        outlist=[0,0,0]
        days=year*360
        outlist[0]=(days//360) # years
        days = days % 360 #set to remainder of days to year conversion
        outlist[1]=(days//30) # months, which are all 31 days because i said so
        days = days % 30 #again, remanider of days to months
        outlist[2]=days #just the leftovers
        return outlist

input_age = float(input("Enter your age: "))
#gets input and converts it to float
print("Your age in dog years is: {:.0f} years, {:.0f} months, and {:.0f} days.".format(*float_year_to_YMD(human_to_dog_year(input_age))))
print("Your age in cat years is: {:.0f} years, {:.0f} months, and {:.0f} days.".format(*float_year_to_YMD(human_to_cat_year(input_age))))
print("Your age in horse(?) years is: {:.0f} years, {:.0f} months, and {:.0f} days.".format(*float_year_to_YMD(human_to_horse_year(input_age))))
#{} and .format inputs the data from the format function into the {}s
#the :.0f rounds the float into int
#* after a list unpacks the list, allowing you to just shove output from a function
