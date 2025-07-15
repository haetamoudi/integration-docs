# Custom API using Common Expression Language

The `cel` input package for Elastic allows for highly customizable data ingestion from various sources, including HTTP APIs and local file systems. It leverages the Common Expression Language (CEL) to define a program that both fetches and
processes data. This enables advanced users to create flexible data collection pipelines, handling tasks like making HTTP requests, parsing diverse payloads, and maintaining state for continuous collection.


## Setup


#### Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Dataset name | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).   |
| Delete redacted fields | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | bool | The default behavior for field redaction is to replace characters with `*`s. If field value length or presence will leak information, the fields can be deleted from logging by setting this configuration to true.   |
| Digest No Challenge Reuse | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | Selecting no challenge reuse prevents the transport from reusing digest challenges  |
| Digest Auth Password | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | password | The password to be used with Digest Auth headers  |
| Digest Auth Username | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The username to be used with Digest Auth headers  |
| OAuth2 Client ID | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Client ID used for OAuth2 authentication  |
| OAuth2 Client Secret | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | password | Client secret used for OAuth2 authentication  |
| OAuth2 Token URL | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The URL endpoint that will be used to generate the tokens during the oAuth2 flow. It is required if no oauth_custom variable is set or provider is not specified in oauth_custom variable.  |
| Basic Auth Password | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | password | The password to be used with Basic Auth headers  |
| Ingest Pipeline | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The Ingest Node pipeline ID to be used by the integration.   |
| The CEL program to be run for each polling. | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | textarea | Program is the CEL program that is executed each polling period to get and transform the API data. More information can be found in the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-cel.html#_execution).   |
| Redacted fields | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Fields to redact in debug logs. When logging at debug-level the input state and CEL evaluation state are included in logs. This may leak secrets, so list sensitive state fields in this configuration.   |
| Defined Regular Expressions | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | Regexps is the set of regular expression to be made available to the program by name. The syntax used is [RE2](https://github.com/google/re2/wiki/Syntax). More information can be found in the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-cel.html#regexp-cel).   |
| Resource Interval | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | How often the API is polled, supports seconds, minutes and hours.  |
| Resource URL | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | i.e. scheme://host:port/path  |
| Initial CEL evaluation state | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | State is the initial state to be provided to the program. If it has a cursor field, that field will be overwritten by any stored cursor, but will be available if no stored cursor exists. More information can be found in the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-cel.html#input-state-cel).   |
| Basic Auth Username | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The username to be used with Basic Auth headers  |

#### Advanced Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Allowed environment variables | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The CEL program may access environment variables via the `env` global. This lists the environment variables that are made available to the program during evaluation. See the [`allowed_environment` documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-cel.html#environ-cel) for details.   |
| Condition | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Condition to filter when to collect this input. See [Dynamic Input Configuration](https://www.elastic.co/guide/en/fleet/current/dynamic-input-configuration.html) for details.   |
| Enable request tracing | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | The request tracer logs HTTP requests and responses to the agent's local file-system for debugging configurations. Enabling this request tracing compromises security and should only be used for debugging. See [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-cel.html#_resource_tracer_filename) for details.   |
| OAuth2 Azure Resource | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Optional setting for the accessed WebAPI resource when using azure provider.  |
| OAuth2 Azure Tenant ID | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Optional setting used for authentication when using Azure provider. Since it is used in the process to generate the token_url, it can’t be used in combination with it.  |
| OAuth2 Endpoint Params | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | Set of values that will be sent on each resource to the token_url. Each param key can have multiple values. Can be set for all providers except google.  |
| OAuth2 Google Credentials File | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The full path to the credentials file for Google.  |
| OAuth2 Google Credentials JSON | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Your Google credentials information as raw JSON.  |
| OAuth2 Google Delegated account | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Email of the delegated account used to create the credentials (usually an admin).  |
| OAuth2 Google JWT File | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Full path to the JWT Account Key file for Google.  |
| OAuth2 Google JWT JSON | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Your Google JWT information as raw JSON.  |
| OAuth2 Okta JWT File | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Full path to the JWT account private key file for Okta.  |
| OAuth2 Okta JWT JSON | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Your Okta JWT private key as raw JSON.  |
| OAuth2 Okta JWT PEM | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Your Okta JWT private key encoded as a PEM block.  |
| OAuth2 Provider | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Used to configure supported oAuth2 providers. Each supported provider will require specific settings. It is not set by default. Supported providers are "azure" and "google".  |
| OAuth2 Scopes | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | A list of scopes that will be resourceed during the oAuth2 flow. It is optional for all providers.  |
| Processors | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | Processors are used to reduce the number of fields in the exported event or to enhance the event with metadata. This executes in the agent before the logs are parsed. See [Processors](https://www.elastic.co/guide/en/beats/filebeat/current/filtering-and-enhancing-data.html) for details.   |
| Resource Proxy | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | This specifies proxy configuration in the form of `http[s]://<user>:<password>@<server name/ip>:<port>`.  |
| Resource Rate Limit Burst | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The maximum burst size. Burst is the maximum number of resource requests that can be made above the overall rate limit.  |
| Resource Rate Limit | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The value of the response that specifies the total limit.  |
| Resource Redirect Forward Headers | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | When set to true resource headers are forwarded in case of a redirect. Default is "false".  |
| Resource Redirect Headers Ban List | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | When Redirect Forward Headers is set to true, all headers except the ones defined in this list will be forwarded. All headers are forwarded by default.  |
| Resource Redirect Max Redirects | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The maximum number of redirects to follow for a resource. Default is "10".  |
| Resource Retry Max Attempts | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The maximum number of retries for the HTTP client. Default is "5".  |
| Resource Retry Wait Max | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The maximum time to wait before a retry is attempted. Default is "60s".  |
| Resource Retry Wait Min | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The minimum time to wait before a retry is attempted. Default is "1s".  |
| Resource SSL Configuration | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | i.e. certificate_authorities, supported_protocols, verification_mode etc, more examples found in the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/configuration-ssl.html#ssl-common-config)  |
| Resource Timeout | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Duration before declaring that the HTTP client connection has timed out. Valid time units are ns, us, ms, s, m, h. Default is "30"s.  |
| Tags | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text |   |
| XML Schema Definitions (XSD) for XML documents. | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | textarea | The XSD needed for correct parsing and ingestion of XML documents using decode_xml CEL extension. More information can be found in the [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-cel.html#xsd-cel).   |
