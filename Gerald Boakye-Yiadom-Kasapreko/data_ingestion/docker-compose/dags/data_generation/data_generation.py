from faker import Faker
import csv

fake = Faker()

# Define the fields for the data
fields = ['Customer Name', 'Address', 'Transaction Amount', 'Transaction Date', 'Customer Preference', 'Product', 'Product Quantity']

# Define products and their corresponding prices
products = {
    'water': 1.0,    # Fake price for water
    'juice': 2.0,    # Fake price for juice
    'wine': 3.0,     # Fake price for wine
    'bitters': 4.0,  # Fake price for bitters
}

# Generate 100k records
num_records = 100000

# Generate and save data to CSV file
with open('kasapreko_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()

    for _ in range(num_records):
        name = fake.name()
        address = fake.address()
        customer_preference = fake.random_element(elements=('App', 'Website'))  # Random customer preference
        product = fake.random_element(elements=list(products.keys()))  # Random product

        # Determine transaction amount and product quantity based on product
        price = products[product]  # Get price for selected product
        product_quantity = fake.random_int(min=1, max=10)  # Random product quantity
        transaction_amount = price * product_quantity  # Calculate transaction amount

        transaction_date = fake.date_between(start_date='-1y', end_date='today')  # Random transaction date within the 

        writer.writerow({
        'Customer Name': name,
        'Address': address,
        'Transaction Amount': transaction_amount,
        'Transaction Date': transaction_date,
        'Customer Preference': customer_preference,
        'Product': product,
        'Product Quantity': product_quantity
        })
        