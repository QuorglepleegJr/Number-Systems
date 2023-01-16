import os
import sys

numerals = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
nums = sorted(numerals, reverse=True)

tests = open(os.path.join(sys.path[0], 'RomanUnitTests.txt'), "r").readlines()

for line in tests:

    line = line.strip()
    
    inp_raw = line.split(", ")[0]

    expected = line.split(", ")[1]

    out = ""

    try:
        inp = int(inp_raw)

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

    except ValueError:
        out = "Not accepted"
    
    if out == expected:
        print(f"Test, input {inp_raw} Passed")
    else:
        print(f"Test, input {inp_raw} FAILED, expected {expected}, got {out}")
        break