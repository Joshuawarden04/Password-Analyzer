import re

def check_length(password):
    """Check if the password length is sufficient."""
    return len(password) >= 8

def check_uppercase(password):
    """Check if the password contains at least one uppercase letter."""
    return any(char.isupper() for char in password)

def check_lowercase(password):
    """Check if the password contains at least one lowercase letter."""
    return any(char.islower() for char in password)

def check_digit(password):
    """Check if the password contains at least one digit."""
    return any(char.isdigit() for char in password)

def check_special(password):
    """Check if the password contains at least one special character."""
    special_characters = r"[@$!%*?&]"
    return re.search(special_characters, password) is not None

def evaluate_password(password):
    """Evaluate the password strength and provide recommendations."""
    score = 0
    recommendations = []

    if check_length(password):
        score += 1
    else:
        recommendations.append("Password should be at least 8 characters long.")

    if check_uppercase(password):
        score += 1
    else:
        recommendations.append("Password should contain at least one uppercase letter.")

    if check_lowercase(password):
        score += 1
    else:
        recommendations.append("Password should contain at least one lowercase letter.")

    if check_digit(password):
        score += 1
    else:
        recommendations.append("Password should contain at least one digit.")

    if check_special(password):
        score += 1
    else:
        recommendations.append("Password should contain at least one special character.")

    if score == 5:
        strength = "Strong"
        recommendations.append("Your password is strong.")
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, recommendations

def main():
    print("Password Analyzer")
    password = input("Enter your password: ")
    strength, recommendations = evaluate_password(password)
    
    print(f"Password Strength: {strength}")
    for recommendation in recommendations:
        print(f"- {recommendation}")

if __name__ == "__main__":
    main()
