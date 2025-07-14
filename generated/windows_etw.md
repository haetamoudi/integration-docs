# Custom Windows ETW logs

The `windows_etw` input package for Elastic enables Filebeat to collect detailed event data directly from Event Tracing for Windows (ETW). This powerful Windows-native mechanism provides low-level telemetry about system performance and
application activity. The input supports various ETW providers and can operate in real-time by subscribing to new or existing sessions, or by processing pre-recorded .etl files for retrospective analysis.


## Setup

### Collecting logs from Custom Windows ETW logs


#### Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Dataset name | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).  |
| File | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Path to an .etl file to read from.  |
| Ingest Pipeline | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The Ingest Node pipeline ID to be used by the integration.   |
| Provider GUID | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | GUID of of an ETW provider (eg. `{EB79061A-A566-4698-9119-3ED2807060E7}`). Run `logman query providers` to list the available providers in the endpoint.  |
| Provider Name | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Name of of an ETW provider (eg. Microsoft-Windows-DNSServer). Run `logman query providers` to list the available providers in the endpoint.  |
| Session | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | An existing ETW session to read from. Existing sessions can be listed using `logman query -ets`.  |
| Session Name | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | When specifying a provider, a new session is created. This controls the name for the new ETW session it will create. If not specified, the session will be named using the provider ID prefixed by 'Elastic-'.  |
| Trace Level | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Defines the filtering level for events based on severity. Valid options include critical, error, warning, information, and verbose. The provider writes an event if the event's level is more severe or equal to the defined value.  |

#### Advanced Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Custom Configurations | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | Here YAML configuration options can be used to be added to your configuration. Be careful using this as it might break your configuration file.  |
| Match All Keyword | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Similar to MatchAnyKeyword, this 8-byte bitmask filters events that match all specified keyword bits. Default value is 0 to let every event pass. Run `logman query providers "<provider.name>"` to list the available keywords for a specific provider.  |
| Match Any Keyword | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | An 8-byte bitmask used for filtering events from specific provider subcomponents based on keyword matching. Any matching keyword will enable the event to be written. Default value is `0xfffffffffffffffff` so it matches every available keyword. Run `logman query providers "<provider.name>"` to list the available keywords for a specific provider.  |
| Tags | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Tags to include in the published event.  |

