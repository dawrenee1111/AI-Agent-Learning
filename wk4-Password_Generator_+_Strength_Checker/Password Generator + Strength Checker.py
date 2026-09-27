import random
import string
favorite_passwords = []
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password
def check_strength(password):
    length = len(password)
    has_lower = False
    has_capital = False
    has_punctuation = False
    has_digit = False
    for char in password:
        if char in string.ascii_lowercase:
            has_lower = True
        elif char in string.ascii_uppercase:
            has_capital = True
        elif char in string.punctuation:
            has_punctuation = True
        elif char in string.digits:
            has_digit = True
    score = sum([length>=8, has_lower, has_capital, has_punctuation, has_digit])
    if score <= 2:
        return "Weak"
    elif score <=4:
        return "Moderate"
    elif score == 5:
        return "Strong"
def main():
    while True:
        choice = input("=== MENU ===\n1. Generate Password\n2.Check Password's Strength\n3. View Favorites\n4. Exit\nChoose an option (1-4): ")
        if choice == "1":
            pwd_len = input("Enter password length (default 12): ")
            if pwd_len.isdigit():
                length=int(pwd_len)
            else:
                length=12
            pwd = generate_password(length)
            print(f"\nGenerated Password: {pwd}")
            print(f"Strength: {check_strength(pwd)}")
            save = input("Save to favourites? (y/n): ").lower()
            if save == "y":
                favorite_passwords.append(pwd)
                print("Saved successfully!\n")
        elif choice == "2":
            pwd = input("Enter password to check: ")
            print(f"\nPassword assessment: {check_strength(pwd)}")
            save = input("Save to favourites? (y/n): ").lower()
            if save == "y":
                favorite_passwords.append(pwd)
                print("Saved successfully!\n")
        elif choice == "3":
            print("\n=== Saved Favorites ===")
            if not favorite_passwords:
                print("No passwords saved yet.")
            else:
                for index, password in enumerate(favorite_passwords):
                    print(f"{index}. {password}")
        elif choice == "4":
            print("Goodbye! Stay strong...")
            break
        else:
            print("Invalid choice! Please pick 1, 2, 3, or 4.")
main()    