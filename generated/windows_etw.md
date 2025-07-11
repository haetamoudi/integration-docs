# Custom Windows ETW logs

The `windows_etw` input package for Elastic enables Filebeat to collect detailed event data directly from Event Tracing for Windows (ETW). This powerful Windows-native mechanism provides low-level telemetry about system performance and
application activity. The input supports various ETW providers and can operate in real-time by subscribing to new or existing sessions, or by processing pre-recorded .etl files for retrospective analysis.


## Setup

### Collecting logs from Custom Windows ETW logs

#### Configuration Parameters

##### Dataset name
*Required*
*type*: text

*description*: Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).
##### File
*Optional*

*type*: text

*description*: Path to an .etl file to read from.
##### Ingest Pipeline
*Optional*

*type*: text

*description*: The Ingest Node pipeline ID to be used by the integration.

##### Provider GUID
*Optional*

*type*: text

*description*: GUID of of an ETW provider (eg. `{EB79061A-A566-4698-9119-3ED2807060E7}`). Run `logman query providers` to list the available providers in the endpoint.
##### Provider Name
*Optional*

*type*: text

*description*: Name of of an ETW provider (eg. Microsoft-Windows-DNSServer). Run `logman query providers` to list the available providers in the endpoint.
##### Session
*Optional*

*type*: text

*description*: An existing ETW session to read from. Existing sessions can be listed using `logman query -ets`.
##### Session Name
*Optional*

*type*: text

*description*: When specifying a provider, a new session is created. This controls the name for the new ETW session it will create. If not specified, the session will be named using the provider ID prefixed by 'Elastic-'.
##### Trace Level
*Optional*

*type*: text

*description*: Defines the filtering level for events based on severity. Valid options include critical, error, warning, information, and verbose. The provider writes an event if the event's level is more severe or equal to the defined value.

#### Advanced Parameters

#### Dataset name
*Required*
*type*: text

*description*: Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).
#### File
*Optional*

*type*: text

*description*: Path to an .etl file to read from.
#### Ingest Pipeline
*Optional*

*type*: text

*description*: The Ingest Node pipeline ID to be used by the integration.

#### Provider GUID
*Optional*

*type*: text

*description*: GUID of of an ETW provider (eg. `{EB79061A-A566-4698-9119-3ED2807060E7}`). Run `logman query providers` to list the available providers in the endpoint.
#### Provider Name
*Optional*

*type*: text

*description*: Name of of an ETW provider (eg. Microsoft-Windows-DNSServer). Run `logman query providers` to list the available providers in the endpoint.
#### Session
*Optional*

*type*: text

*description*: An existing ETW session to read from. Existing sessions can be listed using `logman query -ets`.
#### Session Name
*Optional*

*type*: text

*description*: When specifying a provider, a new session is created. This controls the name for the new ETW session it will create. If not specified, the session will be named using the provider ID prefixed by 'Elastic-'.
#### Trace Level
*Optional*

*type*: text

*description*: Defines the filtering level for events based on severity. Valid options include critical, error, warning, information, and verbose. The provider writes an event if the event's level is more severe or equal to the defined value.

