class Rational():

    def __get_p_factors(a):
        a_div = []

        primes = []

        current = 1

        while abs(a) > 1:
            current += 1
            prime = True
            for p in primes:
                if current % p == 0:
                    prime = False
            if prime:
                primes.append(current)
            
                while a % current == 0:
                    a_div.append(current)
                    a //= current
        
        return a_div

    def __get_cd(a, b):
        
        a_div = Rational.__get_p_factors(a)
        b_div = Rational.__get_p_factors(b)

        total = 1

        all_facts = set(a_div + b_div)

        for p in all_facts:
            total *= p ** max(a_div.count(p), b_div.count(p))

        return total
    
    def __get_hf(a, b):

        a_div = Rational.__get_p_factors(a)
        b_div = Rational.__get_p_factors(b)

        total = 1

        all_facts = set(a_div + b_div)

        for p in all_facts:
            total *= p ** min(a_div.count(p), b_div.count(p))

        return total

    def __add__(a, b):
        if isinstance(b, int) or isinstance(b, float):
            return Rational(a.num + b*a.den, a.den)
        if not isinstance(b, Rational):
            raise ValueError("Unsupported types for addition")
        lcm = Rational.__get_cd(a.den, b.den)
        num = a.num*lcm/a.den + b.num*lcm/b.den
        return Rational(num, lcm)


    def __sub__(a, b):
        if isinstance(b, int) or isinstance(b, float):
            return Rational(a.num - b*a.den, a.den)
        if not isinstance(b, Rational):
            raise ValueError("Unsupported types for subtraction")
        lcm = Rational.__get_cd(a.den, b.den)
        num = a.num*lcm/a.den - b.num*lcm/b.den
        return Rational(num, lcm)

    def __mul__(a, b):
        if isinstance(b, int) or isinstance(b, float):
            return Rational(a.num*b, a.den)
        if not isinstance(b, Rational):
            raise ValueError("Unsupported types for multiplication")
        return Rational(a.num * b.num, a.den * b.den)

    def __truediv__(a, b):
        if isinstance(b, int) or isinstance(b, float):
            return Rational(a.num, a.den*b)
        if not isinstance(b, Rational):
            raise ValueError("Unsuppported types for division")
        return Rational(a.num * b.den, a.den * b.num)
    
    def __eq__(a, b):
        return a.num == b.num and a.den == b.den

    def __gt__(a, b):
        return a.num/a.den > b.num/b.den

    def __str__(self):
        if self.num < 0 and self.den >=0 or self.num >=0 and self.den < 0:
            return "-" + str(abs(self.num)) + "/" + str(abs(self.den))
        return str(abs(self.num)) + "/" + str(abs(self.den))

    def __init__(self, num, den):
        try:
            new_num = float(num)
            if "e" in str(new_num):
                new_num = int(num)
            num = new_num
        except ValueError:
            raise ValueError("Invalid type for numerator of rational")
        try:
            new_den = float(den)
            if "e" in str(new_den):
                new_den = int(den)
            den = new_den
        except ValueError:
            raise ValueError("Invalid type for denominator of rational")
        if den == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        self.num = num
        self.den = den
        self.__simplify()

    def __simplify(self):
        print(self.num, self.den, str(self.num), str(self.den))
        if isinstance(self.den, float):
            decimal = str(self.den).split(".")[1]
            while len(decimal) > 0 and decimal[-1] == "0":
                decimal = decimal[:-1]
            scale = len(decimal)
            self.den = int(self.den*10**scale)
            self.num = self.num*10**scale
        if isinstance(self.num, float):
            decimal = str(self.num).split(".")[1]
            while len(decimal) > 0 and decimal[-1] == "0":
                decimal = decimal[:-1]
            scale = len(decimal)
            self.den = self.den*10**scale
            self.num = int(self.num*10**scale)

        hcf = Rational.__get_hf(self.num, self.den)
        self.num //= hcf
        self.den //= hcf
        