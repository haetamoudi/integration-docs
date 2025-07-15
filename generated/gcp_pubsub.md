# Custom Google Pub/Sub Logs

The `gcp_pubsub` input package for Elastic enables real-time data ingestion from Google Cloud Pub/Sub topics. It allows users to subscribe to a Pub/Sub topic and pull messages, making it ideal for collecting various event-driven data like
Stackdriver logs. This input is designed for continuous processing, handling credentials and message acknowledgment to ensure reliable data flow into Elasticsearch for analysis.


## Setup


#### Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Credentials File | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Path to a JSON file containing the credentials and key used to subscribe.  |
| Credentials JSON | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | password | JSON blob containing the credentials and key used to subscribe.  |
| Dataset name | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).   |
| Ingest Pipeline | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The Ingest Node pipeline ID to be used by the integration.   |
| Project ID | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text |   |
| Subscription Create | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | If true, the integration will create the subscription on start.  |
| Subscription Name | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text |   |
| Topic | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text |   |

#### Advanced Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Alternative host | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text |   |
| Processors | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | Processors are used to reduce the number of fields in the exported event or to enhance the event with metadata. This executes in the agent before the logs are parsed. See [Processors](https://www.elastic.co/guide/en/beats/filebeat/current/filtering-and-enhancing-data.html) for details.   |
| Subscription Max Outstanding Messages | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The maximum number of unprocessed messages (unacknowledged but not yet expired). If the value is negative, then there will be no limit on the number of unprocessed messages. Default is 1000.  |
| Subscription Num Goroutines | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Number of goroutines created to read from the subscription. This does not limit the number of messages that can be processed concurrently or the maximum number of goroutines the input will create.  |
| Tags | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text |   |
