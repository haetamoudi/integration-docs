# Prometheus Input

The `prometheus_input` package for Elastic is designed to collect metrics from Prometheus Exporters (Collectors) and send them to the Elastic Stack. This input allows users to ingest time-series data exposed by various services that are
instrumented for Prometheus. It's a crucial component for unifying Prometheus-collected metrics with logs and traces within Elasticsearch, providing a comprehensive observability solution.


## Setup

### Collecting logs from Prometheus Input

#### Configuration Parameters

##### Condition
*Optional*

*type*: text

*description*: Condition to filter when to collect this input. See [Dynamic Input Configuration](https://www.elastic.co/guide/en/fleet/current/dynamic-input-configuration.html) for details.
##### Datastream Dataset name
*Required*
*type*: text

*description*: Name of Datastream dataset
##### Hosts
*Required*
*type*: text

*description*: 
##### Leader Election
*Required*
*type*: bool

*description*: Enable leaderelection between a set of Elastic Agents running on Kubernetes. See [Kubernetes LeaderElection Provider](https://www.elastic.co/guide/en/fleet/current/kubernetes_leaderelection-provider.html) for details.
##### Password
*Optional*

*type*: password

*description*: 
##### Period
*Required*
*type*: text

*description*: 
##### Rate Counters
*Required*
*type*: bool

*description*: 
##### Use Types
*Required*
*type*: bool

*description*: 
##### Username
*Optional*

*type*: text

*description*: 

#### Advanced Parameters

#### Condition
*Optional*

*type*: text

*description*: Condition to filter when to collect this input. See [Dynamic Input Configuration](https://www.elastic.co/guide/en/fleet/current/dynamic-input-configuration.html) for details.
#### Datastream Dataset name
*Required*
*type*: text

*description*: Name of Datastream dataset
#### Hosts
*Required*
*type*: text

*description*: 
#### Leader Election
*Required*
*type*: bool

*description*: Enable leaderelection between a set of Elastic Agents running on Kubernetes. See [Kubernetes LeaderElection Provider](https://www.elastic.co/guide/en/fleet/current/kubernetes_leaderelection-provider.html) for details.
#### Password
*Optional*

*type*: password

*description*: 
#### Period
*Required*
*type*: text

*description*: 
#### Rate Counters
*Required*
*type*: bool

*description*: 
#### Use Types
*Required*
*type*: bool

*description*: 
#### Username
*Optional*

*type*: text

*description*: 

