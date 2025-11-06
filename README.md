# 🏦 Bank Management System (Python + SQLite)

## 📘 Project Overview

The **Bank Management System** is a simple **minor project** developed in **Python** using **SQLite3** for database storage.
It allows users to perform basic banking operations such as creating accounts, depositing money, withdrawing money, and checking account balances — all through a command-line interface.

This project is ideal for **BCA or CS students** who want to learn database connectivity in Python.

---

## ✨ Features

* 🧾 Create a new bank account
* 💰 Deposit money
* 💸 Withdraw money
* 📊 Check account balance
* 🗂️ View all account details
* 🧩 Uses **SQLite database (bank.db)**
* ✅ User-friendly and easy to understand

---

## 🛠️ Technologies Used

| Component | Description                               |
| --------- | ----------------------------------------- |
| Language  | Python 3.x                                |
| Database  | SQLite3                                   |
| IDE       | Any Python IDE (VS Code / PyCharm / IDLE) |

---

## 📂 Folder Structure

```
BankManagementSystem/
│
├── main.py               # Main source code
├── bank.db               # SQLite database file
├── README.md             # Project description
└── requirements.txt      # (optional)
```

---

## ⚙️ Installation & Setup

1. **Clone this repository**

   ```bash
   git clone https://github.com/<your-username>/BankManagementSystem.git
   cd BankManagementSystem
   ```

2. **Install Python (if not installed)**
   [Download Python](https://www.python.org/downloads/)

3. **Run the project**

   ```bash
   python main.py
   ```

---

## 🧠 How It Works

* The program connects to `bank.db` automatically.
* All account data is stored in a single table named **`account`**.
* You can perform multiple operations through the text-based menu.

**Example Table Structure:**

```sql
CREATE TABLE IF NOT EXISTS account (
    acc_no INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    balance REAL DEFAULT 0.0
);
```

---

## 🧩 Sample Menu Interface

```
======== BANK MANAGEMENT SYSTEM ========
1. Create Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Exit
Enter your choice: _
```

---

## 👩‍💻 Project Created By

**Vaibhavi Singh**
BCA 5th Semester, CSJMU Kanpur
Guided by: **Dr. Pushpa Mamoria**

---

## 🚀 GitHub Upload Commands

```bash
git init
git add .
git commit -m "Initial commit - Bank Management System Project"
git branch -M main
git remote add origin https://github.com/<your-username>/BankManagementSystem.git
git push -u origin main
```

---

## 🏁 Conclusion

This project demonstrates how Python can be used for real-world applications such as **banking systems**.
It’s simple, educational, and a great base for further GUI or web-based upgrades.
