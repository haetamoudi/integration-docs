# Custom Google Pub/Sub Logs

The `gcp_pubsub` input package for Elastic enables real-time data ingestion from Google Cloud Pub/Sub topics. It allows users to subscribe to a Pub/Sub topic and pull messages, making it ideal for collecting various event-driven data like
Stackdriver logs. This input is designed for continuous processing, handling credentials and message acknowledgment to ensure reliable data flow into Elasticsearch for analysis.


## Setup

### Collecting logs from Custom Google Pub/Sub Logs

#### Configuration Parameters

##### Credentials File
*Optional*

*type*: text

*description*: Path to a JSON file containing the credentials and key used to subscribe.
##### Credentials JSON
*Optional*

*type*: password

*description*: JSON blob containing the credentials and key used to subscribe.
##### Dataset name
*Required*
*type*: text

*description*: Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).

##### Ingest Pipeline
*Optional*

*type*: text

*description*: The Ingest Node pipeline ID to be used by the integration.

##### Project ID
*Required*
*type*: text

*description*: 
##### Subscription Create
*Optional*

*type*: bool

*description*: If true, the integration will create the subscription on start.
##### Subscription Name
*Required*
*type*: text

*description*: 
##### Topic
*Required*
*type*: text

*description*: 

#### Advanced Parameters

#### Credentials File
*Optional*

*type*: text

*description*: Path to a JSON file containing the credentials and key used to subscribe.
#### Credentials JSON
*Optional*

*type*: password

*description*: JSON blob containing the credentials and key used to subscribe.
#### Dataset name
*Required*
*type*: text

*description*: Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).

#### Ingest Pipeline
*Optional*

*type*: text

*description*: The Ingest Node pipeline ID to be used by the integration.

#### Project ID
*Required*
*type*: text

*description*: 
#### Subscription Create
*Optional*

*type*: bool

*description*: If true, the integration will create the subscription on start.
#### Subscription Name
*Required*
*type*: text

*description*: 
#### Topic
*Required*
*type*: text

*description*: 

