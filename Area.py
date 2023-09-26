def calculate_area(length,width):
    if length==width:
        return "This is a square!"
    else:
        return length*width  #Area =l*b
#taking input
Length=float(input("enter the length: "))
Width=float(input("enter the width: "))
calculated_area = calculate_area(Length,Width)
print(calculated_area)