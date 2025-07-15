# Custom HTTP Endpoint Logs

The `http_endpoint` input package for Elastic initializes a listening HTTP server, allowing Logstash or Beats to collect incoming HTTP POST requests. It is designed to ingest JSON-formatted data, which can be an object or an array of objects.
This input is commonly used for receiving webhooks from third-party applications or services, facilitating real-time data ingestion into the Elastic Stack.


## Setup


#### Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Dataset name | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).   |
| Listen Address | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | Bind address for the HTTP listener. Use 0.0.0.0 to listen on all interfaces.   |
| Listen port | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | Bind port for the listener.   |
| Ingest Pipeline | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The Ingest Node pipeline ID to be used by the integration.   |
| Preserve Original Event | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | This option copies the raw unmodified body of the incoming request to the event.original field as a string before sending the event to Elasticsearch.  |
| Tags | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Tags to include in the published event  |
| URL | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | This options specific which URL path to accept requests on. Defaults to /.  |

#### Advanced Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Basic Auth | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | Enables or disables HTTP basic auth for each incoming request. If enabled then username and password will also need to be configured.  |
| Content Type | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | By default the input expects the incoming POST to include a Content-Type of application/json to try to enforce the incoming data to be valid JSON. In certain scenarios when the source of the request is not able to do that, it can be overwritten with another value or set to null.  |
| Enable request tracing | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | The request tracer logs HTTP requests and responses to the agent's local file-system for debugging configurations. Enabling this request tracing compromises security and should only be used for debugging. See [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-cel.html#_resource_tracer_filename) for details.   |
| HMAC Header | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The name of the header that contains the HMAC signature, for example X-Dropbox-Signature, X-Hub-Signature-256, etc. HMAC signatures may be encoded as hex or base64 (raw or standard).  |
| HMAC Key | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | password | The secret key used to calculate the HMAC signature. Typically, the webhook sender provides this value.  |
| HMAC Prefix | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The prefix for the signature. Certain webhooks prefix the HMAC signature with a value, for example sha256=.  |
| HMAC Type | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The hash algorithm to use for the HMAC comparison. At this time the only valid values are sha256 or sha1.  |
| Include Headers | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | This options specifies a list of HTTP headers that should be copied from the incoming request and included in the document. All configured headers will always be canonicalized to match the headers of the incoming request. For example, ["content-type"] will become ["Content-Type"] when the filebeat is running.  |
| HTTP Method | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | select | This options specifies which HTTP method to accept.  |
| Password | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | password | If basic_auth is enabled, this is the password used for authentication against the HTTP listener. Requires username to also be set.  |
| Prefix | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | This option specifies which prefix field the incoming request will be mapped to. Care should be taken when setting this option in conjunction with the Preserve Original Event or the Include Headers options. These will collide the `event` and `headers` fields respecetively, so avoid using a prefix that would result in data being placed in those fields if those other options are used. If a collision occurs the behavior is unspecified.  |
| Processors | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | Processors are used to reduce the number of fields in the exported event or to enhance the event with metadata. This executes in the agent before the logs are parsed. See [Processors](https://www.elastic.co/guide/en/beats/filebeat/current/filtering-and-enhancing-data.html) for details.   |
| The CEL program to be run for each request. | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | textarea | Program is the CEL program that is executed each HTTP request to transform the request body data. More information can be found in the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-http_endpoint.html#_program).   |
| Response Body | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The response body returned upon success. Should be a single line JSON string.  |
| Response Code | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The HTTP response code returned upon success. Should be in the 2XX range.  |
| Secret Header | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The header to check for a specific value specified by secret.value. Certain webhooks provide the possibility to include a special header and secret to identify the source.  |
| Secret Value | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | password | The secret stored in the header name specified by secret.header. Certain webhooks provide the possibility to include a special header and secret to identify the source.  |
| TLS | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | Options for enabling TLS for the listening webhook endpoint. See the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/configuration-ssl.html) for a list of all options.  |
| Username | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | If basic_auth is enabled, this is the username used for authentication against the HTTP listener. Requires password to also be set.  |
