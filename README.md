<!-- Make the README file look nice using markdown formatting. -->
<!-- Be sure to give it a title, and provide a brief summary of what your code does, and how to run it. -->

# Tip Calulator

Program in python3 that calculates a tip with the total bill. 
Once completed The user may enter in a second tip amount.


## How it works

In the terminal run: ``python project_tip_calculator.py``
- User enters the amount of the bill and how many ways the bill will be split
- User enters the value of the tip they wish to add to the amount of the bill
- The sales tax will then be configured to then print the total of either how much each person will spend if the bill was split or how much the total comes to if a single user were paying
- User then enters whether they wish to add another tip or not
    - If yes, the program will then re-calculate the bill with the new tip added
    - If not, the previous total amount will be printed again

## Cases to test my app:

### A meal for 1
Input:
- Food costs $15
- 1 person paying
- 20% tip
Expected output:
- ``Total bill: 19.50``
### A feast to remember
Input:
- Food costs $25000000
- 3 person paying
- 31% tip
Expected output:
- ``Total bill: $35,250,000.00``
- ``Each person should pay $11,750,000.00``
### No tip
Input:
- Food costs $78.99
- 6 person paying
- 0 tip
Expected output:
- ``Total bill: $86.89``
- ``Each person should pay $14.48``
### Sharing the bill among many
Input:
- Food costs $5000
- 876 person paying
- 12% tip
Expected output:
- ``Total bill: $6,100.00``
- ``Each person should pay $11,750,000.00``
