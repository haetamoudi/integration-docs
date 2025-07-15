# Custom GCS (Google Cloud Storage) Input

The `google_cloud_storage` input package for Elastic enables Logstash to read content from files stored in Google Cloud Storage (GCS) buckets. It allows for the ingestion of various data formats, such as CSV, JSON, and NDJSON, into
Elasticsearch. This input is crucial for use cases like importing Stackdriver logs, restoring data from Elastic dumps, or processing gzipped logs from cold storage within the Elastic Stack.


## Setup


#### Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Bucket Timeout | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Defines the maximum time that the sdk will wait for a bucket api response before timing out. Valid time units are ns, us, ms, s, m, h.  |
| Buckets | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | yaml | This attribute contains the details about a specific bucket like, name, number_of_workers, poll, poll_interval and bucket_timeout. The attribute 'name' is specific to a bucket as it describes the bucket name, while the fields number_of_workers, poll, poll_interval and bucket_timeout can exist both at the bucket level and at the global level. If you have already defined the attributes globally, then you can only specify the name in this yaml config. If you want to override any specific attribute for a specific bucket, then, you can define it here. Any attribute defined in the yaml will override the global definitions. Please see the relevant [Documentation](https://www.elastic.co/guide/en/beats/filebeat/8.5/filebeat-input-gcs.html#attrib-buckets) for further information.   |
| Dataset name | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).   |
| Maximum number of workers | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | integer | Determines how many workers are spawned per bucket.  |
| Ingest Pipeline | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The Ingest Node pipeline ID to be used by the integration.   |
| Polling | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | Determines if the bucket will be continuously polled for new documents.  |
| Polling interval | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Determines the time interval between polling operations.  |
| Preserve original event | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | bool | Preserves a raw copy of the original event, added to the field `event.original`  |
| Project ID | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | This attribute is required for various internal operations with respect to authentication, creating storage clients and logging which are used internally for various processing purposes.   |
| Service Account File | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | This attribute contains the service account credentials file, which can be generated from the google cloud console, ref [Service Account Keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys). Required if a Service Account Key is not provided.   |
| Service Account Key | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | password | This attribute contains the json service account credentials string, which can be generated from the google cloud console, ref[Service Account Keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys). Required if a Service Account File is not provided.   |
| Tags | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Tags to include in the published event  |

#### Advanced Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Alternative Host | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Used to override the default host for the storage client (default is storage.googleapis.com)  |
| File Selectors | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | If the GCS bucket will have events that correspond to files that this integration shouldn’t process, file_selectors can be used to limit the files that are downloaded. This is a list of selectors which is made up of regex patters. The regex should match the GCS bucket filepath. Regexes use [RE2 syntax](https://pkg.go.dev/regexp/syntax). Files that don’t match one of the regexes will not be processed.   |
| Processors | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | Processors are used to reduce the number of fields in the exported event or to enhance the event with metadata. This executes in the agent before the logs are parsed. See [Processors](https://www.elastic.co/guide/en/beats/filebeat/current/filtering-and-enhancing-data.html) for details.   |
| Timestamp Epoch | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | integer | Defines the epoch time in seconds, which is used to filter out objects/files that are older than the specified timestamp.  |
