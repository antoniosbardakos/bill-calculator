print ("welcome to the tip calculator\n")
bill=float(input("what was the total bill? \n"))
tip= int(input("how much tip would you like to give?10, 12, 15?\n"))
people=int(input("how many people to split the bill?\n"))
tip_calculator=bill/100*tip
bill_with_tip=tip_calculator + bill
every_person=round(bill_with_tip / people,2)
print(f"Euch person should pay {every_person} $")

