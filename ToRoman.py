import os
import sys

numerals = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}


def toRoman(inp):
    nums = sorted(numerals, reverse=True)
    out = ""

    if inp < 0:
        raise ValueError()

    while inp > 0:  
        current_num = nums[0]
        if current_num <= inp:
            inp -= current_num
            out += numerals[current_num]
        else:
            if current_num//5 in nums:
                if current_num - current_num//5 <= inp:
                    inp -= current_num - current_num//5
                    out += numerals[current_num//5] + numerals[current_num]
                else:
                    nums.remove(current_num)
            elif current_num//10 in nums and str(current_num)[0] == "1":
                if current_num - current_num//10 <= inp:
                    inp -= current_num - current_num//10
                    out += numerals[current_num//10] + numerals[current_num]
                else:
                    nums.remove(current_num)
            else:
                nums.remove(current_num)
    
    return out


def fromRoman(inp):
    try:
        if not isinstance(inp, str):
            raise KeyError()
        out = fromRomanRecurse(inp)[0]
    except KeyError:
        out = "Not accepted"
    return out

def fromRomanRecurse(inp, big_value=None):

    if len(inp) == 0:
        return 0, 0

    if len(inp) == 1:
        if big_value is None or values[inp] < big_value:
            return values[inp], 0
        else:
            raise KeyError

    total = 0

    char = inp[0]

    if str(values[char])[0] == "1" and values[inp[1]]//values[char] in [5,10]:
        char2 = inp[1]
        total += values[char2] - values[char]
        if len(inp) == 2:
            if big_value is not None and total >= big_value:
              raise KeyError()
            return total, 0
        big_value = values[char]
        recieved = fromRomanRecurse(inp[2:], big_value)
    else:
        big_value = values[char] + 1
        total += values[char]
        recieved = fromRomanRecurse(inp[1:], big_value)
    if recieved[1] > big_value:
        raise KeyError()
    total += recieved[0]
    
    return total, total-recieved[0]

def romanConvert(inp_raw):
    try:
        inp = int(inp_raw)
        out = toRoman(inp)
    except ValueError:
        out = fromRoman(inp_raw)
    return str(out)
    
        


tests = open(os.path.join(sys.path[0], 'RomanUnitTests.txt'), "r").readlines()

for line in tests:

    line = line.split("\n")[0]
    
    inp_raw = line.split(", ")[0]

    try:
        expected = line.split(", ")[1]
    except IndexError:
        expected = ""

    out = romanConvert(inp_raw)
    
    if out == expected:
        print(f"Test, input {inp_raw} Passed")
    else:
        print(f"Test, input {inp_raw} FAILED, expected {expected}, got {out}")
        break

inp_raw = input("Enter value (quit to quit): ")

while inp_raw != "quit":
    out = romanConvert(inp_raw)
    if out == "Not accepted":
        print("Input must be a non-negative integer or valid string of Roman numerals")
    else:
        print(f"{inp_raw} -> {out}")

    inp_raw = input("Enter number (quit to quit): ")