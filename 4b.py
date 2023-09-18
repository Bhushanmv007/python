def rom2dec(rom_str):
    rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rom_back = list(rom_str)[::-1]
    value = 0
    rightVal = rom_dict[rom_back[0]]
    for numeral in rom_back:
        leftVal = rom_dict[numeral]
        if leftVal < rightVal:
            value -= leftVal
        else:
            value += leftVal
        rightVal = leftVal
    return value

romanStr = input("Enter a Roman number: ")
print(rom2dec(romanStr))