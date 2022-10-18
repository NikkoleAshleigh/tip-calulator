# I need to store the user input to get the value of the bill and
# how many ways the bill will be split

# def  get_the_bill():
the_bill = float(input('What is the bill total? '))

ways_to_split = int(input('How many people will be paying? '))


# I need to store the user input to get the value of the tip they
# wish to add to the bill (also added a little flare with the amount)

# def the_tip():
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
# the_tip()

# def total_bill()

# I need to calculate the 10% sales tax in with the bill 
# in order to get the final total 

sales_tax = (the_bill * 0.10)
# print(sales_tax)
total_bill = (the_bill + tip + sales_tax / ways_to_split)

if ways_to_split >= 2:
    print(f'Each person should pay ${total_bill}')
else:
    print(f'Your total comes to: ${total_bill}')

# total_bill()

# After all is said and done, I nee to ask the user if they are going 
# to be adding a second bill and run through the calulations again

# def adding_second_tip()
another_tip = bool(input('Would you like to add another tip? '))
if another_tip == 'Yes':
    second_tip = float(input('How much would you like to leave as a tip? '))
    # I'm not able to get past asking if they want to add another tip 
    second_total = total_bill + second_tip
    print(second_total)
else:
    print(total_bill)
# adding_second_tip()

print('We hope to have your service again and have a blessed day! Thank you!')

