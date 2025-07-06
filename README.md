# 🔐 Encodex – Custom Cipher Encoder/Decoder

Encodex is a simple yet powerful Python-based encoding/decoding tool that converts your text into a custom cipher using randomly generated keys. Each user session is based on a unique **seed**, making your encoding process reproducible and personalized.

---

## 🚀 Features
- Generate custom key mappings based on random seed
- Encode and decode any text using your personalized key
- Save keys in JSON format for future use
- Login system using the seed as your credential
- Modular and beginner-friendly codebase

---

## 🛠️ How It Works

- **SignIn**: Generates a new key mapping and seed. Keys are stored in a folder named after the seed.
- **LogIn**: Reuse an existing seed to access your personal key and reverse-key.
- **Encode**: Converts your string into an encrypted format using your key.
- **Decode**: Converts an encoded string back using the reverse key.

---

## 📁 Project Structure

encodex/
├── main.py          # Entry point for user interaction
├── key.py           # Generates and stores keys
├── auth.py          # Handles login based on seed
├── encodex.py       # Encoding and decoding logic
├── README.md        # This file!
└── <seed folders>/  # Contains key.json and reverse\_key.json

---

## 🧪 Usage

### 1. SignIn (Generate New Key)

> python main.py
> LogIn/SignIn: signin
> Generated seed: 87.543212

### 2. LogIn (Use Existing Seed)

> python main.py
> LogIn/SignIn: login
> Enter the seed: 87.543212
> Encode/Decode: encode
> Enter the string: Hello123
> Encoded: X8s91Fa92Kk...

---

## ⚠️ Notes
- The seed must be saved if you want to decode your messages later.
- Each character is encoded using a 5-character random string.
- Spaces and digits are supported!

---

## ✨ Future Ideas
- Save encoded/decoded logs
- Add GUI using Tkinter or PyQt
- Web-based interface with Flask
- Password-based key generation

---

## 📄 License
This project is for educational and personal use. Feel free to fork, expand, or contribute!

---

Made by Priyansh Kumar
