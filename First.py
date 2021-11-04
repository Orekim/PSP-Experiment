x = int(input("Enter numerator #1: "))
y = int(input("Enter denomirator #1: "))
a = int(input("Enter numerator #2: "))
b = int(input("Enter denomirator #2: "))

A = x * b
B = y * b
C = a * y
D = b * y

Nume = A + C
sum = (A / B) + (C/D)

print(f"{x} / {y} + {a} / {b} = {Nume} / {B}")
print("Testting.....")
