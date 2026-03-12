# This function is returning multiple values
def rectangle(length, width):
    area = length * width
    paramter = length + length + width + width
    return area, paramter

l = int(input("Enter length : ").strip())
w = int(input("Enter Width: ").strip())
a , p = rectangle(l,w)
print(f"Area: {a} , Parameter: {p}")