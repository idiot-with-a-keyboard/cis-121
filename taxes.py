def get_taxed_amount(income:float, married:bool) -> float:
    taxed_amount:float = 0
    taxes_list =  [[0,0],
                  [11_000,  22_000],
                  [44_725,  89_450],
                  [95_375,  190_750],
                  [182_100, 364_200],
                  [231_250, 462_500],
                  [578_125, 693_750],
                  [1e250, 1e250]]
    taxed_perc_list = [0,10,12,22,24,32,35,37] #yoinked from the 2023 IRS tax bracket
    for i in taxes_list[1:]: # runs through the tax bracket cutoffs
        tax_index:int = taxes_list.index(i)

        tax_range:int = i[married] - taxes_list[tax_index-1][married]
#        ^returns the current tax limit - previous tax limit, giving the tax range
#         distincted between married and unmarried brackets with a bool implicit conversion to an int

        tax_perc:int = taxed_perc_list[tax_index] #gets the current tax percentage
        if income > tax_range: #if income can be carried over to the next bracket
            curtax = tax_range * (tax_perc / 100) #set the current tax
            income -= tax_range #remove bracketed cash and set it to the remainder for the next one
            taxed_amount += curtax
        else:
            taxed_amount += income * (tax_perc / 100)
            break #escape from loop when in final bracket
    return taxed_amount

income:float = float(input("How much taxable income do you have as of 2023? "))
married:bool = input("Are you married? y/n: ") == "y" #check if married
taxed:float = get_taxed_amount(income,married)

print(f"You are going to be taxed: {taxed}.")
