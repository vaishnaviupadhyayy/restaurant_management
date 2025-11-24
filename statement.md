Project Statement: Iris Restaurant Billing System

Problem Statement

The primary problem this project addresses is the inefficiency and high probability of error associated with manual billing processes in restaurants. Relying on handwritten notes and manual calculation of totals, line items, and taxes (8%) leads to customer delays, financial discrepancies, and a poor service experience. The goal is to develop a reliable, accurate, and simple Python application to automate these financial calculations and instantly generate an itemized bill.

Scope of the Project

The project is scoped as a Proof-of-Concept console application.

Inclusions:

Displaying a fixed, pre-defined menu (menuitems dictionary).

Handling single-session order input from the user/cashier.

Performing arithmetic calculations (multiplication, addition) for subtotals and the fixed 8% tax rate.

Providing basic input validation for menu codes and quantities.

Generating a final, formatted console output receipt.

Exclusions (Limitations):

No database integration (data is lost upon program exit).

No support for multiple concurrent tables or orders.

No discount or coupon functionality.

No graphical user interface (GUI).

Target Users

Restaurant Cashiers/Servers: Primary users who need a quick, accurate tool to input orders and generate receipts for dining customers.

Small Business Owners: Owners of small eateries who require a minimal, low-cost solution for managing daily transactions without complex software.

Students/Developers: The application serves as a clean example of procedural programming, dictionary manipulation, and input validation in Python.

High-Level Features:

The system is built upon three core feature groups, represented by the main functions:

Presentation (display_menu): Displays the current menu in a clear, formatted structure for the cashier.

Transaction Processing (take_order): Handles the loop of order input, item lookup, quantity validation, and compilation of the final order list.

Financial Computation (generate_bill): Executes all necessary arithmetic: summing line totals, calculating sales tax (8%), and determining the final amount due.
