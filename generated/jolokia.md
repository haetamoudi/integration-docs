# Jolokia Input

The `jolokia` input package for Elastic collects metrics from Jolokia agents, which act as a JMX-HTTP bridge. It allows Logstash or Metricbeat to retrieve Java Management Extensions (JMX) metrics over HTTP in JSON format. This input is vital
for monitoring Java applications, providing insights into their performance and health by exposing MBean attributes and operations to the Elastic Stack.


## Setup

### Collecting logs from Jolokia Input

#### Configuration Parameters

##### Hosts
*Required*
*type*: text

*description*: 
##### HTTP Method
*Required*
*type*: text

*description*: 
##### JMX Mappings
*Required*
*type*: yaml

*description*: 
##### Metrics Path
*Required*
*type*: text

*description*: 
##### Period
*Required*
*type*: text

*description*: 
##### SSL CA Trusted Fingerprint
*Optional*

*type*: text

*description*: SSL CA trusted fingerprint. See [documentation](https://www.elastic.co/guide/en/fleet/current/elastic-agent-ssl-configuration.html) for details.
##### SSL Certificate
*Optional*

*type*: text

*description*: SSL certificate. See [documentation](https://www.elastic.co/guide/en/fleet/current/elastic-agent-ssl-configuration.html) for details.
##### SSL Certificate Authorities
*Optional*

*type*: text

*description*: SSL certificate authorities.  See [documentation](https://www.elastic.co/guide/en/fleet/current/elastic-agent-ssl-configuration.html) for details.
##### SSL Private Key
*Optional*

*type*: text

*description*: SSL private key. See [documentation](https://www.elastic.co/guide/en/fleet/current/elastic-agent-ssl-configuration.html) for details.
##### SSL Key Passphrase
*Optional*

*type*: password

*description*: SSL key passphrase. See [documentation](https://www.elastic.co/guide/en/fleet/current/elastic-agent-ssl-configuration.html) for details.

#### Advanced Parameters

#### Hosts
*Required*
*type*: text

*description*: 
#### HTTP Method
*Required*
*type*: text

*description*: 
#### JMX Mappings
*Required*
*type*: yaml

*description*: 
#### Metrics Path
*Required*
*type*: text

*description*: 
#### Period
*Required*
*type*: text

*description*: 
#### SSL CA Trusted Fingerprint
*Optional*

*type*: text

*description*: SSL CA trusted fingerprint. See [documentation](https://www.elastic.co/guide/en/fleet/current/elastic-agent-ssl-configuration.html) for details.
#### SSL Certificate
*Optional*

*type*: text

*description*: SSL certificate. See [documentation](https://www.elastic.co/guide/en/fleet/current/elastic-agent-ssl-configuration.html) for details.
#### SSL Certificate Authorities
*Optional*

*type*: text

*description*: SSL certificate authorities.  See [documentation](https://www.elastic.co/guide/en/fleet/current/elastic-agent-ssl-configuration.html) for details.
#### SSL Private Key
*Optional*

*type*: text

*description*: SSL private key. See [documentation](https://www.elastic.co/guide/en/fleet/current/elastic-agent-ssl-configuration.html) for details.
#### SSL Key Passphrase
*Optional*

*type*: password

*description*: SSL key passphrase. See [documentation](https://www.elastic.co/guide/en/fleet/current/elastic-agent-ssl-configuration.html) for details.

