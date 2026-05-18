class Polynomial:
    def __init__(self, coefficients):        
        self.coeffs = coefficients

    def __call__(self, x):
        res = 0
        n = len(self.coeffs)
        for i, c in enumerate(self.coeffs):
            power = n - 1 - i
            res += c * (x ** power)
        return res

    def __add__(self, other):
        c1 = self.coeffs[::-1] 
        c2 = other.coeffs[::-1]
        
        max_len = max(len(c1), len(c2))
        c1 += [0] * (max_len - len(c1))
        c2 += [0] * (max_len - len(c2))
        
        res_coeffs = [(a + b) for a, b in zip(c1, c2)]
        return Polynomial(res_coeffs[::-1]) 

    def __str__(self):
        n = len(self.coeffs)
        if not self.coeffs or all(c == 0 for c in self.coeffs):
            return "0"
        
        terms = []
        for i, c in enumerate(self.coeffs):
            if c == 0:
                continue
            
            power = n - 1 - i
            
            abs_c = abs(c)
            coeff_str = ""
            
            if power == 0:
                coeff_str = str(abs_c)
            elif abs_c != 1:
                coeff_str = str(abs_c)
            
            var_str = ""
            if power > 0:
                var_str = "x"
                if power > 1:
                    var_str += "^" + str(power)
            
            term = coeff_str + var_str
            
            if not terms: 
                if c < 0:
                    terms.append("-" + term)
                else:
                    terms.append(term)
            else:
                op = " + " if c > 0 else " - "
                terms.append(op + term)
                
        return "".join(terms)