# Custom Windows Event Logs

The `winlog` input package for Elastic, typically used by Filebeat, is dedicated to collecting Windows event logs. It utilizes Windows APIs to read events from various logs such as Application, Security, and System. This input is crucial
for monitoring Windows systems, providing essential data for security analysis, troubleshooting, and general system health insights within the Elastic Stack.


## Setup

### Collecting logs from Custom Windows Event Logs

#### Configuration Parameters

##### Channel Name
*Required*
*type*: text

*description*: Name of Windows event log channel (eg. Microsoft-Windows-PowerShell/Operational). It expects a single channel name. To collect multiple channels, add multiple integrations.
##### Dataset name
*Required*
*type*: text

*description*: Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).
##### Ingest Pipeline
*Optional*

*type*: text

*description*: The Ingest Node pipeline ID to be used by the integration.

##### Preserve original event
*Required*
*type*: bool

*description*: Preserves a raw copy of the original XML event, added to the field `event.original`

#### Advanced Parameters

#### Channel Name
*Required*
*type*: text

*description*: Name of Windows event log channel (eg. Microsoft-Windows-PowerShell/Operational). It expects a single channel name. To collect multiple channels, add multiple integrations.
#### Dataset name
*Required*
*type*: text

*description*: Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).
#### Ingest Pipeline
*Optional*

*type*: text

*description*: The Ingest Node pipeline ID to be used by the integration.

#### Preserve original event
*Required*
*type*: bool

*description*: Preserves a raw copy of the original XML event, added to the field `event.original`

