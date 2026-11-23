import random
import string

MIN_LENGTH = 8


def get_length():
    """Ask for a password length and keep asking until it is valid."""
    while True:
        value = input("Enter password length (minimum 8): ").strip()
        if not value.isdigit():
            print("Please enter a valid whole number.")
            continue
        length = int(value)
        if length < MIN_LENGTH:
            print(f"Length must be at least {MIN_LENGTH} characters.")
            continue
        return length


def ask_yes_no(question):
    """Ask a yes/no question and return True or False."""
    while True:
        answer = input(question + " (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please type y or n.")


def get_character_sets():
    """Let the user choose character types (at least 2 required)."""
    while True:
        print("\nChoose character types (select at least 2):")
        selected = []
        if ask_yes_no("Include uppercase letters?"):
            selected.append(string.ascii_uppercase)
        if ask_yes_no("Include lowercase letters?"):
            selected.append(string.ascii_lowercase)
        if ask_yes_no("Include numbers?"):
            selected.append(string.digits)
        if ask_yes_no("Include symbols?"):
            selected.append(string.punctuation)

        if len(selected) >= 2:
            return selected
        print("You must select at least 2 character types. Try again.")


def generate_password(length, character_sets):
    """Build a password containing at least one char from each chosen type."""
    password = [random.choice(chars) for chars in character_sets]
    all_chars = "".join(character_sets)
    remaining = length - len(password)
    password += [random.choice(all_chars) for _ in range(remaining)]
    random.shuffle(password)
    return "".join(password)


def main():
    print("=== Random Password Generator ===")
    while True:
        length = get_length()
        character_sets = get_character_sets()
        password = generate_password(length, character_sets)
        print(f"\nYour password: {password}\n")

        if not ask_yes_no("Generate another password?"):
            print("Goodbye! Stay safe online.")
            break
        print()


if __name__ == "__main__":
    main()
