def check_password_strength(password):
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Check for numbers
    if any(char.isdigit() for char in password):
        score += 1

    # Check for special characters
    if any(not char.isalnum() for char in password):
        score += 1

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        score += 1

    # Check for lowercase letters
    if any(char.islower() for char in password):
        score += 1

    # Rate password
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


password = input("Enter your password: ")
strength = check_password_strength(password)

print("Password strength:", strength)