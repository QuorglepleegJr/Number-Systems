dividend = int(input())
divisor = int(input())

out = ""

negative = False

if dividend < 0:
  negative = not negative
  dividend *= -1
if divisor < 0:
  negative = not negative
  divisor *= -1

found_remainders = []

current_remainder = 0

multiple = dividend//divisor
if multiple < 0:
  multiple += 1

out += str(multiple)

out += "."

current_remainder = dividend - multiple * divisor

while current_remainder not in found_remainders:
    found_remainders.append(current_remainder)
    dividend = 10 * current_remainder
    multiple = dividend//divisor
    out += str(multiple)
    current_remainder = dividend - multiple * divisor
    

out += "\u0307"

index = found_remainders.index(current_remainder)

out = out.split(".")

if len(out) > 1:
  out = out[0] + "." + out[1][:index] + "\u0307" + out[1][index:]
else:
  out = out[0]

if negative:
  out = "-" + out

print(out)