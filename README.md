🔐 Auto Password Generator
A Python script that generates strong, randomized passwords with customizable length and secure character distribution.

🌟 Features
✅ Secure & Randomized – Uses random.shuffle() for unpredictability.
✅ Custom Length – Minimum 8 characters (configurable).
✅ Mixed Character Sets – Includes:

Lowercase (a-z)

Uppercase (A-Z)

Digits (0-9)

Symbols (!@#$%^&*, etc.)
✅ Smart Distribution – 30% letters, 20% digits/symbols for balance.
✅ Input Validation – Ensures only numbers are entered.

🛠️ Installation
Clone the repo:

sh
Copy
git clone https://github.com/HassanAmohamed/Secure-Password-Generator.git
Navigate to the directory:

sh
Copy
cd Auto-Generate-Password
Run the script:

sh
Copy
python password_generator.py
🚀 Usage
Enter desired password length (e.g., 12):

Copy
How many characters do you need for the password? 12
Get your generated password:

Copy
Generated Password: xK3@jB9!qL2%
Password generation complete! ✅
📝 Code Overview
python
Copy
import string
import random

# 1. Define character sets (lowercase, uppercase, digits, symbols)
# 2. Validate user input (must be ≥8 and numeric)
# 3. Shuffle characters for randomness
# 4. Generate password with 30% letters, 20% digits/symbols
# 5. Output final shuffled password
🤝 Contributing
PRs welcome! For major changes, open an issue first.

📜 License
MIT © [Your Name]

🔎 Example Output
Length	Example Password
8	pA7@kL2!
12	xK3@jB9!qL2%
16	mQ5#tY8&kP1$rN9*
💡 Pro Tip:
For extra security, combine this with a password manager like Bitwarden or KeePass.