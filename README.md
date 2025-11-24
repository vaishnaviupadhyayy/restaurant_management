Iris Restaurant Billing System

Overview:

Welcome to the Iris Restaurant Billing System! This isn't just code; it's a quick, reliable digital cashier built entirely with Python. It was designed to solve a huge real-world headache: manual billing errors and delays. This friendly, command-line application handles the entire transaction—from showing the menu to taking complex, multi-item orders, applying the 8% sales tax flawlessly, and printing a professional receipt. Say goodbye to pen and paper!

Features

Clear Menu Display: No confusing numbers here! We show all 23 delicious menu items with their unique codes and prices in a neatly organized, easy-to-read list.

Effortless Ordering: The system is patient! You can keep entering item codes and quantities until you're absolutely done, then just type 'DONE' to finalize the transaction.

Crash-Proof Input: We built in strong validation using Python's try-except blocks. If you accidentally type a letter instead of a quantity, the program won't crash—it just asks nicely for the correct input.

Instant Subtotaling: Watch the bill build itself! The system automatically calculates the cost for each line item and keeps a running subtotal.

Flawless Tax: Forget manual tax calculations. The system automatically applies the required 8% sales tax to ensure the final amount is always perfect.

Professional Receipt: The final output looks great—it's a clean, aligned, and professional receipt ready to present to the customer.

Technologies/Tools Used

Python 3: The whole application is powered by clean, readable Python code.

Core Python Tools: We rely on Python's native data structures: Dictionaries for fast menu lookups (like an instant pricing database) and Lists of Dictionaries to neatly hold the customer's final order.

Just the Basics: It uses only the standard time library (just for a nice, brief pause at the end!) and runs right in your terminal. No fancy software needed!

Steps to Install & Run the Project

Prerequisites: Make sure you have Python 3 installed on your computer.

Save the Code: Save the provided Python code into a file named billing_system.py.

Run from Terminal: Open your terminal or command prompt, navigate to the directory where you saved the file, and execute the script:

python billing_system.py


Instructions for Testing

We built this to be robust! Follow these simple steps to ensure everything works, especially the crash-proofing features:

1. Happy Path Test (Successful Transaction)

Enter code 1 (Paneer Lababdar).

Enter quantity 2.

Enter code 20 (Cheesecake Slice).

Enter quantity 1.

Enter DONE.

Expected Result: A complete bill showing the correct subtotal, 8% tax, and grand total.

2. Input Validation Test (Quantity)

Enter a valid code, e.g., 3.

When prompted for quantity, try entering A (non-numeric).

Expected Result: The system should print "Invalid input. Please enter a number for the quantity." and prompt again—it won't crash!

Enter 0 (non-positive).

Expected Result: The system should print "Quantity must be a positive number." and prompt again.

3. Invalid Code Test (Menu Code)

Enter a code that doesn't exist, e.g., 99.

Expected Result: The system should print "Invalid menu code. Please try again or enter 'DONE'."

Screenshots (Conceptual)
