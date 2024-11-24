import pykbtcal

print ("\n--Basic Python Arithmetic Operations--")

def arithmetic(num1,num2):
    sum = pykbtcal.add_numbers(num1, num2)
    difference = pykbtcal.subtract_numbers(num1, num2)
    product = pykbtcal.multiply_numbers(num1, num2)
    quotient = pykbtcal.divide_numbers_float(num1, num2)

    print (f"\n{sum}")
    print (difference)
    print (product)
    print (f"{quotient}\n")

def main():
    n1 = int(input("\nEnter 1st number: "))
    n2 = int(input("Enter 2nd number: "))

    arithmetic(n1, n2)

if __name__ == "__main__":
    main()
