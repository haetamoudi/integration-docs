# Custom Logs (Deprecated)

The `log` input package for Elastic, primarily used by Filebeat, is designed to read and stream lines from various log files. It offers robust capabilities for monitoring specified file paths, collecting new log entries as they are written,
and forwarding them to Elasticsearch or other destinations. This input is essential for centralizing diverse log data from applications, servers, and other systems into the Elastic Stack for real-time analysis and troubleshooting.


## Setup



#### Advanced Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Custom configurations | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | Additional settings to be added to the configuration. Be careful using this as it might break the input as those settings are not validated and can override the settings specified above. See [`log` input settings docs](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-log.html) for details.   |
| Dataset name | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | Set the name for your dataset. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).   |
| Exclude files | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Patterns to be ignored  |
| Ignore events older than | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | If this option is specified, events that are older than the specified amount of time are ignored. Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h".  |
| Log file path | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | Path to log files to be collected  |
| Processors | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | Processors are used to reduce the number of fields in the exported event or to enhance the event with metadata. This executes in the agent before the logs are parsed. See [Processors](https://www.elastic.co/guide/en/beats/filebeat/current/filtering-and-enhancing-data.html) for details.  |
| Tags | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Tags to include in the published event  |
