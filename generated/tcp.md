# Custom TCP Logs

The `tcp` input package for Elastic establishes a listening TCP socket, allowing Logstash or Elastic Agent to receive and ingest data sent over TCP connections. This input is highly versatile, commonly used for collecting raw log lines,
events, or other structured data from applications and devices that communicate via the TCP protocol. It supports various codecs for parsing the incoming data and can be configured with SSL for secure communication.


## Setup

### Collecting logs from Custom TCP Logs

#### Configuration Parameters

##### Dataset name
*Required*
*type*: text

*description*: Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).

##### Listen Address
*Required*
*type*: text

*description*: Bind address for the listener. Use 0.0.0.0 to listen on all interfaces.

##### Listen port
*Required*
*type*: text

*description*: Bind port for the listener.

##### Ingest Pipeline
*Optional*

*type*: text

*description*: The Ingest Node pipeline ID to be used by the integration.

##### Preserve original event
*Required*
*type*: bool

*description*: Preserves a raw copy of the original event, added to the field `event.original`.
##### Syslog Parsing
*Optional*

*type*: bool

*description*: Enable the syslog parser to automatically parse RFC3164 and RFC5424 syslog formatted data. The syslog parser can be configured under Advanced Options.
##### Tags
*Optional*

*type*: text

*description*: Tags to include in the published event

#### Advanced Parameters

#### Dataset name
*Required*
*type*: text

*description*: Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).

#### Listen Address
*Required*
*type*: text

*description*: Bind address for the listener. Use 0.0.0.0 to listen on all interfaces.

#### Listen port
*Required*
*type*: text

*description*: Bind port for the listener.

#### Ingest Pipeline
*Optional*

*type*: text

*description*: The Ingest Node pipeline ID to be used by the integration.

#### Preserve original event
*Required*
*type*: bool

*description*: Preserves a raw copy of the original event, added to the field `event.original`.
#### Syslog Parsing
*Optional*

*type*: bool

*description*: Enable the syslog parser to automatically parse RFC3164 and RFC5424 syslog formatted data. The syslog parser can be configured under Advanced Options.
#### Tags
*Optional*

*type*: text

*description*: Tags to include in the published event

