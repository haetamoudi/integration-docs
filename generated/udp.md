# Custom UDP Logs

The `udp` input package for Elastic creates a listening UDP socket, allowing Logstash or Elastic Agent to receive and ingest data sent over UDP connections. This is particularly useful for collecting logs or metrics from sources that
transmit data via the unreliable but fast UDP protocol, such as syslog messages or custom application events. It provides flexibility for various data streams where guaranteed delivery is less critical than high throughput.


## Setup

### Collecting logs from Custom UDP Logs

#### Configuration Parameters

##### Dataset name
*Required*
*type*: text

*description*: Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).

##### Listen Address
*Required*
*type*: text

*description*: Bind address for the listener. Use 0.0.0.0 to listen on all interfaces.

##### Listen Port
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

#### Listen Port
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

