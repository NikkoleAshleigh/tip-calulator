# I need to store the user input to get the value of the bill and
# how many ways the bill will be split


the_bill = float(input('What is the bill total? $'))

ways_to_split = int(input('How many people will be paying? '))


# I need to store the user input to get the value of the tip they
# wish to add to the bill (also added a little flare with the amount)

def the_tip():
    tip_amount = float(input('How much would you like to leave as a tip? '))
    if tip_amount <= 5:
        print('Ouch, that\'s lousy.')
    elif tip_amount <= 10:
        print('Were there any complaints with your service? ')
    elif tip_amount <= 20:
        print('I hope you enjoyed dining with us!')
    else:
        print('It\'s been an absolute pleasure serving you, and we hope to see you soon!' )

    tip = (the_bill * (0.01 * tip_amount))
    return tip
tip = the_tip()
 
# Once the program has run, I need to ask the user if they are going to be 
# adding a second bill and run through the calulations again. 
# The reason I place this here is because I dont want to change the entire 
# bill amount and not give the correct amount in the end

another_tip = input('Would you like to add another tip? ')
if another_tip == 'Yes':
    tip_new = tip + the_tip()
else:
    print('We hope to have your service again and have a blessed day! Thank you!')

# I need to calculate the 10% sales tax in with the bill 
# in order to get the final total

sales_tax = (the_bill * 0.10)
# print(sales_tax)
total_bill = ((the_bill + tip + sales_tax) / ways_to_split)

# I need to round the bill 
final_bill = round(total_bill, 2)

# I want to give different feedback based on if the bill was split or not
if ways_to_split >= 2:
    print(f'Each person should pay ${final_bill}')
else:
    print(f'Your total comes to: ${final_bill}')

# After all is said and done, I need to ask the user if they are going 
# to be adding a second bill and run through the calulations again The code 
# is on lines 31-35. Explanation for placement given there as well.





