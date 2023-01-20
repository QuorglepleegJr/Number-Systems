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
        pass

    def __sub__(a, b):
        pass

    def __mul__(a, b):
        return Rational(a.num * b.num, a.den * b.den)

    def __div__(a, b):
        return Rational(a.num * b.den, a.den * b.num)
    
    def __eq__(a, b):
        return a.num == b.num and a.den == b.den

    def __repr__(self):
        return str(self.num) + "/" + str(self.den)

    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.__simplify()
    
    def __simplify(self):
        pass