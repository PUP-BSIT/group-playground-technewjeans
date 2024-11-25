from nara import CreateFunc

CreateFunc()
def calculate_area_and_input():

    print ("\n--Calculate the area of a rectangle--")

    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))

    area = length * width

    print(f"The area of the rectangle is: {area}")

if __name__ == "_main_":
    calculate_area_and_input()