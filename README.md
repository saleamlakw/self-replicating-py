⚠️ **DISCLAIMER**  
This repository is for **educational and research purposes only**.  
Running this code may modify `.py` files on your system. DO NOT run this on your personal or production machine.  
The author is **not responsible** for any damage caused by misuse.

---
![vv](https://github.com/user-attachments/assets/914ed9c2-4ccf-4595-8797-e7278a34a9a8)


## 📌 Description

This project demonstrates various techniques used in self-replicating Python scripts . The goal is to explore:

- File traversal and infection logic
- Signature checking and prevention of reinfection
- Hash-based tagging for identification
- Code obfuscation using `base64` and `zlib`
- Payload execution 

---

## 📂 Versions

### 🔹 `version_1.py`
- Basic infection engine
- Uses static markers
- Infects other Python files by prepending its own code

### 🔹 `version_2.py`
- Introduces **MD5 hashes** to identify infections
- Adds hash-based headers (`# begin-<hash>`)
- More resilient against duplicate infections

### 🔹 `version_3.py`
- Advanced obfuscation:
  - Compresses and encodes payload with `zlib` and `base64`
  - Executes via `exec(...)`
- Random comments added to confuse code reviewers

---

## 🧠 How It Works

Each version follows the same high-level approach:

1. Identify `.py` files in specified directories
2. Check for infection via signature or hash
3. If not infected:
   - Extract code from current file
   - Prepend/encode it into the target
4. Execute a custom payload

---

## ⚙️ Requirements

- Python 3.x
- Windows
---

## 🚨 WARNING

These scripts intentionally **modify files** on your system.  
To test safely:

- Use a virtual environment or sandbox
- Run on disposable directories
- Never test on production machines

---

