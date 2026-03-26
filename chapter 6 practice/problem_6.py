marks = int(input("Enter marks: "))
if marks == 100 or marks >= 90:
    print("EX")
elif marks == 90 or marks >= 80:
    print("A")
elif marks == 80 or marks >= 70:
    print("B")
elif marks == 70 or marks >= 60:
    print("C")
elif marks == 50 or marks > 60:
    print("D")
elif marks < 50:
    print("F")

# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# # <50 => F
