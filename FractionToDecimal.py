dividend = int(input())
divisor = int(input())

out = ""

found_remainders = []

current_remainder = 0

multiple = dividend//divisor

out += str(multiple)

out += "."

while current_remainder not in found_remainders:
    current_remainder = dividend - multiple * divisor
    found_remainders.append(current_remainder)
    dividend = 10 * current_remainder
    multiple = dividend//divisor
    out += str(multiple)

print(out)