"""
Password Strength Checker
A simple tool that evaluates password strength based on common security criteria.

Author: [Nafeez]
"""

import re


def check_password_strength(password):
    """
    Checks a password against common strength criteria and returns
    a score (0-5) along with feedback for improvement.
    """
    score = 0
    feedback = []

    # 1. Length check
    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    # 2. Uppercase letter check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    # 3. Lowercase letter check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    # 4. Digit check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    # 5. Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&* etc.).")

    return score, feedback


def get_strength_label(score):
    """Maps a numeric score to a human-readable strength label."""
    if score <= 1:
        return "Very Weak"
    elif score == 2:
        return "Weak"
    elif score == 3:
        return "Moderate"
    elif score == 4:
        return "Strong"
    else:
        return "Very Strong"


def main():
    print("=" * 40)
    print(" Password Strength Checker")
    print("=" * 40)

    password = input("\nEnter a password to check: ")

    score, feedback = check_password_strength(password)
    label = get_strength_label(score)

    print(f"\nStrength: {label}  ({score}/5)")

    if feedback:
        print("\nSuggestions to improve:")
        for tip in feedback:
            print(f"  - {tip}")
    else:
        print("\nGreat job! This password meets all the basic criteria.")


if __name__ == "__main__":
    main()
