a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
d = int(input("Enter 4th number: "))
if a > b and a > c and a > d and a == a:
    print("1st is the greatest number.")
elif b > a and b > c and b > d and b == b:
    print("2nd is the greatest number.")
elif c > a and c > b and c > d and c == c:
    print("3rd is the greatest number.")
elif d > a and d > b and d > c and d == d:
    print("4th is the greatest number.")
else:
    print("Plz Enter number!!")
