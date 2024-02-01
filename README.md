# Batch Processing with HDFS and Apache PySpark

The project aims to create an automated data ingestion and analysis pipeline that fetches data from a third-party API, stores it in HDFS, and processes it with PySpark for further analysis and insights.

## Objectives

- **Choose a Third-Party API**: Find and select a third-party API for data ingestion.
- **Set Up Batch Data Ingestion**: Develop a script for regular data fetching from the chosen API in scheduled batches.
- **Save Data Using HDFS**: Store the collected data using HDFS (Hadoop Distributed File System).
- **Process Data with Apache PySpark**: Implement ELT (Extract, Load, Transform) by extracting data from HDFS, loading it into PySpark, and performing necessary transformation operations (e.g., aggregation, filtering, joining).

## Project Evolution: Methodology

### **1. Shopify API Setup** (Completed on 2024-01-31)
- #### **Development storefront and custom app creation**: Created a Shopify development storefront to simulate live e-commerce environment. Developed a custom application to enable authorized access to the storefront's data, with appropriate permission settings in place. 
- #### **API access token generation**: Generated an admin API access token to serve as an authentication mechanism for API requests for data retrieval. 

### **2. Initial Python Script Design** (Completed on 2024-01-31)
- #### **Script configuration**: Configured the Python script using the admin API access token to access the Shopify store's data, including store name and product information. Initially set the endpoint to product.json, but the script is designed for future enhancements to fetch different data types.
- #### **Data retrieval**: Programmed the script to fetch product information, generate a unique timestamp for each data retrieval session, and construct filenames incorporating these timestamps. Stored the retrieved data in JSON format within a 'data' folder. 

### **3. Version Control Implementation** (Completed on 2024-01-31)
- #### **Git repository initialization**: Initialized a Git repository within the project directory to enable version control and allow for the tracking and management of changes. 
- #### **Configuration file exclusion**: Created a .gitignore file to exclude the config file storing the access token password from version control. 

### **4. Script Execution Automation** (Completed on 2024-02-01)
- **Task scheduling**: Employed a task scheduler to automate the execution of the Python script at predetermined intervals (once per week).

### **5. Logging Integration** (Completed on 2024-02-01) 
- **Logging**: Updated the Python script to include logging capabilities to capture records of operational processes, including timestamps and messages related to the success or failure of data ingestion tasks. 

### **6. HDFS Setup** (In Progress)
- **Infrastructure development**: Working on establishing a Hadoop Distributed File System (HDFS) for the storage of ingested data.

 ## Project files
 Please visit the GitHub repository to view all project files. Key files include
 ```dds_v1.py```: Automates data retrieval from the Shopify API and saves the fetched data in JSON format.

## Prerequisites

To run or contribute to this project, you will need:
- Python 3.x
- Access to a Hadoop environment for HDFS
- Apache PySpark
- Necessary credentials for the Shopify API

## Contact Information
For questions, feedback, or contributions, feel free to reach out through Linkedin or create an on the GitHub repository.
