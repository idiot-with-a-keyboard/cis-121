
def BubbleSort(data:list[int]) -> list[int]:
    has_swapped:bool = True
    index:int = 0
    while has_swapped:
        index = 0
        has_swapped = False
        while index < len(data)-1:
            if data[index] > data[index+1]: #if the current number is bigger than the one after it
                has_swapped = True
                data[index+1],data[index] = data[index],data[index+1] # swap the number at the index with the one after it
            index += 1
    return data




def read_data(filename:str) -> list[tuple[int,str,int]]: #read data and output it in a easy to parse format
    with open(filename,'r') as f:
        #static type initialization
        output:list[tuple[int,str,int]] = []
        s_day:str = ""
        fruit:str = ""
        s_amnt:str = ""
        day:int = 0
        amnt:int = 0

        for dirty_line in f.readlines(): #loop through the lines in the file
            line = dirty_line.strip() #cleans up the data by removing newline should it be there
            if line[:3] == "Day": continue #skips past the title line

            s_day,fruit,s_amnt = line.split() #split the string by spaces into unprocessed integers as strings and the fruit name

            day = int(s_day[4:]) #removes the day_ prefix and converts the integer as a string into an integer
            amnt = int(s_amnt) #converts the amount from an integer as a string into an integer

            output.append((day,fruit,amnt)) #add the tuple to the output list
    return output

def calc_mean_of(data:list[tuple[int,str,int]], item:str) -> float: #calculate the mean/average of the amount of an arbitrary fruit consumed on days they were eaten
    #static type initialization
    only_item_days:list[int] = []

    for i in data:
        if i[1] == item or item == "*":
            only_item_days.append(i[2])

    return sum(only_item_days)/len(only_item_days)

def calc_median_of(data:list[tuple[int,str,int]], item:str) -> float: #calculate the median of the amount of an arbitrary fruit consumed on days they were eaten
    #static type initialization
    only_item_days:list[int] = []
    midpoint:(float|int) = 0

    for i in data:
        if i[1] == item or item == "*":
            only_item_days.append(i[2])

    only_item_days = BubbleSort(only_item_days)

    midpoint = (len(only_item_days)-1) / 2

    if len(only_item_days) % 2 != 0: #if odd length
        return only_item_days[int(midpoint)]
    else: #if even length
        return sum(only_item_days[int(midpoint-0.5):int(midpoint+0.5)+1])/2 #return average of the two values
