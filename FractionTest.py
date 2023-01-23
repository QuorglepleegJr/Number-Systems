from Fraction import Rational

tests = open("FractionUnitTests.txt", "r").readlines()

for line in tests:
    test = line.split(" : ")
    inp = test[0]
    exp = test[1].split("\n")[0]

    print("Test:", inp)

    try:
        exec("out = str("+inp+")")
    except Exception as e:
        out = str(e)
    
    if out == exp:
        print(f"SUCCESS, input {inp}, output {out}")
    else:
        print(f"FAIL, input {inp},  output {out}, expected {exp}")
        break