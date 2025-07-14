# Custom UDP Logs

The `udp` input package for Elastic creates a listening UDP socket, allowing Logstash or Elastic Agent to receive and ingest data sent over UDP connections. This is particularly useful for collecting logs or metrics from sources that
transmit data via the unreliable but fast UDP protocol, such as syslog messages or custom application events. It provides flexibility for various data streams where guaranteed delivery is less critical than high throughput.


## Setup

### Collecting logs from Custom UDP Logs


#### Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Dataset name | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).   |
| Listen Address | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | Bind address for the listener. Use 0.0.0.0 to listen on all interfaces.   |
| Listen Port | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | Bind port for the listener.   |
| Ingest Pipeline | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The Ingest Node pipeline ID to be used by the integration.   |
| Preserve original event | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | bool | Preserves a raw copy of the original event, added to the field `event.original`.  |
| Syslog Parsing | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | Enable the syslog parser to automatically parse RFC3164 and RFC5424 syslog formatted data. The syslog parser can be configured under Advanced Options.  |
| Tags | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Tags to include in the published event  |

#### Advanced Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Custom configurations | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | Here YAML configuration options can be used to be added to your configuration. Be careful using this as it might break your configuration file.   |
| Keep Null Values | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | If this option is set to true, fields with null values will be published in the output document. By default, keep_null is set to false.  |
| Max Message Size | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The maximum size of the message received over UDP. The default is 10KiB  |
| Processors | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | Processors are used to reduce the number of fields in the exported event or to enhance the event with metadata. This executes in the agent before the logs are parsed. See [Processors](https://www.elastic.co/guide/en/beats/filebeat/current/filtering-and-enhancing-data.html) for details.   |
| Read Buffer Size | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The size of the read buffer on the UDP socket in the format KiB/MiB, an example would be: 10KiB   |
| Syslog Options | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | i.e. format, time zone, etc.  |
| Timeout | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The read and write timeout for socket operations. Valid time units are ns, us, ms, s, m, h.  |

