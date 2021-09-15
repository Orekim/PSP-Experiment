year = int(input("Enter year: "))

if year%4:
    print(f"{year} is a common year.")
elif year%100:
    print(f"{year} is a leap year.")
elif year%400:
    print(f"{year} is a common year.")
else:
    print(f"{year} is a leap year.")
    