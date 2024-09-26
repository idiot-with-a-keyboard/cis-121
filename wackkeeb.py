def decode_wack(wack_str:str) -> str:
    wack_str = wack_str.upper() #just in case
    output:str = ""
    wack_index:int = 0
    trans_dict = {'L':'T',
                  'T':'L',
                  '8':'A',
                  'B':'A',
                  'A':'E',
                  #'UU':'W',
                  'E':'B'}

    while True:
        #check if done
        if wack_index >= len(wack_str):
            break

        #check for the w
        cur_char = wack_str[wack_index]
        if cur_char == 'U' and wack_str[wack_index:wack_index+2] == 'UU': #check for W
            output += 'W'
            wack_index += 2
            continue

        #add the non W translated char to output
        if cur_char in trans_dict.keys():
            output += trans_dict[cur_char]
        else:
            output += cur_char

        #increment the thingy
        wack_index += 1
    return output


def main():
    wack_str:str = ""
    list_of_ex_strs:list[str] = ["WBLARF8TTS","L8KAOUL","E8N8N8","8TRA8DY T8LA","8TT LHA TILLTA LIMAS","LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS","TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY","UUHO","EOUUUUOUU"]

    choice:str = input("Do you want to test a custom string or ron through all provided examples? (C or E):")

    match choice.upper():
        case 'C':
            wack_str = input("Input custom string:")
            print(f"{wack_str} -> {decode_wack(wack_str)}")
        case 'E':
            for i in list_of_ex_strs:
                print(f"{i} -> {decode_wack(i)}")
        case _:
            quit("That was not C or E.")



#i guess ill start doing this now, never really understeed this if im not specifically writing a library of custom functions
if __name__ == "__main__":
    main()

