def tip_calculator():

    the_bill = float(input('What is the bill total? '))

    ways_to_split = int(input('How many people will be paying? '))

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
    
    sales_tax = (the_bill * 0.10)
    # print(sales_tax)
    total_bill = (the_bill + tip + sales_tax / ways_to_split)

    if ways_to_split >= 2:
        print(f'Each person should pay ${total_bill}')
    else:
        print(f'Your total comes to: ${total_bill}')

tip_calculator()



