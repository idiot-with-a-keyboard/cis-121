db_cooper : dict[str,int] = {}

def get_modes(numbers: list[int]) -> list[int] :
    occurances: dict[int,int] = {}
    for i in numbers:
        if i in occurances.keys():
            occurances[i] += 1
        else:
            occurances[i] = 1
    output = [*occurances.keys()]
    output.sort()
    for i in output:
        if i < output[0]:
            output.remove(i)
    return output
#                       should never be input a string but the type hinting is there so that my codeserver doesn't whine
def stringify(phone_number:int | str) -> str: #strictly 10 digits only
    phone_number = str(phone_number)
    return f"{phone_number[0:3]}-{phone_number[3:7]}-{phone_number[7:10]}"

def numify(str_number:str) -> int:
    if not(len(inp) == 10 or len(inp)==12): #simple and dashed american phone number format
        quit("Recieved an invalid format for a phone number")
    if len(inp)==10:
        return int(str_number)
    elif len(inp)==12:
        return int("".join(str_number.split("-")))
    else:
        quit("Write your last will and testament for the apocalypse is upon ye.")

inp:str = ""
name:str | list[str] = ""
while inp != "quit":
    inp = input("Name and Number: ")
    if inp != "quit":
        name = inp.split() # i know, misnomer, but im lazy and using it for data processing, sue me

        if not(len(name) >= 2):
            quit("Must input a name and a phone number formatted like so:/Name(arbitrary number of identifiers supported) 0123456789 OR 012-345-6789")

        inp = name[-1]
        name = " ".join(name[:-1])

        if len(inp)==10 or len(inp)==12:
            db_cooper[name] = numify(inp)
        else:
            print("error",inp,name)
            quit()

data_set_1 = [3,3,2,2,2,2,4,4,4,14,14]
data_set_2 = [
		10, 8, 5, 3, 6, 8, 8, 6, 7, 3, 6, 4, 6, 10, 6, 6, 9, 6, 10, 8, 
		4, 6, 5, 7, 4, 5, 2, 4, 2, 6, 10, 3, 2, 5, 5, 6, 4, 3, 2, 9, 3, 
		5, 9, 9, 9, 6, 7, 5, 5, 6, 5, 8, 10, 4, 9, 3, 3, 10, 7, 8, 2, 6, 
		4, 7, 9, 9, 8, 8, 3, 9, 7, 4, 3, 9, 8, 4, 9, 3, 7, 2, 10, 10, 8, 
		6, 4, 7, 10, 8, 4, 4, 5, 4, 9, 3, 8, 2, 5, 8, 10, 5, 10, 7, 2, 
		3, 3, 5, 3, 4, 8, 10, 9, 7, 5, 9, 5, 5, 2, 6, 10, 9, 4, 2, 9, 
		10, 7, 10, 8, 4, 10, 6, 10, 10, 4, 2, 6, 2, 3, 5, 8, 5, 10, 8, 
		7, 5, 10, 7, 5, 9, 5, 5, 10, 5, 7, 2, 3, 2, 2
	]
data_set_3 = [1,2,2,2,3,3,4,4,4,5]
data_sets = [data_set_1,data_set_2,data_set_3]
print("Your phonebook is:")
for i in db_cooper.keys():
    print(i,db_cooper[i])
print("The modes of the thingies are:")
for i in data_sets:
    print(i)
    print("Mode(s):", get_modes(i))
