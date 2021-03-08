import pandas as pd


#2.2.1 Answer Customer Emails

inventory = pd.read_csv("inventory.csv")

istanbul = inventory.head(10)

product_request = istanbul['product_description']

seed_request = inventory[(inventory.location == 'Bursa') & (inventory.product_type == 'seeds')]


#2.2.2 Inventory

def quantity_checker(row):
    if row['quantity'] > 0 :
        return True
    if row['quantity'] == 0 :
        return False


inventory['in_stock'] = inventory.apply(lambda row: quantity_checker(row), axis = 1)

inventory['total_value'] = inventory.apply(lambda row: row['price'] * row['quantity'], axis =1 )

combine_lambda = lambda row : '{} - {} '. format (row. product_type, row. product_description)

inventory['full description'] = inventory.apply(combine_lambda, axis =1)








