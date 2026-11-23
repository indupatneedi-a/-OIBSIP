# 🔐 Random Password Generator

**OIBSIP / Python-Task3-PasswordGenerator**

A command-line Python tool that generates strong, random passwords based on criteria chosen by the user. Built as part of the **Oasis Infobyte Student Internship Program (OIBSIP)**, Python Programming Track, **Task 3 (Beginner Tier)**.

---

## 📌 Objective

Weak and reused passwords are one of the most common causes of hacked accounts. The goal of this project is to build a simple tool that lets a user generate a random password of their chosen length and character types, so they don't have to invent one themselves.

---

## ✨ Features

- 🔢 **Custom length:** the user chooses the password length (minimum **8 characters** enforced)
- 🔤 **Choice of character types:** uppercase letters, lowercase letters, numbers and symbols (at least **2 types** must be selected)
- ✅ **Guaranteed variety:** every selected character type appears at least once in the generated password
- 🛡️ **Input validation:** rejects non-numeric input, lengths below 8, and fewer than 2 character types, with a helpful message each time
- 🔁 **Generate again:** create as many passwords as you like without restarting the program

---

## 🛠️ Tech Stack

| Item | Details |
|------|---------|
| Language | Python 3 |
| Modules | `random`, `string` (both built into Python) |
| External libraries | None needed |
| Interface | Command line |

---

## 📋 Requirements

- Python 3.6 or higher installed on your computer
- No extra packages to install, so there is no `requirements.txt` for this task

To check your Python version, run:

```
python --version
```

---

## 🚀 Installation and How to Run

1. **Clone the repository** (or download the file directly):

   ```
   git clone https://github.com/indupatneedi-a/OIBSIP.git
   ```

2. **Go to the task folder:**

   ```
   cd OIBSIP/Python-Task3-PasswordGenerator
   ```

3. **Run the program:**

   ```
   python password_generator.py
   ```

4. **Follow the on-screen prompts** to enter the length and pick character types.

---

## 🖥️ How to Use

1. Enter the password length (8 or more).
2. Answer `y` or `n` for each character type:
   - Uppercase letters (A-Z)
   - Lowercase letters (a-z)
   - Numbers (0-9)
   - Symbols (!, @, #, $, etc.)
3. The program prints your password.
4. Choose `y` to generate another one, or `n` to exit.

### Sample Session

```
=== Random Password Generator ===
Enter password length (minimum 8): 12

Choose character types (select at least 2):
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): n

Your password: k7Tq2LmX9bRe

Generate another password? (y/n): n
Goodbye! Stay safe online.
```

*(The password above is only an example. Every run produces a different one.)*

---

## ⚙️ How It Works

The program is split into small functions, each with one job:

| Function | Purpose |
|----------|---------|
| `get_length()` | Asks for the length and keeps asking until the input is a whole number of at least 8 |
| `ask_yes_no()` | Asks a yes/no question and accepts only `y`, `yes`, `n` or `no` |
| `get_character_sets()` | Collects the character types chosen by the user and makes sure at least 2 are selected |
| `generate_password()` | Builds the password |
| `main()` | Runs the program loop and lets the user generate more passwords |

**Password generation logic:**

1. Pick one random character from *each* selected type, so every type is guaranteed to appear.
2. Fill the remaining length with random characters from the combined pool of all selected types.
3. Shuffle everything so the guaranteed characters are not always at the start.
4. Join the characters into the final password.

---

## ✅ Input Validation

| Situation | What the program does |
|-----------|-----------------------|
| Length is not a number (e.g. `abc`, `-5`, `8.5`) | Shows "Please enter a valid whole number." and asks again |
| Length is below 8 | Shows "Length must be at least 8 characters." and asks again |
| Fewer than 2 character types chosen | Shows an error and asks the user to choose again |
| Invalid yes/no answer | Shows "Please type y or n." and asks again |

---

## 📁 Project Structure

```
OIBSIP/
└── Python-Task3-PasswordGenerator/
    ├── password_generator.py   # Main program
    ├── README.md               # Project documentation
    └── screenshots/            # Screenshots of the program running
```

---

## 📸 Screenshots
<img width="1920" height="752" alt="1000095990" src="https://github.com/user-attachments/assets/91f5d10f-813c-4683-8e89-55a9cf7aad98" />
<img width="1920" height="752" alt="1000095991" src="https://github.com/user-attachments/assets/4b62f598-55eb-4e5f-b880-5c34e56445a8" />
<img width="1920" height="752" alt="1000095992" src="https://github.com/user-attachments/assets/860f08f6-e061-40f5-b22c-1ab61eb24429" />


---

## 🔒 Security Note

This beginner version uses Python's `random` module, which is fine for learning and demonstration but is **not designed for cryptographic security**. The Advanced tier uses the `secrets` module for secure password generation. Generated passwords are only printed on screen and are **never saved to any file**.

---

## 🔮 Future Improvements

- Upgrade to the Advanced tier with a GUI (`tkinter`)
- Use the `secrets` module for cryptographically secure generation
- Add a password strength indicator (Weak / Medium / Strong)
- Add a "Copy to Clipboard" button using `pyperclip`
- Add an option to exclude ambiguous characters (0, O, l, 1)
- Show the last 5 generated passwords during the session

---

## 👩‍💻 Author

**Indu Seetala Patneedi**
Oasis Infobyte SIP (OIBSIP) | Python Programming Track

#oasisinfobyte
