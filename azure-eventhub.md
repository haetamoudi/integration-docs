## Setup

- You must have a subscription to Microsoft Azure.
- Elastic Agent must be installed. For more details, check the Elastic Agent [installation instructions](docs-content://reference/fleet/install-elastic-agents.md). You can install only one Elastic Agent per host. You can install only one Elastic Agent per host.
Elastic Agent is required to stream data from the **Azure Event Hub** and ship the data to Elastic, where the events will then be processed via the integration's ingest pipelines.

### Collecting logs from Azure Eventhub

To collect logs via Azure Event Hub, select **Collect logs via Azure Event Hub** and configure the following parameters:

- Eventhub: It is a fully managed, real-time data ingestion service. Elastic recommends using only letters, numbers, and the hyphen (-) character for Event Hub names to maximize compatibility. You can use existing Event Hubs having underscores (_) in the Event Hub name; in this case, the integration will replace underscores with hyphens (-) when it uses the Event Hub name to create dependent Azure resources behind the scenes (e.g., the storage account container to store Event Hub consumer offsets). Elastic also recommends using a separate event hub for each log type as the field mappings of each log type differ.
- Consumer group:  The publish/subscribe mechanism of Event Hubs is enabled through consumer groups. A consumer group is a view (state, position, or offset) of an entire event hub. Consumer groups enable multiple consuming applications to each have a separate view of the event stream, and to read the stream independently at their own pace and with their own offsets.
- Connection string: The connection string required to communicate with Event Hubs, steps here https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-get-connection-string.
- Storage account: The name of the storage account the state/offsets will be stored and updated.
- Storage account key: The storage account key, this key will be used to authorize access to data in your storage account.
