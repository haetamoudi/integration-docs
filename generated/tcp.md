# Custom TCP Logs

The `tcp` input package for Elastic establishes a listening TCP socket, allowing Logstash or Elastic Agent to receive and ingest data sent over TCP connections. This input is highly versatile, commonly used for collecting raw log lines,
events, or other structured data from applications and devices that communicate via the TCP protocol. It supports various codecs for parsing the incoming data and can be configured with SSL for secure communication.


## Setup

### Collecting logs from Custom TCP Logs

To collect logs with the `tcp` input, configure the Listen Address and Listen Port. When deployed with Elastic Agent, the agent will listen for TCP messages on the configured address and port.
If a secure TCP connection is used, you may need to specify the SSL details in the `SSL` parameter.

#### Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Dataset name | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).   |
| Listen Address | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | Bind address for the listener. Use 0.0.0.0 to listen on all interfaces.   |
| Listen port | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | Bind port for the listener.   |
| Ingest Pipeline | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The Ingest Node pipeline ID to be used by the integration.   |
| Preserve original event | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | bool | Preserves a raw copy of the original event, added to the field `event.original`.  |
| Syslog Parsing | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | Enable the syslog parser to automatically parse RFC3164 and RFC5424 syslog formatted data. The syslog parser can be configured under Advanced Options.  |
| Tags | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Tags to include in the published event  |

#### Advanced Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Custom configurations | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | Here YAML configuration options can be used to be added to your configuration. Be careful using this as it might break your configuration file.   |
| Framing | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Specify the framing used to split incoming events. Can be one of delimiter or rfc6587. The default is delimiter  |
| Keep Null Values | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | If this option is set to true, fields with null values will be published in the output document. By default, keep_null is set to false.  |
| Line Delimiter | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Specify the characters used to split the incoming events. The default is \n.  |
| Max Connections | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The at most number of connections to accept at any given point in time.  |
| Max Message Size | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The maximum size of the message received over TCP. The default is 20MiB  |
| Processors | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | Processors are used to reduce the number of fields in the exported event or to enhance the event with metadata. This executes in the agent before the logs are parsed. See [Processors](https://www.elastic.co/guide/en/beats/filebeat/current/filtering-and-enhancing-data.html) for details.   |
| SSL Configuration | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | SSL configuration options. See [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/configuration-ssl.html#ssl-common-config) for details.  |
| Syslog Configuration | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | i.e. field, format, time zone, etc. See [Syslog](https://www.elastic.co/guide/en/beats/filebeat/current/syslog.html) for details.  |
| Timeout | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The duration of inactivity before a remote connection is closed. The default is 300s. Valid time units are ns, us, ms, s, m, h.  |

