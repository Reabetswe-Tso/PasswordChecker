import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[@$!%*?&]", password) is None
    
    if not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error):
        return "Strong password ✅"
    elif len(password) >= 6:
        return "Medium strength ⚠️ - Try adding more complexity"
    else:
        return "Weak password ❌ - Too simple"

# Ask user for password
password = input("Enter your password to check: ")
print(check_password_strength(password))
