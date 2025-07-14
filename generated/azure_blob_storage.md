# Custom Azure Blob Storage Input

The `azure_blob_storage` input package for Elastic allows users to read content from files stored in Azure Blob Storage containers. It supports both one-time data ingestion and continuous polling for new or updated files. This input is
designed to be resilient, resuming processing from the last successfully handled file in case of outages and logging errors for individual files without halting the entire process. Currently, it supports JSON and NDJSON blob formats, which
can also be gzip compressed.


## Setup

### Collecting logs from Custom Azure Blob Storage Input

#### Configuration Parameters

##### Account Name
*Required*
*type*: text

*description*: This attribute is required for various internal operations with respect to authentication, creating service clients and blob clients which are used internally for various processing purposes.

##### Client ID (OAuth2)
*Optional*

*type*: text

*description*: Client ID of Azure Account. This is required if 'Collect logs using OAuth2 authentication' is enabled.
##### Client Secret (OAuth2)
*Optional*

*type*: password

*description*: Client Secret of Azure Account. This is required if 'Collect logs using OAuth2 authentication' is enabled.
##### Containers
*Required*
*type*: yaml

*description*: This attribute contains the details about a specific container like, name, number_of_workers, poll, poll_interval etc. The attribute 'name' is specific to a container as it describes the container name, while the fields number_of_workers, poll, poll_interval can exist both at the container level and at the global level.  If you have already defined the attributes globally, then you can only specify the container name in this yaml config. If you want to override any specific attribute for a container, then, you can define it here. Any attribute defined in the yaml will override the global definitions.  Please see the relevant [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-azure-blob-storage.html#attrib-containers) for further information.

##### Dataset name
*Required*
*type*: text

*description*: Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).

##### Maximum number of workers
*Optional*

*type*: integer

*description*: Determines how many workers are spawned per container.
##### Collect logs using OAuth2 authentication
*Required*
*type*: bool

*description*: To collect logs using OAuth2 authentication enable the toggle switch. By default, it will collect logs using service account key or URI.
##### Ingest Pipeline
*Optional*

*type*: text

*description*: The Ingest Node pipeline ID to be used by the integration.

##### Polling
*Optional*

*type*: bool

*description*: Determines if the container will be continuously polled for new documents.
##### Polling interval
*Optional*

*type*: text

*description*: Determines the time interval between polling operations.
##### Preserve original event
*Required*
*type*: bool

*description*: Preserves a raw copy of the original event, added to the field `event.original`
##### Service Account Key
*Optional*

*type*: password

*description*: This attribute contains the access key, found under the Access keys section on Azure Cloud, under the respective storage account. A single storage account can contain multiple containers, and they will all use this common access key.

##### Tags
*Optional*

*type*: text

*description*: Tags to include in the published event
##### Tenant ID (OAuth2)
*Optional*

*type*: text

*description*: Tenant ID of Azure Account. This is required if 'Collect logs using OAuth2 authentication' is enabled.

#### Advanced Parameters

#### Account Name
*Required*
*type*: text

*description*: This attribute is required for various internal operations with respect to authentication, creating service clients and blob clients which are used internally for various processing purposes.

#### Client ID (OAuth2)
*Optional*

*type*: text

*description*: Client ID of Azure Account. This is required if 'Collect logs using OAuth2 authentication' is enabled.
#### Client Secret (OAuth2)
*Optional*

*type*: password

*description*: Client Secret of Azure Account. This is required if 'Collect logs using OAuth2 authentication' is enabled.
#### Containers
*Required*
*type*: yaml

*description*: This attribute contains the details about a specific container like, name, number_of_workers, poll, poll_interval etc. The attribute 'name' is specific to a container as it describes the container name, while the fields number_of_workers, poll, poll_interval can exist both at the container level and at the global level.  If you have already defined the attributes globally, then you can only specify the container name in this yaml config. If you want to override any specific attribute for a container, then, you can define it here. Any attribute defined in the yaml will override the global definitions.  Please see the relevant [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-azure-blob-storage.html#attrib-containers) for further information.

#### Dataset name
*Required*
*type*: text

*description*: Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).

#### Maximum number of workers
*Optional*

*type*: integer

*description*: Determines how many workers are spawned per container.
#### Collect logs using OAuth2 authentication
*Required*
*type*: bool

*description*: To collect logs using OAuth2 authentication enable the toggle switch. By default, it will collect logs using service account key or URI.
#### Ingest Pipeline
*Optional*

*type*: text

*description*: The Ingest Node pipeline ID to be used by the integration.

#### Polling
*Optional*

*type*: bool

*description*: Determines if the container will be continuously polled for new documents.
#### Polling interval
*Optional*

*type*: text

*description*: Determines the time interval between polling operations.
#### Preserve original event
*Required*
*type*: bool

*description*: Preserves a raw copy of the original event, added to the field `event.original`
#### Service Account Key
*Optional*

*type*: password

*description*: This attribute contains the access key, found under the Access keys section on Azure Cloud, under the respective storage account. A single storage account can contain multiple containers, and they will all use this common access key.

#### Tags
*Optional*

*type*: text

*description*: Tags to include in the published event
#### Tenant ID (OAuth2)
*Optional*

*type*: text

*description*: Tenant ID of Azure Account. This is required if 'Collect logs using OAuth2 authentication' is enabled.

