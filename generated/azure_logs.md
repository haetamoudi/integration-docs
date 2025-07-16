# Custom Azure Logs

The `azure_logs` input package for Elastic facilitates the collection of logs from various Azure services. It supports specialized integrations for services like Microsoft Entra ID (Sign-in, Audit, Identity Protection, Provisioning), Azure
Spring Apps, and Azure Firewall, as well as a generic integration for any Azure service. This input typically leverages Azure Event Hubs and Storage Accounts to ingest log data into Elasticsearch for analysis, visualization, and alerting
within Kibana. It helps users gain insights into their Azure environment for security, observability, and operational troubleshooting.


## Setup


#### Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Connection String | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | password | The connection string required to communicate with Event Hubs. See [Get an Event Hubs connection string](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-get-connection-string) to learn more.  |
| Consumer Group | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text |   |
| Dataset name | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | Dataset to write data to. Changing the dataset will send the data to a different index.  You can't use `-` in the name of a dataset and only valid characters for [Elasticsearch index names](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html).  |
| Event Hub Name | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | The event hub name that contains the logs to ingest. Do not use the event hub namespace here. Elastic recommends using one event hub for each integration. Visit [Create an event hub](https://docs.elastic.co/integrations/azure#create-an-event-hub) to learn more. Use event hub names up to 30 characters long to avoid compatibility issues.  |
| Ingest Pipeline | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The ingest pipeline ID to use for processing the data. If provided, replaces the default pipeline for this integration.  |
| Storage Account | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | The name of the storage account where the consumer group's state/offsets will be stored and updated.  |
| Storage Account Key | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | password | The storage account key, this key will be used to authorize access to data in your storage account.  |

#### Advanced Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Migrate checkpoint information | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | (Processor v2 only) Flag to control if the processor should perform  the checkpoint information migration from processor v1 to v2 at startup. The checkpoint migration converts the checkpoint information from the v1 format to the v2 format. Default is `false`, which means the processor will not perform the checkpoint migration.  |
| Partition receive count | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | (Processor v2 only) Maximum number of messages from the event hub to wait for before processing them. The partition consumer waits up to a "receive count" or a "receive timeout", whichever comes first. Default is `100` messages.  |
| Partition receive timeout | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | (Processor v2 only) Maximum time to wait before processing the messages received from the event hub. The partition consumer waits up to a "receive count" or a "receive timeout", whichever comes first. Default is `5` seconds.  |
| Processor start position | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | (Processor v2 only) Controls from what position in the event hub the processor should start processing messages for all partitions. Possible values are `earliest` and `latest`. `earliest` starts processing messages from the last checkpoint, or the beginning of the event hub if no checkpoint is available. `latest` starts processing messages from the the latest event in the event hub and continues to process new events as they arrive. Default is `earliest`.  |
| Processor update interval | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | (Processor v2 only) How often the processor should attempt to claim partitions. Default is `10` seconds.  |
| Processor version | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The processor version that the integration should use. Possible values are `v1` and `v2` (preview).  The v2 event hub processor is in preview, so using the v1 processor is recommended for typical use cases. Default is `v1`.  |
| Processors | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | Processors are used to reduce the number of fields in the exported event or to enhance the event with metadata. This runs in the agent before the logs are parsed. Check [Processors](https://www.elastic.co/guide/en/beats/filebeat/current/filtering-and-enhancing-data.html) for details.   |
| Resource Manager Endpoint | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The Azure Resource Manager endpoint to use for authentication.  |
| Sanitizes New Lines | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | Removes new lines in logs to ensure proper formatting of JSON data and avoid parsing issues during processing.   |
| Sanitizes Single Quotes | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | bool | Replaces single quotes with double quotes (single quotes inside double quotes are omitted) in logs to ensure proper formatting of JSON data and avoid parsing issues during processing.   |
| Storage Account Container | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The storage account container where the integration stores the checkpoint data for the event hub / consumer group. It is an advanced option to use with extreme care. If you are using the [processor_version](https://www.elastic.co/guide/en/integrations/current/azure_logs.html#azure_logs-event-hub-processor-options) v1 (default option), you MUST use a dedicated storage account container for each event hub / consumer group pair. For information about container name restrictions, please refer to the [Container Names](https://docs.microsoft.com/en-us/rest/api/storageservices/naming-and-referencing-containers--blobs--and-metadata#container-names) section in Microsoft's documentation. If you don't specify a container name, the integration will automatically generate a default one for you.  |
| Tags | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text |   |
