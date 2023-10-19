A = int(input("Tamil: "))
B = int(input("English: "))
C = int(input("Maths: "))
D = int(input("Phy: "))
E = int(input("Che: "))
F = int(input("CS: "))

sum_marks = A + B + C + D + E + F
margin_marks = 40

if A > margin_marks and B > margin_marks and C > margin_marks and D > margin_marks and E > margin_marks and F > margin_marks:
    print("Pass")
else:
    print("Fail")

if sum_marks > 450:
    print("Grade A")
elif sum_marks > 390:
    print("Grade B")
elif sum_marks > 350:
    print("Grade C")
else:
    print("Fail")