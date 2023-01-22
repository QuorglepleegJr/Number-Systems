class Rational():


    # TO FINISH - ADD ADD, SUB, LESSER

    def __get_p_factors(a):
        a_div = []

        primes = []

        current = 1

        while a > 1:
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
        #TEMPORARY INEFFECIENT METHOD
        
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
        num = a.num*lcm/b.den + b.num*lcm/a.den
        return Rational(num, lcm)


    def __sub__(a, b):
        if isinstance(b, int) or isinstance(b, float):
            return Rational(a.num - b*a.den, a.den)
        if not isinstance(b, Rational):
            raise ValueError("Unsupported types for subtraction")
        lcm = Rational.__get_cd(a.den, b.den)
        num = a.num*lcm/b.den - b.num*lcm/a.den
        return Rational(num, lcm)

    def __mul__(a, b):
        if isinstance(b, int) or isinstance(b, float):
            return Rational(a.num*b, a.den)
        if not isinstance(b, Rational):
            raise ValueError("Unsupported types for multiplication")
        return Rational(a.num * b.num, a.den * b.den)

    def __div__(a, b):
        if isinstance(b, int) or isinstance(b, float):
            return Rational(a.num, a.den*b)
        if not isinstance(b, Rational):
            raise ValueError("Unsuppported types for division")
        return Rational(a.num * b.den, a.den * b.num)
    
    def __eq__(a, b):
        return a.num == b.num and a.den == b.den

    def __gt__(a, b):
        return a.num/a.den > b.num/b.den

    def __repr__(self):
        return str(self.num) + "/" + str(self.den)

    def __new__(cls, num, den):
        if int(num/den) == num/den:
            return int(num/den)
        return super().__new__(Rational)


    def __init__(self, num, den):
        if not isinstance(num, int) and not isinstance(num, float):
            raise ValueError("Invalid type for numerator of rational")
        if not isinstance(den, int) and not isinstance(den, float):
            raise ValueError("Invalid type for denominator of rational")
        if den == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        self.num = num
        self.den = den
        self.__simplify()

    def __simplify(self):
        if isinstance(self.den, float):
            scale = len(str(self.den).split("."))
            self.den = int(self.den*10**scale)
            self.num = int(self.num*10**scale)
        if isinstance(self.num, float):
            scale = len(str(self.num).split("."))
            self.den = int(self.den*10**scale)
            self.num = int(self.num*10**scale)

        hcf = Rational.__get_hf(self.num, self.den)
        self.num //= hcf
        self.den //= hcf
        