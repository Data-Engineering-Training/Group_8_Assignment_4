from faker import Faker
import pandas as pd
import random

# Create instance for faker
fake = Faker()

def generate_customer_id():
    # Generate a unique customer ID specific to the bank "Amansie"
    bank_code = "AMS"
    customer_number = random.randint(100000, 999999)
    return f"{bank_code}-{customer_number}"

def create_customers(num_customers):
    customer_list = []
    # Create customers dictionary
    for _ in range(num_customers):
        customer = {
            'customer_id': generate_customer_id(),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'address': fake.address(),
            'transaction_activity': fake.random_element(elements=("withdrawal", "deposit")),
            'customer_preference': fake.random_element(elements=("app", "website")),
            'email': fake.email()
        }
        customer_list.append(customer)
    
    return customer_list

# Number of customers
num_customers = 100000

# Generate customer data
customer_list = create_customers(num_customers)

# Create DataFrame
df = pd.DataFrame(customer_list)

# Save DataFrame to CSV
df.to_csv('customer_data.csv', index=False)

print("Data saved to customer_data.csv")
