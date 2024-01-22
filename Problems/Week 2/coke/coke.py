amount_due = 50
amount_owed = -50
accepted_change = [25, 10, 5]


while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    amount_insert = int(input("Insert coin:"))
    if amount_insert in accepted_change:
        amount_due -= amount_insert
        amount_owed += amount_insert

print(f"Change Owed: {amount_owed}")
