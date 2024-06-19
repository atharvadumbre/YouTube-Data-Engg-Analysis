# Data Engineering & Analysis with AWS and Power BI on YouTube Dataset

This repository contains the code and documentation for a data engineering and analysis project that uses various AWS services to create a data pipeline and Power BI for building a dashboard. The dataset used is the YouTube Trending Videos dataset available on Kaggle.

## Dataset

**Source**: [YouTube Trending Videos](https://www.kaggle.com/datasets/datasnaek/youtube-new/data)

### Description

This dataset includes several months of data on daily trending YouTube videos from multiple regions: US, GB, DE, CA, FR, RU, MX, KR, JP, and IN. Each region’s data is stored in a separate file and includes information such as video title, channel title, publish time, tags, views, likes, dislikes, description, and comment count.

## Project Architecture

This project follows an architecture inspired by Darshil Parmar. The process involves creating a data pipeline for data pre-processing and building a Power BI dashboard.

### ETL Data Pipeline

1. **IAM Setup**: Created the required IAM users and roles (S3-Glue).
2. **Data Transfer**: Uploaded the dataset to an S3 bucket as the initial raw data repository.
3. **Data Crawling & Cataloging**: Used AWS Glue to create a database for raw data, setting up tables for reference data and actual data after crawling the initial S3 bucket.
4. **Data Conversion**: Implemented an AWS Lambda function to convert JSON files to Parquet format for efficiency.
5. **ETL Jobs**: Developed a Glue ETL job for Canada, USA, and Great Britain regions, creating an analytics database. Queried the data using AWS Athena to join reference data and actual data.
6. **Automation & Monitoring**: Set triggers to launch the Lambda function upon S3 updates and used AWS CloudWatch to monitor all jobs and functions.
7. **Data Visualization**: Built a detailed dashboard in Power BI, displaying various KPIs and trends. Connected Power BI to AWS Data Catalog using ODBC driver.

### Challenges & Solutions

1. **CloudWatch Logs Role**: Needed to change the auto-assigned CloudWatch logs role in Lambda to allow S3 permissions.
2. **Lambda Deployment**: Required deployment for testing functions.
3. **Data Type Mismatch**: Encountered issues with the "id" column in Parquet files being binary. Resolved by casting it to "int64".

## Data Visualization

Fetched data into Power BI via ODBC driver, connecting to AWS Data Catalog to create a dynamic and insightful dashboard.

![dashboard](https://github.com/atharvadumbre/YouTube-Data-Engg-Analysis/assets/59522832/2de3dbe8-e9b3-414a-b623-add76254b7bc)



## Next Steps

Currently, only data from 3 regions are processed due to encoding issues with non-UTF-8 formats in other regions' data. A temporary manual solution involves re-saving files in VSCode with "UTF-8" encoding. Exploring automation methods for this task to streamline the process further.

## How to Run

1. **Setup AWS Environment**:
   - Create required IAM users and roles.
   - Setup S3 buckets for raw data.
   - Setup AWS Glue for data cataloging and ETL jobs.
   - Implement AWS Lambda functions for data conversion.

2. **Data Processing**:
   - Transfer dataset to S3 bucket.
   - Use AWS Glue to catalog the data.
   - Convert JSON files to Parquet using Lambda functions.
   - Execute Glue ETL jobs to process data.

3. **Data Visualization**:
   - Connect Power BI to AWS Data Catalog using ODBC driver.
   - Create and customize the dashboard to display key metrics and trends.

## Repository Structure

- `scripts/`: AWS Lambda jobs and glue ETL Jobs.
- `powerbi-dashboard/`: Power BI files and documentation for dashboard creation.


This project was a fantastic opportunity to delve into AWS services and Power BI, overcoming challenges and gaining insights from the YouTube trending dataset. Looking forward to implementing more regions and enhancing the pipeline!

### Connect with Me

- LinkedIn: [Atharva Dumbre](https://www.linkedin.com/in/atharvadumbre/)
- Email: [atharva.dumbre1@gmail.com](mailto:atharva.dumbre1@gmail.com)

Happy Data Engineering! 🚀
