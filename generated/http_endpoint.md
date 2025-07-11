# Custom HTTP Endpoint Logs

The `http_endpoint` input package for Elastic initializes a listening HTTP server, allowing Logstash or Beats to collect incoming HTTP POST requests. It is designed to ingest JSON-formatted data, which can be an object or an array of objects.
This input is commonly used for receiving webhooks from third-party applications or services, facilitating real-time data ingestion into the Elastic Stack.


## Setup

### Collecting logs from Custom HTTP Endpoint Logs

#### Configuration Parameters

##### Dataset name
*Required*
*type*: text

*description*: Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).

##### Listen Address
*Required*
*type*: text

*description*: Bind address for the HTTP listener. Use 0.0.0.0 to listen on all interfaces.

##### Listen port
*Required*
*type*: text

*description*: Bind port for the listener.

##### Ingest Pipeline
*Optional*

*type*: text

*description*: The Ingest Node pipeline ID to be used by the integration.

##### Preserve Original Event
*Optional*

*type*: bool

*description*: This option copies the raw unmodified body of the incoming request to the event.original field as a string before sending the event to Elasticsearch.
##### Tags
*Optional*

*type*: text

*description*: Tags to include in the published event
##### URL
*Optional*

*type*: text

*description*: This options specific which URL path to accept requests on. Defaults to /.

#### Advanced Parameters

#### Dataset name
*Required*
*type*: text

*description*: Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).

#### Listen Address
*Required*
*type*: text

*description*: Bind address for the HTTP listener. Use 0.0.0.0 to listen on all interfaces.

#### Listen port
*Required*
*type*: text

*description*: Bind port for the listener.

#### Ingest Pipeline
*Optional*

*type*: text

*description*: The Ingest Node pipeline ID to be used by the integration.

#### Preserve Original Event
*Optional*

*type*: bool

*description*: This option copies the raw unmodified body of the incoming request to the event.original field as a string before sending the event to Elasticsearch.
#### Tags
*Optional*

*type*: text

*description*: Tags to include in the published event
#### URL
*Optional*

*type*: text

*description*: This options specific which URL path to accept requests on. Defaults to /.

