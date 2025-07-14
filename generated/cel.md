# Custom API using Common Expression Language

The `cel` input package for Elastic allows for highly customizable data ingestion from various sources, including HTTP APIs and local file systems. It leverages the Common Expression Language (CEL) to define a program that both fetches and
processes data. This enables advanced users to create flexible data collection pipelines, handling tasks like making HTTP requests, parsing diverse payloads, and maintaining state for continuous collection.


## Setup

### Collecting logs from Custom API using Common Expression Language

#### Configuration Parameters

##### Dataset name
*Required*
*type*: text

*description*: Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).

##### Delete redacted fields
*Required*
*type*: bool

*description*: The default behavior for field redaction is to replace characters with `*`s. If field value length or presence will
leak information, the fields can be deleted from logging by setting this configuration to true.

##### Digest No Challenge Reuse
*Optional*

*type*: bool

*description*: Selecting no challenge reuse prevents the transport from reusing digest challenges
##### Digest Auth Password
*Optional*

*type*: password

*description*: The password to be used with Digest Auth headers
##### Digest Auth Username
*Optional*

*type*: text

*description*: The username to be used with Digest Auth headers
##### OAuth2 Client ID
*Optional*

*type*: text

*description*: Client ID used for OAuth2 authentication
##### OAuth2 Client Secret
*Optional*

*type*: password

*description*: Client secret used for OAuth2 authentication
##### OAuth2 Token URL
*Optional*

*type*: text

*description*: The URL endpoint that will be used to generate the tokens during the oAuth2 flow. It is required if no oauth_custom variable is set or provider is not specified in oauth_custom variable.
##### Basic Auth Password
*Optional*

*type*: password

*description*: The password to be used with Basic Auth headers
##### Ingest Pipeline
*Optional*

*type*: text

*description*: The Ingest Node pipeline ID to be used by the integration.

##### The CEL program to be run for each polling.
*Required*
*type*: textarea

*description*: Program is the CEL program that is executed each polling period to get and transform the API data.
More information can be found in the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-cel.html#_execution).

##### Redacted fields
*Optional*

*type*: text

*description*: Fields to redact in debug logs. When logging at debug-level the input state and CEL evaluation state are included
in logs. This may leak secrets, so list sensitive state fields in this configuration.

##### Defined Regular Expressions
*Optional*

*type*: yaml

*description*: Regexps is the set of regular expression to be made available to the program by name. The syntax used is [RE2](https://github.com/google/re2/wiki/Syntax).
More information can be found in the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-cel.html#regexp-cel).

##### Resource Interval
*Required*
*type*: text

*description*: How often the API is polled, supports seconds, minutes and hours.
##### Resource URL
*Required*
*type*: text

*description*: i.e. scheme://host:port/path
##### Initial CEL evaluation state
*Optional*

*type*: yaml

*description*: State is the initial state to be provided to the program. If it has a cursor field, that field will be overwritten by any stored cursor, but will be available if no stored cursor exists.
More information can be found in the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-cel.html#input-state-cel).

##### Basic Auth Username
*Optional*

*type*: text

*description*: The username to be used with Basic Auth headers

#### Advanced Parameters

#### Dataset name
*Required*
*type*: text

*description*: Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).

#### Delete redacted fields
*Required*
*type*: bool

*description*: The default behavior for field redaction is to replace characters with `*`s. If field value length or presence will
leak information, the fields can be deleted from logging by setting this configuration to true.

#### Digest No Challenge Reuse
*Optional*

*type*: bool

*description*: Selecting no challenge reuse prevents the transport from reusing digest challenges
#### Digest Auth Password
*Optional*

*type*: password

*description*: The password to be used with Digest Auth headers
#### Digest Auth Username
*Optional*

*type*: text

*description*: The username to be used with Digest Auth headers
#### OAuth2 Client ID
*Optional*

*type*: text

*description*: Client ID used for OAuth2 authentication
#### OAuth2 Client Secret
*Optional*

*type*: password

*description*: Client secret used for OAuth2 authentication
#### OAuth2 Token URL
*Optional*

*type*: text

*description*: The URL endpoint that will be used to generate the tokens during the oAuth2 flow. It is required if no oauth_custom variable is set or provider is not specified in oauth_custom variable.
#### Basic Auth Password
*Optional*

*type*: password

*description*: The password to be used with Basic Auth headers
#### Ingest Pipeline
*Optional*

*type*: text

*description*: The Ingest Node pipeline ID to be used by the integration.

#### The CEL program to be run for each polling.
*Required*
*type*: textarea

*description*: Program is the CEL program that is executed each polling period to get and transform the API data.
More information can be found in the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-cel.html#_execution).

#### Redacted fields
*Optional*

*type*: text

*description*: Fields to redact in debug logs. When logging at debug-level the input state and CEL evaluation state are included
in logs. This may leak secrets, so list sensitive state fields in this configuration.

#### Defined Regular Expressions
*Optional*

*type*: yaml

*description*: Regexps is the set of regular expression to be made available to the program by name. The syntax used is [RE2](https://github.com/google/re2/wiki/Syntax).
More information can be found in the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-cel.html#regexp-cel).

#### Resource Interval
*Required*
*type*: text

*description*: How often the API is polled, supports seconds, minutes and hours.
#### Resource URL
*Required*
*type*: text

*description*: i.e. scheme://host:port/path
#### Initial CEL evaluation state
*Optional*

*type*: yaml

*description*: State is the initial state to be provided to the program. If it has a cursor field, that field will be overwritten by any stored cursor, but will be available if no stored cursor exists.
More information can be found in the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-cel.html#input-state-cel).

#### Basic Auth Username
*Optional*

*type*: text

*description*: The username to be used with Basic Auth headers

