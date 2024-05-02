#!/usr/bin/env python
# coding: utf-8

# In[98]:


# Import Required Libraries


# In[47]:


import os


# In[48]:


import sys


# In[49]:


import csv


# In[50]:


import psycopg2


# In[51]:


from sqlalchemy import create_engine, text


# In[52]:


import pandas as pd


# In[53]:


import numpy as np


# In[54]:


import random


# In[55]:


from random import randint, uniform, choice


# In[56]:


import string


# In[57]:


from datetime import datetime, timedelta


# In[58]:


import mysql.connector


# In[59]:


from faker import Faker


# In[112]:


# Generate records for L'aine company using Faker library


# In[60]:


fake = Faker()


# In[61]:


fake_gh = Faker('tw_GH')


# In[62]:


def generate_company_records(company_name, num_records):
    """
    Generates customer records for a l'aine company using Faker library.

    Parameters:
        company_name (str): Name of the company.
        num_records (int): Number of records to generate.

    Returns:
        list: List of tuples containing customer records.
    """


# In[63]:


def generate_random_numbers():
    random_numbers = ""
    for _ in range(3):
        random_numbers += str(random.randint(0, 9))  
        # Concatenate random numbers as strings
    return random_numbers


# In[117]:


# Generate customers demographic data


# In[64]:


customers_data = []
for customer_id in range(1, 10001):
    random_numbers = generate_random_numbers()
    name = fake_gh.name()
    username = f"{name.lower()}.{random_numbers}"
    age = fake_gh.random_int(min=1, max=60)
    gender = random.choice(['male', 'female'])
    address = fake_gh.address()
    email_domain = random.choice(['gmail.com', 'yahoo.com', 'uk.org', 'outlook.com'])
     # random numbers
    phone_number = fake_gh.phone_number()
    email = f"{name.lower()}.{random_numbers}@{email_domain}"
    customers = {
    'CustomerID': customer_id,
    'Name': name,
    'Username': username,
    'Age': age,
    'Gender': gender,
    'Address': address,
    'PhoneNumber': phone_number,
    'Email': email,
    }
    customers_data.append(customers)


# In[65]:


def save_to_csv(self, company_name, company_records):
        """
        Saves customer data for l'aine company into a CSV file.
        Parameters:
            company_name (str): Name of the company.
            company_records (list): List of tuples containing customer records for the company.
        """


# In[120]:


# def file path of csv file 'customers data'


# In[69]:


os.chdir(r"C:\Users\PC\Desktop\Assignment_4_lainecompany_data\CSV file")


# In[70]:


filepath = r"C:\Users\PC\Desktop\Assignment_4_lainecompany_data\CSV file/customers_data.csv"


# In[71]:


with open(filepath, 'w', newline='', encoding='UTF-8') as csvfile:
    fieldnames = ['CustomerID', 'Name', 'Username', 'Age', 'Gender', 'Address', 'PhoneNumber', 'Email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(customers_data)


# In[124]:


# display content of csv file


# In[72]:


data1 = csv.reader(open (filepath))
for header in data1:
    print(header)


# In[126]:


# generate account data of all customers


# In[24]:


customer_account = []
for account_id in range(1, 10001):
    customer_id = random.choice([x['CustomerID'] for x in customers_data])
    customer_type = random.choice(['public_sector_worker', 'private_sector_worker'])
    company = fake_gh.company()
    accounts = {
    'AccountID': account_id,
    'CustomerID': customer_id,
    'CustomerType': customer_type,
    'Company': company
    }
    customer_account.append(accounts)


# In[128]:


# Define file path and save customer account as csv file


# In[73]:


filepath2 = r"C:\Users\PC\Desktop\Assignment_4_lainecompany_data\CSV file/customer_account.csv"


# In[74]:


with open(filepath2, 'w', newline='', encoding='UTF-8') as csvfile:
    fieldnames = ['AccountID', 'CustomerID', 'CustomerType', 'Company']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(customer_account)


# In[131]:


# display content of csv file


# In[75]:


data2 = csv.reader(open (filepath2))
for header in data2:
    print(header)


# In[133]:


# Generate customer prefererence data


# In[27]:


customer_preference = []
for _ in range(1, 100001):
    account_id = random.choice([x['AccountID'] for x in customer_account])
    service_preference = random.choice(['management and organizational skills training', 'technical skills training', 'human resources services', 'financial skills training', 'partnership and networking services', 'leadership and team building'])
    contact_preference = random.choice(['phone call', 'email', 'SMS'])
    connect_preference = random.choice(['facebook', 'LinkedIn', 'Instagram', 'WhatsApp', 'Website'])
    preferences = {
    'AccountID': account_id,
    'ServicePreference': service_preference,
    'ContactPreference': contact_preference,
    'ConnectPreference': connect_preference
    }
    customer_preference.append(preferences)
    


# In[135]:


# Define file path and save customer preferences as csv file


# In[76]:


filepath3 = r"C:\Users\PC\Desktop\Assignment_4_lainecompany_data\CSV file/customer_preference.csv"


# In[77]:


with open(filepath3, 'w', newline='', encoding='UTF-8') as csvfile:
    fieldnames = ['AccountID', 'ServicePreference', 'ContactPreference', 'ConnectPreference']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(customer_preference)


# In[138]:


# display content of csv file


# In[78]:


data3 = csv.reader(open (filepath3))
for header in data3:
    print(header)


# In[140]:


# Create a connection to postgreSQL for ingesting the data generated


# In[79]:


def create_connection(self, cursor):
    """
# Create a connection to postgreSQL database
    
    Connection Parameters
    dbname (str): Name of the database.
    table_name (str): Name of table in database.
    user (str): Username for database authentication.
    password (str): Password for database authentication.
    host (str): Hostname where the database is hosted.
    """
    db_params = {
    'host': 'localhost',
    'database': 'postgres',
    'table_name': 'table_name',
    'user': 'postgres',
    'password': 'admin'
    }

    return  psycopg2.connect(
            host=db_params['host'],
            database=db_params['database'],
            table_name=df_params['table_name'],
            user=db_params['user'],
            password=db_params['password']
        )


# In[142]:


# Create a database named laine customers


# In[80]:


def create_database(self, cursor):
    """
    Creates a new database with a cursor object

    Parameters
    cursor (psycopg2.extensions.cursor): Database cursor object.
    database=db_params['database']
    """
    cursor.execute("CREATE DATABASE laine_customers")


# In[144]:


# Create a table in the new database


# In[145]:


def create_table(self, cursor, table_name):
        """
        Creates a table for laine services limited in the database if not exists.

        Parameters:
            cursor (psycopg2.extensions.cursor): Database cursor object.
            table_name (str): Name of table
        """
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS (
                CustomerID VARCHAR(10) PRIMARY KEY,
                Name VARCHAR(100),
                Age INTEGER,
                Gender CHAR(10),
                Address VARCHAR(50),
                PhoneNumber INTEGER,
                Email VARCHAR(100),
                )
            ''')


# In[146]:


#connect to new database


# In[40]:


def get_db_engine(database, user, password, port, host):
    """
    connects to laine_customers database

    Parameters
    db_params['host'] = 'localhost',
    db_params['database'] = 'laine_customers',
    db_params['user'] = 'postgres',
    db_params['port'] = '5432',
    db_params['password'] = 'pass2030'
    """
    connection_string = "postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}"
    engine = create_engine(conection_string, echo=True)
    return engine


# In[148]:


# load customers data into postgreSQL database


# In[41]:


def ingest_customer_data(self, cursor, table_name, customers):
    """
    ingests data into the specific table

    Parameters
     cursor (psycopg2.extensions.cursor): Database cursor object.
     table_name (str): Name of table in database 'laine_customers'
     customers (list): List of tuples containing customers records for laine company
    """
    for table_name in customers:
        data1.to_sql(table_name, engine, if_exists='replace', index=False, chunksize=1000)


# In[150]:


# load customer account data into postgres database


# In[151]:


def ingest_customer_account(self, cursor, table_name, accounts):
    """
    ingests data into the specific table

    Parameters
     cursor (psycopg2.extensions.cursor): Database cursor object.
     table_name (str): Name of table in database 'laine_customers'
     accounts (list): List of tuples containing records of customer account for laine company
    """
    for table_name in accounts:
        data2.to_sql(table_name, engine, if_exists='replace', index=False, chunksize=1000)


# In[152]:


# load customer preference data into postgres database


# In[153]:


def ingest_customer_preference(self, cursor, table_name, preferences):
    """
    ingests data into the specific table

    Parameters
     cursor (psycopg2.extensions.cursor): Database cursor object.
     table_name (str): Name of table in database 'laine_customers'
     preferences (list): List of tuples containing records of customer preferences for laine company
    """
    for table_name in preferences:
        data3.to_sql(table_name, engine, if_exists='replace', index=False, chunksize=1000)


# In[154]:


# run data pipeline


# In[155]:


def run_pipeline(self, table_name, customers):
       """
       Runs the data pipeline to create table and load data

       Parameters:
           customers (list): List of tuples containing customers records for laine company.
            table_name (str): Name of table.
            database=db_params['database']
       """
       conn = psycopg2.connect(
           host=db_params['host'],
           database=db_params['database'],
           user=db_params['user'],
           port=db_params['port'],
           password=db_params['password']
       )
       cur = conn.cursor()
       conn.set_session(autocommit=True)
       cur.execute("CREATE DATABASE laine_customers")
       conn.commit()
       cur.close()
       conn.close()


# In[ ]:




