# Terms and definitions

    GCP Input Knowledge Evaluation, 5.10.2021
    Final score: 25/75

## Tools

### Stackdriver Logging
Is a managed service designed for storing logging data. Is used to collect semi-structured data about events.

### Stackdriver Monitoring
Collects performance metrics, and the slot metrics are the ones that show resource utilization related to queries

### Stackdriver Debugger
Is used to inspect the state of running code.

### Stackdriver Trace
Is used to collect information about the time required to execute functions in a call stack.

### Cloud Dataflow
Its implementation of the Apache Beam model that is used for executing stream and batch processing program.

### Apache Flink
Its implementation of the Apache Beam model that is used for executing stream and batch processing program.

### Data Studio
Is used for reporting and visualizing data.


## Services

----

### Cloud Bigtable
Is a wide-column NoSQL database that supports semi-structured data and works well with datasets over 1 TB. 
Is the best storage service for IoT data, especially when a large number of devices will be sending data at short intervals. 
Doesn't support SQL. 

### Cloud Storage
Is used for unstructured data. Doesn't support querying the contents of objects, streaming inserts.

### Cloud SQL
Is a fully managed RDBMS: MySQl, PostgreSQL, etc. so it may be used to store data (structured data), but it is not a service specifically 
for ingesting and transforming data before writing to a database. Is designed for transaction processing at a regional level.
Does not currently scale to 40 TB in a single database.

### Cloud Spanner
Is designed for transaction processing, and although it scales to global levels, it is not the best option for IoT data.
For structured data. 

### Cloud Datastore
Doesn't support SQL.

----

### Cloud Composer
Is a managed workflow service, designed to support workflow orchestration.

### Cloud Dataflow
Stream and batch processing service that is used for transforming data and processing streaming data.

### Cloud Dataproc
Is a managed Hadoop and Spark service and not as well suited as Cloud Dataflow for the kind of stream processing specified.  
Good for batch processing jobs.

### Cloud Dataprep
Is an interactive service for exploring and preparing (deduplication, cleansing) data sets for analysis and machine learning.

### Cloud Catalog
Is designed to help data consumers understand what data is available, what it means, and how it can be used. 



### Cloud Pub/Sub
Is a scalable, managed messaging queue that is typically used for ingesting high-volume streaming data.

### Cloud Datalab
Do visualization and data filtering, run custom Python functions. Allows working interactively with the data. 


### BigQuery
1. It's serverless.
2. Flexible pricing model
3. Data encryption and security
4. Geospatial data types & functions
5. Foundation for BI and AI

Uses columnar storage. For structured data. Has streaming inserts, but is designed for analytic operations.
BigQuery does use Colossus, but that does not change the number of joins.
The roles/BigQuery.jobUser role allows users to run jobs, including queries. 


### BigQuery ML
Provides access to machine learning algorithms from within SQL, and there is no need to move the data from BigQuery. 
Also, BigQuery builds models faster than AutoML.

### AutoML Tables
### Kubeflow
Requires some machine learning experience to use.
### Spark MLib
Requires some machine learning experience to use.


----

## Storages

### Key-value database
Doesn't support indexing on non-key attributes.

### Document database
For a semi-structured schema. Could store the volume of data, and it provides for indexing on columns other than a single key. 

### Analytical database
Is structured data store. Is not a type of NoSQL database.

### Wide-column database
Doesn't support indexing on non-key attributes.


## Data models

### OLTP
OLTP models are designed to facilitate storing, searching, and retrieving individual records in a database.

### OLAP
OLAP data models are designed to support drilling down and slicing and dicing. Often employ denormalization.

### Graph
Graph data models are used to model nodes and their relationships, such as those in social networks.

## Big Data Challenges
1. migrating existing big data workloads (e.g. Hadoop, Spark jobs)
2. Analyzing large datasets at scale
3. Building streaming data pipelines
4. Applying machine learning to your data

## Google Cloud overall architecture
|       Big Data and ML Products        |
|:-------------------------------------:|
|Compute Power / Storage / Networking   |
|           Security                    |