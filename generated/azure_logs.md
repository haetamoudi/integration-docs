# Custom Azure Logs

The `azure_logs` input package for Elastic facilitates the collection of logs from various Azure services. It supports specialized integrations for services like Microsoft Entra ID (Sign-in, Audit, Identity Protection, Provisioning), Azure
Spring Apps, and Azure Firewall, as well as a generic integration for any Azure service. This input typically leverages Azure Event Hubs and Storage Accounts to ingest log data into Elasticsearch for analysis, visualization, and alerting
within Kibana. It helps users gain insights into their Azure environment for security, observability, and operational troubleshooting.


## Setup

### Collecting logs from Custom Azure Logs

#### Configuration Parameters

##### Connection String
*Required*
*type*: password

*description*: The connection string required to communicate with Event Hubs. See [Get an Event Hubs connection string](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-get-connection-string) to learn more.
##### Consumer Group
*Required*
*type*: text

*description*: 
##### Dataset name
*Required*
*type*: text

*description*: Dataset to write data to. Changing the dataset will send the data to a different index.  You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).
##### Event Hub Name
*Required*
*type*: text

*description*: The event hub name that contains the logs to ingest. Do not use the event hub namespace here. Elastic recommends using one event hub for each integration. Visit [Create an event hub](https://docs.elastic.co/integrations/azure#create-an-event-hub) to learn more. Use event hub names up to 30 characters long to avoid compatibility issues.
##### Ingest Pipeline
*Optional*

*type*: text

*description*: The ingest pipeline ID to use for processing the data. If provided, replaces the default pipeline for this integration.
##### Storage Account
*Required*
*type*: text

*description*: The name of the storage account where the consumer group's state/offsets will be stored and updated.
##### Storage Account Key
*Required*
*type*: password

*description*: The storage account key, this key will be used to authorize access to data in your storage account.

#### Advanced Parameters

#### Connection String
*Required*
*type*: password

*description*: The connection string required to communicate with Event Hubs. See [Get an Event Hubs connection string](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-get-connection-string) to learn more.
#### Consumer Group
*Required*
*type*: text

*description*: 
#### Dataset name
*Required*
*type*: text

*description*: Dataset to write data to. Changing the dataset will send the data to a different index.  You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).
#### Event Hub Name
*Required*
*type*: text

*description*: The event hub name that contains the logs to ingest. Do not use the event hub namespace here. Elastic recommends using one event hub for each integration. Visit [Create an event hub](https://docs.elastic.co/integrations/azure#create-an-event-hub) to learn more. Use event hub names up to 30 characters long to avoid compatibility issues.
#### Ingest Pipeline
*Optional*

*type*: text

*description*: The ingest pipeline ID to use for processing the data. If provided, replaces the default pipeline for this integration.
#### Storage Account
*Required*
*type*: text

*description*: The name of the storage account where the consumer group's state/offsets will be stored and updated.
#### Storage Account Key
*Required*
*type*: password

*description*: The storage account key, this key will be used to authorize access to data in your storage account.

