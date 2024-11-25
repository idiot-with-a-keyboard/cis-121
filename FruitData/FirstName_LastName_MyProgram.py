import FirstName_LastName_Stats as stats


data = stats.read_data("500DayFruitData.txt")
#static initialization
mean:float = 0
means:list[float] = []
median:float = 0
medians:list[float] = []

defined_fruits:list[str] = ["apple", "banana", "strawberry", "*"]

for i in defined_fruits:
    mean = stats.calc_mean_of(data,i)
    median = stats.calc_median_of(data,i)
    means.append(mean)
    medians.append(median)

with open("FirstName_LastName_Output.txt",'w') as f:
    f.write(f"The mean number of apples is {means[0]:.2f}\n")
    f.write(f"The median number of apples is {medians[0]:.2f}\n")

    f.write(f"The mean number of bananas is {means[1]:.2f}\n")
    f.write(f"The median number of bananas is {medians[1]:.2f}\n")

    f.write(f"The mean number of strawberries is {means[2]:.2f}\n")
    f.write(f"The median number of strawberries is {medians[2]:.2f}\n")

    f.write(f"The mean number of all fruits is {means[3]:.2f}\n")
    f.write(f"The median number of all fruits is {medians[3]:.2f}\n")
