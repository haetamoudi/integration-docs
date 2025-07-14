# GCP Metrics Input

The `gcp_metrics` input package for Elastic is designed to collect custom metrics from any Google Cloud Platform (GCP) service. It integrates with the GCP Cloud Monitoring API to gather a wide range of performance and operational data. This
allows users to monitor the health and performance of their GCP resources within Elastic, providing insights into various services like Compute Engine and Firestore. It's important to note that this package primarily focuses on metric
collection and typically requires custom ingest pipelines for pre-ingest data processing.


## Setup

### Collecting logs from GCP Metrics Input

#### Configuration Parameters

##### Credentials File
*Optional*

*type*: text

*description*: 
##### Credentials Json
*Optional*

*type*: text

*description*: 
##### Exclude Labels
*Optional*

*type*: bool

*description*: Exclude additional labels from metrics
##### GCP Metrics
*Required*
*type*: text

*description*: 
##### Project Id
*Required*
*type*: text

*description*: 
##### GCP Regions
*Optional*

*type*: text

*description*: 
##### GCP Service
*Required*
*type*: text

*description*: 
##### GCP Zone
*Optional*

*type*: text

*description*: 

#### Advanced Parameters

#### Credentials File
*Optional*

*type*: text

*description*: 
#### Credentials Json
*Optional*

*type*: text

*description*: 
#### Exclude Labels
*Optional*

*type*: bool

*description*: Exclude additional labels from metrics
#### GCP Metrics
*Required*
*type*: text

*description*: 
#### Project Id
*Required*
*type*: text

*description*: 
#### GCP Regions
*Optional*

*type*: text

*description*: 
#### GCP Service
*Required*
*type*: text

*description*: 
#### GCP Zone
*Optional*

*type*: text

*description*: 

