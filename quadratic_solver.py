
import math

print("=== QUADRATIC EQUATION SOLVER ===")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a == 0:
    print("This is not a quadratic equation.")
else:
    delta = b**2 - 4*a*c

    print("Delta =", delta)

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Two distinct roots:")
        print("x1 =", x1)
        print("x2 =", x2)

    elif delta == 0:
        x = -b / (2*a)
        print("One double root:")
        print("x =", x)

    else:
        print("No real roots.")
