## Setup

For more details about the GCS Pub/Sub input settings, check the [Filebeat documentation](https://www.elastic.co/docs/reference/beats/filebeat/filebeat-input-gcs-pubsub).

1. [Create Topic for Pub/sub](https://cloud.google.com/pubsub/docs/create-topic#create_a_topic).
2. [Create Subscription for topic](https://cloud.google.com/pubsub/docs/create-subscription#create_subscriptions)

### Collecting logs from GCP Pub/Sub

To collect logs via GCP Pub/Sub, select **Collect logs via GCP Pub/Sub** and configure the following parameters:

##### Project ID
*type*: text

*description*: 

##### Subscription Name
*type*: text

*description*: 

##### Topic
*type*: text

*description*: 

#### Credentials File
*type*: text

*description*: Path to a JSON file containing the credentials and key used to subscribe.

#### Credentials JSON
*type*: password

*description*: JSON blob containing the credentials and key used to subscribe.