# Jolokia Input

The `jolokia` input package for Elastic collects metrics from Jolokia agents, which act as a JMX-HTTP bridge. It allows Logstash or Metricbeat to retrieve Java Management Extensions (JMX) metrics over HTTP in JSON format. This input is vital
for monitoring Java applications, providing insights into their performance and health by exposing MBean attributes and operations to the Elastic Stack.


## Setup


#### Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Hosts | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text |   |
| HTTP Method | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text |   |
| JMX Mappings | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | yaml |   |
| Metrics Path | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text |   |
| Period | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text |   |
| SSL CA Trusted Fingerprint | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | SSL CA trusted fingerprint. See [documentation](https://www.elastic.co/guide/en/fleet/current/elastic-agent-ssl-configuration.html) for details.  |
| SSL Certificate | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | SSL certificate. See [documentation](https://www.elastic.co/guide/en/fleet/current/elastic-agent-ssl-configuration.html) for details.  |
| SSL Certificate Authorities | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | SSL certificate authorities.  See [documentation](https://www.elastic.co/guide/en/fleet/current/elastic-agent-ssl-configuration.html) for details.  |
| SSL Private Key | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | SSL private key. See [documentation](https://www.elastic.co/guide/en/fleet/current/elastic-agent-ssl-configuration.html) for details.  |
| SSL Key Passphrase | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | password | SSL key passphrase. See [documentation](https://www.elastic.co/guide/en/fleet/current/elastic-agent-ssl-configuration.html) for details.  |

#### Advanced Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| HTTP config options: bearer_token_file | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | If defined, the contents of the file will be read once at initialization and then the value will be used in an HTTP Authorization header.  |
| HTTP config options: connect_timeout | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Total time limit for an HTTP connection to be completed (Default 2 seconds)  |
| HTTP config options: headers | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | A list of headers to use with the HTTP request  |
| HTTP config options: Password | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | password | The password to use for basic authentication.  |
| Processors | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | Processors are used to reduce the number of fields in the exported event or to enhance the event with metadata. This executes in the agent before the events are shipped. See [Processors](https://www.elastic.co/guide/en/fleet/current/elastic-agent-processor-configuration.html) for details.   |
| SSL Verification Mode | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | SSL verification mode. See [documentation](https://www.elastic.co/guide/en/fleet/current/elastic-agent-ssl-configuration.html) for details.  |
| HTTP config options: timeout | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Total time limit for HTTP requests made by the module (Default 10 seconds)  |
| HTTP config options: Username | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The username to use for basic authentication.  |
