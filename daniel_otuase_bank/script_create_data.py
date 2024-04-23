import pandas as pd 
import numpy as np
from faker import Faker

data_faker = Faker()

customer_data = []

def generate_user_data(numOfCustomers):
    for _ in range(numOfCustomers):
        data_set = {
            'customer_id': data_faker.bothify(text="Otua???", letters="123657098990"),
            'first_name': data_faker.first_name(),
            'last_name': data_faker.last_name(),
            'email': data_faker.email(),
            'transaction_activity': data_faker.random_element(elements=("withdrawal", "deposit")),
            'customer_preference': data_faker.random_element(elements=("app", "website"))
            } 
        customer_data.append(data_set)
    return customer_data
    
num = 10000

data_frame = pd.DataFrame(generate_user_data(num))
data_frame.to_csv('data_frame.csv', index=False)
print(data_frame)