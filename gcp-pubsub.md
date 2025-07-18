## Setup

For more details about the GCS Pub/Sub input settings, check the [Filebeat documentation](https://www.elastic.co/docs/reference/beats/filebeat/filebeat-input-gcs-pubsub).

1. [Create Topic for Pub/sub](https://cloud.google.com/pubsub/docs/create-topic#create_a_topic).
2. [Create Subscription for topic](https://cloud.google.com/pubsub/docs/create-subscription#create_subscriptions)

### Collecting logs from GCP Pub/Sub

To collect logs via GCP Pub/Sub, select **Collect logs via GCP Pub/Sub** and configure the following parameters:

- Project ID
- Subscription Name
- Topic
- Credentials File: Path to a JSON file containing the credentials and key used to subscribe.
- Credentials JSON: JSON blob containing the credentials and key used to subscribe.