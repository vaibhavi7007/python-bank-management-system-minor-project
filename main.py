import sqlite3

# Database connection
con = sqlite3.connect("bank.db")
cur = con.cursor()

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS account(
    acc_no INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    balance REAL NOT NULL
)
""")
con.commit()


# Create new account
def create_account():
    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Deposit: "))
    cur.execute("INSERT INTO account(name, balance) VALUES(?, ?)", (name, balance))
    con.commit()
    print("✅ Account Created Successfully!")


# Deposit amount
def deposit():
    acc = int(input("Enter Account Number: "))
    amt = float(input("Enter Amount to Deposit: "))
    cur.execute("UPDATE account SET balance = balance + ? WHERE acc_no = ?", (amt, acc))
    con.commit()
    print("💰 Amount Deposited Successfully!")


# Withdraw amount
def withdraw():
    acc = int(input("Enter Account Number: "))
    amt = float(input("Enter Amount to Withdraw: "))
    cur.execute("SELECT balance FROM account WHERE acc_no = ?", (acc,))
    bal = cur.fetchone()
    if bal and bal[0] >= amt:
        cur.execute("UPDATE account SET balance = balance - ? WHERE acc_no = ?", (amt, acc))
        con.commit()
        print("💸 Amount Withdrawn Successfully!")
    else:
        print("❌ Insufficient Balance or Invalid Account!")


# Check balance
def check_balance():
    acc = int(input("Enter Account Number: "))
    cur.execute("SELECT * FROM account WHERE acc_no = ?", (acc,))
    data = cur.fetchone()
    if data:
        print(f"\nAccount No: {data[0]}\nName: {data[1]}\nBalance: ₹{data[2]}")
    else:
        print("❌ Account not found!")


# Main menu
while True:
    print("\n====== BANK MANAGEMENT SYSTEM ======")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    ch = input("Enter your choice (1-5): ")

    if ch == '1':
        create_account()
    elif ch == '2':
        deposit()
    elif ch == '3':
        withdraw()
    elif ch == '4':
        check_balance()
    elif ch == '5':
        print("thankyou for using the system")
        break
    else:
        print("⚠️ Invalid choice! Try again.")
