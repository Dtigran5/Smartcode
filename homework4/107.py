def reduce_fraction(numerator, denominator):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

if __name__ == "__main__":
    num = int(input("Enter the numerator: "))
    denom = int(input("Enter the denominator: "))
    
    reduced_num, reduced_denom = reduce_fraction(num, denom)
    print(f"The reduced fraction is: {reduced_num}/{reduced_denom}")
