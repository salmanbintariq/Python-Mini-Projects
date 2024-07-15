print("---RENT CALCULATOR---")

unit_price = 34 #Electricity unit price

# Taking inputs from user
total_rent = int(input("Enter the total rent of the room: "))
food_ordered = int(input("Enter the food you ordered in one month: "))
total_unit = int(input("Enter the unit of electricity consumed in one month: "))
person_living = int(input("Enter the number of person living in room: "))

total_bill_ofElectricity = total_unit * unit_price

per_head = (total_rent + food_ordered + total_bill_ofElectricity) / person_living

print(f"The rent per head is {per_head}Rs.")
                        