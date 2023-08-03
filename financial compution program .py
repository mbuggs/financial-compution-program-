Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
... 
... def compute_payment(PV, r, n):
...     r = r / 12.0
...     payment = PV * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
...     return payment
... 
... def compute_PV(pmt, r, n):
...     r = r / 12.0
...     PV = pmt / (r * (1 - (1 + r) ** -n))
...     return PV
... 
... def compute_months(PV, r, pmt):
...     r = r / 12.0
...     n = np.log(1 - PV * r / pmt) / np.log(1 + r)
...     return n
... 
... def compute_missing_variable(PV, pmt, r, n):
...     if PV is None:
...         return compute_PV(pmt, r, n)
...     elif pmt is None:
...         return compute_payment(PV, r, n)
...     elif r is None:
...                 r_guess = 0.1  
...         tolerance = 1e-6  
...         max_iterations = 1000
... 
...         for _ in range(max_iterations):
...             pmt_calculated = compute_payment(PV, r_guess, n)
...             error = pmt_calculated - pmt
... 
...             if abs(error) < tolerance:
...                 return r_guess
... 
...             r_guess -= error * 0.01  
... 
...         raise ValueError("Failed to converge in computing r")
    elif n is None:
        return compute_months(PV, r, pmt)


PV = 10000
pmt = 500
r = 0.06
n = None


n = compute_missing_variable(PV, pmt, r, n)
print("Number of months to pay off the loan:", n)


r = compute_missing_variable(PV, pmt, None, n)
print("Annual interest rate (as decimal):", r)


