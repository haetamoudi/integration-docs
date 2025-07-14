# SQL Input

The `sql` input package for Elastic enables Logstash or Metricbeat to execute custom SQL queries against various relational databases. It retrieves the results of these queries and ingests them as structured events into Elasticsearch. This
input is highly flexible, supporting multiple database drivers (e.g., MySQL, PostgreSQL, Oracle, MSSQL) and allowing users to define specific SQL statements for pulling custom metrics or data.


## Setup

### Collecting logs from SQL Input

#### Configuration Parameters

##### Driver
*Required*
*type*: text

*description*: 
##### Hosts
*Required*
*type*: password

*description*: 
##### SQL Queries
*Required*
*type*: yaml

*description*: 

#### Advanced Parameters

#### Driver
*Required*
*type*: text

*description*: 
#### Hosts
*Required*
*type*: password

*description*: 
#### SQL Queries
*Required*
*type*: yaml

*description*: 

