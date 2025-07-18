## Setup
For more details about the Azure Blob Storage input settings, check the [Filebeat documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-azure-blob-storage.html).

### Collecting logs from Azure Blob Storage

To collect logs via Azure Blob Storage, select **Collect logs via Azure Blob Storage** and configure the following parameters:
For OAuth2, toggle on **Collect logs using OAuth2 authentication**

- Account Name: This attribute is required for various internal operations with respect to authentication, creating service clients and blob clients which are used internally for various processing purposes.
- Client ID (OAuth2): Client ID of Azure Account. This is required if 'Collect logs using OAuth2 authentication' is enabled.
- Client Secret (OAuth2): Client Secret of Azure Account. This is required if 'Collect logs using OAuth2 authentication' is enabled.
- Dataset name: Dataset to write data to. Changing the dataset will send the data to a different index. You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).
- Containers: This attribute contains the details about a specific container like, name, number_of_workers, poll, poll_interval etc. The attribute 'name' is specific to a container as it describes the container name, while the fields number_of_workers, poll, poll_interval can exist both at the container level and at the global level.  If you have already defined the attributes globally, then you can only specify the container name in this yaml config. If you want to override any specific attribute for a container, then, you can define it here. Any attribute defined in the yaml will override the global definitions.  Please see the relevant [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-azure-blob-storage.html#attrib-containers) for further information.

