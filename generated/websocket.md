# Custom Websocket logs

The `websocket` input package for Elastic enables the ingestion of real-time data from WebSocket servers. It connects to a specified WebSocket URL, listens for incoming messages, and processes them as they arrive. This allows for
low-latency, full-duplex communication, making it ideal for streaming data like live updates, financial feeds, or IoT sensor data directly into the Elastic Stack for near real-time analysis.


## Setup

### Collecting logs from Custom Websocket logs


#### Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Basic Auth Token | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | password | The token to be used for Basic Authentication.  |
| Bearer Auth Token | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | password | The token to be used for Bearer Authentication.  |
| Dataset name | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).   |
| Delete redacted fields | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | bool | The default behavior for field redaction is to replace characters with `*`s. If field value length or presence will leak information, the fields can be deleted from logging by setting this configuration to true.   |
| Custom Header Key | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The custom header key name for Authentication.  |
| Custom Header Value | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | password | The custom header key value for Authentication.  |
| Maximum Reconnect Attempts | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | integer | The maximum number of times the agent will attempt to reconnect to the websocket endpoint if the connection is lost before giving up.  |
| Maximum Wait Time | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The maximum amount of time the agent will wait before attempting to reconnect to the websocket endpoint if the connection is lost.  This is a time duration value. Examples, 1s, 1m, 1h.   |
| Minimum Wait Time | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The minimum amount of time the agent will wait before attempting to reconnect to the websocket endpoint if the connection is lost.  This is a time duration value. Examples, 1s, 1m, 1h.   |
| Ingest Pipeline | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The Ingest Node pipeline ID to be used by the integration.   |
| The CEL program to be run for each message. | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | textarea | Program is the The CEL program that is executed on each message received. More information can be found in the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-websocket.html#_execution_2).   |
| Redacted fields | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Fields to redact in debug logs. When logging at debug-level the input state and CEL evaluation state are included in logs. This may leak secrets, so list sensitive state fields in this configuration.   |
| Defined Regular Expressions | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | Regexps is the set of regular expression to be made available to the program by name. The syntax used is [RE2](https://github.com/google/re2/wiki/Syntax). More information can be found in the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-websocket.html#regexp-websocket).   |
| Initial CEL evaluation state | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | State is the initial state to be provided to the program. If it has a cursor field, that field will be overwritten by any stored cursor, but will be available if no stored cursor exists. More information can be found in the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-websocket.html#state-websocket).   |
| URL | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | URL of the Websocket Server.  |

#### Advanced Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Blanket Retries | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | If enabled the agent will retry connection attempts irrespective of the type of connection/network error.  |
| Infinite Retries | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | If enabled the agent will retry connection attempts indefinitely irrespective of the "Maximum Reconnect Attempts" value.  |
| Processors | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | Processors are used to reduce the number of fields in the exported event or to enhance the event with metadata. This executes in the agent before the logs are parsed. See [Processors](https://www.elastic.co/guide/en/beats/filebeat/current/filtering-and-enhancing-data.html) for details.  |
| SSL Configuration | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | i.e. certificate_authorities, supported_protocols, verification_mode etc, more examples found in the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/configuration-ssl.html#ssl-common-config).  |
| Tags | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text |   |

