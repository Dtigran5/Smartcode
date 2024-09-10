def is_good_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True

if __name__ == "__main__":
    user_password = input("Enter a password to check if it is good: ")
    if is_good_password(user_password):
        print("The password is good.")
    else:
        print("The password is not good.")
