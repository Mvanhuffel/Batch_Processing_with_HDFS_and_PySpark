# Batch Processing with HDFS and Apache PySpark

The project aims to create an automated data ingestion and analysis pipeline that fetches data from a third-party API, stores it in HDFS, and processes it with PySpark for further analysis and insights.

## Objectives

- **Choose a Third-Party API**: Find and select a third-party API for data ingestion.
- **Set Up Batch Data Ingestion**: Develop a script for regular data fetching from the chosen API in scheduled batches.
- **Save Data Using HDFS**: Store the collected data using HDFS (Hadoop Distributed File System).
- **Process Data with Apache PySpark**: Implement ELT (Extract, Load, Transform) by extracting data from HDFS, loading it into PySpark, and performing necessary transformation operations (e.g., aggregation, filtering, joining).

## Project Evolution: Methodology

**1. Shopify API Setup** (Completed on 2024-01-31)
- **Development storefront and custom app creation**: Shopify development storefront was created to simulate live e-commerce environment. A custom application was developed to enable authorized access to the storefront's data, with appropriate permission settings in place. 
- **API access token generation**: An admin API access token was generated, serving as an authentication mechanism for API requests used for data retrieval. 

**2. Initial Python Script Design** (Completed on 2024-01-31)
- **Script configuration**: Using the admin API access token, the python script was configured to access the Shopify store's data, including store name and product information. The initial endpoint in the function was set to `product.json`, however additional modifications can be made in the future to create a more generic function to fetch different types of data.
- **Data retrieval**: The script was programmed to fetch product information, generate a unique timestamp for each data retrieval session, and construct filenames incorporating these timestamps. The retrieved data was then stored in JSON format within a 'data' folder. 

**3. Version Control Implementation** (Completed on 2024-01-31)
- **Git repository initialization**: A Git repo was initialized within the project directory to enable version control, and allow for tracking and management of changes. 
- **Configuration file exclusion**: A `.gitignore` file was created to exclude a config file which stored the access token password. 

**4. Script Execution Automation** (Completed on 2024-02-01)
- **Task scheduling**: Employed a task scheduler to automate the execution of the python script at predetermined intervals (once per week). 

**5. Logging Integration** (Completed on 2024-02-01) 
- **Logging**: Updated the python script to include logging capabilities in order to capture records of operational processes, including timestamps and messages related to the success or failure of data ingestion tasks. 

**6. HDFS Setup** (In Progress)
- **Infrastructure development**: Attempting to establish a Hadoop Distributed File System (HDFS) for storage of the ingested data. 

 ## Project files
 
 ```dds_v1.py```: Automates data retrieval from Shopify API, saving the fetched data in JSON format.
