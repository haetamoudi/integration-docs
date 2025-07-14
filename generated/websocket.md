# Custom Websocket logs

The `websocket` input package for Elastic enables the ingestion of real-time data from WebSocket servers. It connects to a specified WebSocket URL, listens for incoming messages, and processes them as they arrive. This allows for
low-latency, full-duplex communication, making it ideal for streaming data like live updates, financial feeds, or IoT sensor data directly into the Elastic Stack for near real-time analysis.


## Setup

### Collecting logs from Custom Websocket logs

#### Configuration Parameters

##### Basic Auth Token
*Optional*

*type*: password

*description*: The token to be used for Basic Authentication.
##### Bearer Auth Token
*Optional*

*type*: password

*description*: The token to be used for Bearer Authentication.
##### Dataset name
*Required*
*type*: text

*description*: Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).

##### Delete redacted fields
*Required*
*type*: bool

*description*: The default behavior for field redaction is to replace characters with `*`s. If field value length or presence will
leak information, the fields can be deleted from logging by setting this configuration to true.

##### Custom Header Key
*Optional*

*type*: text

*description*: The custom header key name for Authentication.
##### Custom Header Value
*Optional*

*type*: password

*description*: The custom header key value for Authentication.
##### Maximum Reconnect Attempts
*Optional*

*type*: integer

*description*: The maximum number of times the agent will attempt to reconnect to the websocket endpoint if the connection is lost before giving up.
##### Maximum Wait Time
*Optional*

*type*: text

*description*: The maximum amount of time the agent will wait before attempting to reconnect to the websocket endpoint if the connection is lost. 
This is a time duration value. Examples, 1s, 1m, 1h.

##### Minimum Wait Time
*Optional*

*type*: text

*description*: The minimum amount of time the agent will wait before attempting to reconnect to the websocket endpoint if the connection is lost. 
This is a time duration value. Examples, 1s, 1m, 1h.

##### Ingest Pipeline
*Optional*

*type*: text

*description*: The Ingest Node pipeline ID to be used by the integration.

##### The CEL program to be run for each message.
*Required*
*type*: textarea

*description*: Program is the The CEL program that is executed on each message received.
More information can be found in the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-websocket.html#_execution_2).

##### Redacted fields
*Optional*

*type*: text

*description*: Fields to redact in debug logs. When logging at debug-level the input state and CEL evaluation state are included
in logs. This may leak secrets, so list sensitive state fields in this configuration.

##### Defined Regular Expressions
*Optional*

*type*: yaml

*description*: Regexps is the set of regular expression to be made available to the program by name. The syntax used is [RE2](https://github.com/google/re2/wiki/Syntax).
More information can be found in the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-websocket.html#regexp-websocket).

##### Initial CEL evaluation state
*Optional*

*type*: yaml

*description*: State is the initial state to be provided to the program. If it has a cursor field, that field will be overwritten by any stored cursor, but will be available if no stored cursor exists.
More information can be found in the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-websocket.html#state-websocket).

##### URL
*Required*
*type*: text

*description*: URL of the Websocket Server.

#### Advanced Parameters

#### Basic Auth Token
*Optional*

*type*: password

*description*: The token to be used for Basic Authentication.
#### Bearer Auth Token
*Optional*

*type*: password

*description*: The token to be used for Bearer Authentication.
#### Dataset name
*Required*
*type*: text

*description*: Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).

#### Delete redacted fields
*Required*
*type*: bool

*description*: The default behavior for field redaction is to replace characters with `*`s. If field value length or presence will
leak information, the fields can be deleted from logging by setting this configuration to true.

#### Custom Header Key
*Optional*

*type*: text

*description*: The custom header key name for Authentication.
#### Custom Header Value
*Optional*

*type*: password

*description*: The custom header key value for Authentication.
#### Maximum Reconnect Attempts
*Optional*

*type*: integer

*description*: The maximum number of times the agent will attempt to reconnect to the websocket endpoint if the connection is lost before giving up.
#### Maximum Wait Time
*Optional*

*type*: text

*description*: The maximum amount of time the agent will wait before attempting to reconnect to the websocket endpoint if the connection is lost. 
This is a time duration value. Examples, 1s, 1m, 1h.

#### Minimum Wait Time
*Optional*

*type*: text

*description*: The minimum amount of time the agent will wait before attempting to reconnect to the websocket endpoint if the connection is lost. 
This is a time duration value. Examples, 1s, 1m, 1h.

#### Ingest Pipeline
*Optional*

*type*: text

*description*: The Ingest Node pipeline ID to be used by the integration.

#### The CEL program to be run for each message.
*Required*
*type*: textarea

*description*: Program is the The CEL program that is executed on each message received.
More information can be found in the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-websocket.html#_execution_2).

#### Redacted fields
*Optional*

*type*: text

*description*: Fields to redact in debug logs. When logging at debug-level the input state and CEL evaluation state are included
in logs. This may leak secrets, so list sensitive state fields in this configuration.

#### Defined Regular Expressions
*Optional*

*type*: yaml

*description*: Regexps is the set of regular expression to be made available to the program by name. The syntax used is [RE2](https://github.com/google/re2/wiki/Syntax).
More information can be found in the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-websocket.html#regexp-websocket).

#### Initial CEL evaluation state
*Optional*

*type*: yaml

*description*: State is the initial state to be provided to the program. If it has a cursor field, that field will be overwritten by any stored cursor, but will be available if no stored cursor exists.
More information can be found in the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-websocket.html#state-websocket).

#### URL
*Required*
*type*: text

*description*: URL of the Websocket Server.

