# Prometheus Input

The `prometheus_input` package for Elastic is designed to collect metrics from Prometheus Exporters (Collectors) and send them to the Elastic Stack. This input allows users to ingest time-series data exposed by various services that are
instrumented for Prometheus. It's a crucial component for unifying Prometheus-collected metrics with logs and traces within Elasticsearch, providing a comprehensive observability solution.


## Setup

### Collecting logs from Prometheus Input


#### Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Condition | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Condition to filter when to collect this input. See [Dynamic Input Configuration](https://www.elastic.co/guide/en/fleet/current/dynamic-input-configuration.html) for details.  |
| Datastream Dataset name | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | Name of Datastream dataset  |
| Hosts | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text |   |
| Leader Election | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | bool | Enable leaderelection between a set of Elastic Agents running on Kubernetes. See [Kubernetes LeaderElection Provider](https://www.elastic.co/guide/en/fleet/current/kubernetes_leaderelection-provider.html) for details.  |
| Password | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | password |   |
| Period | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text |   |
| Rate Counters | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | bool |   |
| Use Types | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | bool |   |
| Username | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text |   |

#### Advanced Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Metrics Filters Exclude | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text |   |
| Metrics Filters Include | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text |   |
| Processors | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | Processors are used to reduce the number of fields in the exported event or to enhance the event with metadata. This executes in the agent before the events are shipped. See [Processors](https://www.elastic.co/guide/en/fleet/current/elastic-agent-processor-configuration.html) for details.     |
| SSL Certificate Authorities | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | SSL Certificate Authorities. See [documentation](https://www.elastic.co/guide/en/beats/metricbeat/current/configuration-ssl.html#client-certificate-authorities) for details.  |

