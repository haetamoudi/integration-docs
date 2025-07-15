## Setup

- You must have a subscription to Microsoft Azure.
- Elastic Agent must be installed. For more details, check the Elastic Agent [installation instructions](docs-content://reference/fleet/install-elastic-agents.md). You can install only one Elastic Agent per host. You can install only one Elastic Agent per host.
Elastic Agent is required to stream data from the **Azure Event Hub** and ship the data to Elastic, where the events will then be processed via the integration's ingest pipelines.

### Collecting logs from Azure Eventhub

While adding the integration, to collect logs via **Azure Event Hub**, enter the following details:
   - eventhub
   - consumer_group
   - connection_string
   - storage_account
   - storage_account_key
   - storage_account_container (optional)
   - resource_manager_endpoint (optional)