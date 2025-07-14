# Custom GCS (Google Cloud Storage) Input

The `google_cloud_storage` input package for Elastic enables Logstash to read content from files stored in Google Cloud Storage (GCS) buckets. It allows for the ingestion of various data formats, such as CSV, JSON, and NDJSON, into
Elasticsearch. This input is crucial for use cases like importing Stackdriver logs, restoring data from Elastic dumps, or processing gzipped logs from cold storage within the Elastic Stack.


## Setup

### Collecting logs from Custom GCS (Google Cloud Storage) Input

#### Configuration Parameters

##### Bucket Timeout
*Optional*

*type*: text

*description*: Defines the maximum time that the sdk will wait for a bucket api response before timing out. Valid time units are ns, us, ms, s, m, h.
##### Buckets
*Required*
*type*: yaml

*description*: This attribute contains the details about a specific bucket like, name, number_of_workers, poll, poll_interval and bucket_timeout. The attribute 'name' is specific to a bucket as it describes the bucket name, while the fields number_of_workers, poll, poll_interval and bucket_timeout can exist both at the bucket level and at the global level. If you have already defined the attributes globally, then you can only specify the name in this yaml config. If you want to override any specific attribute for a specific bucket, then, you can define it here. Any attribute defined in the yaml will override the global definitions. Please see the relevant [Documentation](https://www.elastic.co/guide/en/beats/filebeat/8.5/filebeat-input-gcs.html#attrib-buckets) for further information.

##### Dataset name
*Required*
*type*: text

*description*: Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).

##### Maximum number of workers
*Optional*

*type*: integer

*description*: Determines how many workers are spawned per bucket.
##### Ingest Pipeline
*Optional*

*type*: text

*description*: The Ingest Node pipeline ID to be used by the integration.

##### Polling
*Optional*

*type*: bool

*description*: Determines if the bucket will be continuously polled for new documents.
##### Polling interval
*Optional*

*type*: text

*description*: Determines the time interval between polling operations.
##### Preserve original event
*Required*
*type*: bool

*description*: Preserves a raw copy of the original event, added to the field `event.original`
##### Project ID
*Required*
*type*: text

*description*: This attribute is required for various internal operations with respect to authentication, creating storage clients and logging which are used internally for various processing purposes.

##### Service Account File
*Optional*

*type*: text

*description*: This attribute contains the service account credentials file, which can be generated from the google cloud console, ref [Service Account Keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys).
Required if a Service Account Key is not provided.

##### Service Account Key
*Optional*

*type*: password

*description*: This attribute contains the json service account credentials string, which can be generated from the google cloud console, ref[Service Account Keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys).
Required if a Service Account File is not provided.

##### Tags
*Optional*

*type*: text

*description*: Tags to include in the published event

#### Advanced Parameters

#### Bucket Timeout
*Optional*

*type*: text

*description*: Defines the maximum time that the sdk will wait for a bucket api response before timing out. Valid time units are ns, us, ms, s, m, h.
#### Buckets
*Required*
*type*: yaml

*description*: This attribute contains the details about a specific bucket like, name, number_of_workers, poll, poll_interval and bucket_timeout. The attribute 'name' is specific to a bucket as it describes the bucket name, while the fields number_of_workers, poll, poll_interval and bucket_timeout can exist both at the bucket level and at the global level. If you have already defined the attributes globally, then you can only specify the name in this yaml config. If you want to override any specific attribute for a specific bucket, then, you can define it here. Any attribute defined in the yaml will override the global definitions. Please see the relevant [Documentation](https://www.elastic.co/guide/en/beats/filebeat/8.5/filebeat-input-gcs.html#attrib-buckets) for further information.

#### Dataset name
*Required*
*type*: text

*description*: Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).

#### Maximum number of workers
*Optional*

*type*: integer

*description*: Determines how many workers are spawned per bucket.
#### Ingest Pipeline
*Optional*

*type*: text

*description*: The Ingest Node pipeline ID to be used by the integration.

#### Polling
*Optional*

*type*: bool

*description*: Determines if the bucket will be continuously polled for new documents.
#### Polling interval
*Optional*

*type*: text

*description*: Determines the time interval between polling operations.
#### Preserve original event
*Required*
*type*: bool

*description*: Preserves a raw copy of the original event, added to the field `event.original`
#### Project ID
*Required*
*type*: text

*description*: This attribute is required for various internal operations with respect to authentication, creating storage clients and logging which are used internally for various processing purposes.

#### Service Account File
*Optional*

*type*: text

*description*: This attribute contains the service account credentials file, which can be generated from the google cloud console, ref [Service Account Keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys).
Required if a Service Account Key is not provided.

#### Service Account Key
*Optional*

*type*: password

*description*: This attribute contains the json service account credentials string, which can be generated from the google cloud console, ref[Service Account Keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys).
Required if a Service Account File is not provided.

#### Tags
*Optional*

*type*: text

*description*: Tags to include in the published event

