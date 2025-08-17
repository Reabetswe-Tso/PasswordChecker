# Password Strength Checker (Python)

This is a simple Python script that checks the strength of a password using **regular expressions (Regex)**.  
It evaluates a password based on **length, digits, uppercase letters, lowercase letters, and special characters**.

---

## Features
- Checks if the password:
  - Has at least 8 characters  
  - Contains at least one digit (`0-9`)  
  - Contains at least one uppercase letter (`A-Z`)  
  - Contains at least one lowercase letter (`a-z`)  
  - Contains at least one special character (`@, $, !, %, *, ?, &`)  

- Returns one of three results:
  - ✅ **Strong password**  
  - ⚠️ **Medium strength** (needs more complexity)  
  - ❌ **Weak password** (too simple)

---

## How It Works
1. The user enters a password.  
2. The program checks it against different security rules using **Regex**.  
3. The result is displayed as `Strong`, `Medium`, or `Weak`.  
---

## Usage
Run the script in your terminal:

```bash
python password_checker.py
```
Enter your password to check: Strong@123
Strong password ✅

## Example Outputs
1. Enter your password to check: abc
Weak password ❌ - Too simple
2. Enter your password to check: Abc123
Medium strength ⚠️ - Try adding more complexity
3. Enter your password to check: Abc@12345
Strong password ✅

## Author
Reabetswe Tsotetsi

