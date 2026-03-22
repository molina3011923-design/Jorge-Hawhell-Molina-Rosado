name = input("What's your name? ")
years = int(input("How old are you? "))
proyects = int(input("How many projects do you have? "))

print("\nReviewing application...\n")

if proyects >= 3 and years >= 20:
    print(f"{name}, you are a top candidate. We'll contact you soon.")
elif proyects >= 2 and years >= 16:
    print(f"{name}, we’ll review your profile and contact you for more details.")
elif years >= 14:
    print(f"{name}, you are still young. Keep learning and building projects.")
else:
    print(f"{name}, you are too young for this program.")
    
