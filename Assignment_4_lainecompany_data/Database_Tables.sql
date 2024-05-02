-- Database: laine_customers

-- DROP DATABASE IF EXISTS laine_customers;

CREATE DATABASE laine_customers
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

# CREATE TABLES
-- Table: public.Demographics

-- DROP TABLE IF EXISTS public."Demographics";

CREATE TABLE IF NOT EXISTS public."Demographics"
(
    customerid integer NOT NULL,
    name character varying(100) COLLATE pg_catalog."default",
    username text COLLATE pg_catalog."default",
    age integer,
    gender character varying(50) COLLATE pg_catalog."default",
    address text COLLATE pg_catalog."default",
    phonenumber integer,
    email text COLLATE pg_catalog."default",
    CONSTRAINT "Demographics_pkey" PRIMARY KEY (customerid)
);

-- Table: public.accounts

-- DROP TABLE IF EXISTS public.accounts;

CREATE TABLE IF NOT EXISTS public.accounts
(
    "AccountID" integer NOT NULL,
    "CustomerID" integer,
    "CustomerType" text COLLATE pg_catalog."default",
    "Company" text COLLATE pg_catalog."default",
    CONSTRAINT "Account1D" PRIMARY KEY ("AccountID")
);

-- Table: public.preferences

-- DROP TABLE IF EXISTS public.preferences;

CREATE TABLE IF NOT EXISTS public.preferences
(
    "AccountID" integer,
    "ServicePreference" text COLLATE pg_catalog."default",
    "ContactPreference" text COLLATE pg_catalog."default",
    "ConnectPreference" character varying(50)[] COLLATE pg_catalog."default"
);

ALTER TABLE IF EXISTS public.accounts
    ADD CONSTRAINT "accounts_CustomerID_fkey" FOREIGN KEY ("CustomerID")
    REFERENCES public."Demographics" (customerid) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.preferences
    ADD CONSTRAINT "preferences_AccountID_fkey" FOREIGN KEY ("AccountID")
    REFERENCES public.accounts ("AccountID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;
	
# Show all columns in tables

-- 1. Retrieve all columns in the table Demographics
SELECT * FROM Public."Demographics" ;

-- Retrieve all columns in the table accounts
SELECT * FROM Public."accounts" ;

-- 3. Retrieve all columns in the table preferences
SELECT * FROM Public."preferences" ;

END;