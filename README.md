# Batch Processing with HDFS and Apache PySpark

The project aims to create an automated data ingestion and analysis pipeline that fetches data from an open-source API, stores it in HDFS, and processes it with PySpark for further analysis and insights.

## Objectives

**1. Choose an Open Source API:**
- Find an open-source API where you can regularly fetch data.

**2. Set Up Batch Data Ingestion:**
- Write a script to fetch data from the chosen API at regular intervals, where data is collected in batches at scheduled times.

**3. Save Data Using HDFS (Hadoop Distributed File System):**
- Once fetched, store it using HDFS.

**4. Process Data with Apache PySpark (ELT with Batch Processing):**
- Perform ELT (Extract, Load, Transform) - and extract data from HDFS, load it into PySpark, and then perform transformation operations (like aggregating, filtering, joining, etc.).

## Project Evolution

**1. Shopify API Setup (Completed)**

- We **created** a Shopify development storefront to generate fake data. 
- A custom app **was created** to provide authorization for accessing the store's data, with permissions set accordingly.
- We **received** an Admin API access token, which is required for authenticated requests to the Shopify API.
- This enabled us to **use** an access token for authentication during API requests, allowing us to **fetch** the fake data.

**2. Initial Python Script  (In Progress)**

- The initial python script accomplishes several tasks:
	- It **sets up** access to the Shopify store's data using an access token and store name.
	- It **fetches** information about products from the store.
	- It **gets** the current date and time and **uses** it to create a unique timestamp.
	- It **constructs** a filename that includes the timestamp. 
	- It **saves** the fetched product data into a JSON file, which **is stored** in the 'data' folder in the project's directory.

 ## Project files

 ```dds_v1.py```: Automates data retrieval from an Shopify API, saving the fetched data in JSON format.
