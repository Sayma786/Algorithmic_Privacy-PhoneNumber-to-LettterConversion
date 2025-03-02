# Algorithmic Privacy in Phone Number to Letter Conversion

## Introduction
This project focuses on converting phone numbers into letter combinations using cryptographic methods. The implementation includes two different approaches for generating letter combinations: 
1. **Backtracking Algorithm**
2. **Brute-force Method**

Additionally, the project integrates RSA encryption to secure the generated letter combinations and verify data integrity.

## Features
- Converts numeric phone numbers into possible letter combinations.
- Implements *Backtracking* and *Brute-force* approaches for efficiency comparison.
- Uses *RSA encryption and decryption* to ensure privacy.
- Verifies data integrity after decryption.

## Algorithms Used
### **1. Backtracking Algorithm (`Backtracking.py`)**
- **Time Complexity:** O(mⁿ), where `m` is the number of letters per digit.
- **Space Complexity:** O(n).
- Uses recursion to generate all possible letter combinations for a given number.

### **2. Brute-force Method (`Bruteforce.py`)**
- **Time Complexity:** O(4ⁿ).
- **Space Complexity:** O(3ⁿ).
- Uses an iterative approach to generate all possible letter combinations.

### **3. RSA Encryption and Verification (`verify.py`)**
- Uses **RSA encryption** to secure the generated letter combinations.
- Encrypts letter combinations in segments.
- Decrypts and verifies message integrity.

## How It Works
1. The user inputs a numeric string (phone number).
2. The program generates all possible letter combinations.
3. The generated text is encrypted using RSA.
4. The encrypted text is decrypted to check for errors or corruption.
5. The program verifies that the decrypted message matches the original.

## Installation
### Prerequisites
- Python 3.x
- Required libraries (install via `requirements.txt`)

### Install Dependencies
```sh
pip install -r requirements.txt
