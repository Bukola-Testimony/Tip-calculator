#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇


print("Welcome to the tip calculator!")
bill =float(input("What was the total bill?: $"))
Tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
People = float(input("How many people to split the bill? "))

Tip_calculate =  Tip / 100 * bill + bill
Result = (Tip_calculate / People)
# To round the result into 2 decial places, instead of using "round", use the below:
Payment = "{:.2f}".format (Result)

print(f"Each person should pay: ${Payment}")



# result = (bill / Split) * final_tip

# final_tip = (Tip + 1) + Total_bill



# print(round(final_tip ,2))




# Payment = round(result,2)

