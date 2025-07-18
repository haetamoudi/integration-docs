## Setup

Set up a [CloudWatch Logs](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html#setup-cloudwatch-logs-destination) destination.

To access aws-cloudwatch, these [specific AWS permissions](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-aws-cloudwatch.html#_aws_permissions) are required.

### Collecting logs from CloudWatch

When collecting logs from CloudWatch is enabled, users can retrieve logs from
all log streams in a specific log group. `filterLogEvents` AWS API is used to
list log events from the specified log group. Amazon CloudWatch Logs can be used
to store log files from Amazon Elastic Compute Cloud(EC2), AWS CloudTrail,
Route53, and other sources.
 
To collect logs via CloudWatch, select **Collect logs via CloudWatch** and configure the following parameters:

- Access Key ID
- Secret Access Key
- Bucket ARN or Access Point ARN
- Session Token