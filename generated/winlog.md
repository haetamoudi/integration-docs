# Custom Windows Event Logs

The `winlog` input package for Elastic, typically used by Filebeat, is dedicated to collecting Windows event logs. It utilizes Windows APIs to read events from various logs such as Application, Security, and System. This input is crucial
for monitoring Windows systems, providing essential data for security analysis, troubleshooting, and general system health insights within the Elastic Stack.

For more details about the Winlog input settings, check the [Filebeat documentation](https://www.elastic.co/docs/reference/beats/filebeat/filebeat-input-winlog).


## Setup

The `winlog` input package for Elastic, is dedicated to collecting Windows event logs. It utilizes Windows APIs to read events from various logs such as Application, Security, and System.

To collect logs via Winlog, select **Collect logs via Winlog** and configure the following parameters:

#### Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Channel Name | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | Name of Windows event log channel (eg. Microsoft-Windows-PowerShell/Operational). It expects a single channel name. To collect multiple channels, add multiple integrations.  |
| Dataset name | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).  |
| Ingest Pipeline | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The Ingest Node pipeline ID to be used by the integration.   |
| Preserve original event | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | bool | Preserves a raw copy of the original XML event, added to the field `event.original`  |

#### Advanced Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Custom Configurations | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | YAML configuration options for winlog input. Be careful, this may break the integration.  |
| Event ID | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | A list of included and excluded (blocked) event IDs. The value is a comma-separated list.  The accepted values are single event IDs to include (e.g. 4624), a range of event IDs to include (e.g. 4700-4800),  and single event IDs to exclude (e.g. -4735).  Limit 22 clauses, lower in some situations. See integration documentation for more details.  |
| Ignore events older than | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | If this option is specified, events that are older than the specified amount of time are ignored. Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h".  |
| Language ID | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The language ID the events will be rendered in. The language will be forced regardless of the system language. A complete list of language IDs can be found [here](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-lcid/a9eac961-e77d-41a6-90a5-ce1a8b0cdb9c). It defaults to `0`, which indicates to use the system language. E.g.: `0x0409` for `en-US`  |
| Level | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | A list of event levels to include. The value is a comma-separated list of levels. Accepted levels are: `critical`, `error`, `warning`, `information`, and `verbose`.  |
| Providers | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | A list of providers (source names) to include.  |
| Tags | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Tags to include in the published event  |
| XML Query | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Provide a custom XML query. This option is mutually exclusive with the `name`, `event_id`, `ignore_older`, `level`, and `providers` options. These options should be included in the XML query directly. Furthermore, an id must be provided. Custom XML queries provide more flexibility and advanced options than the simpler query options.  |
