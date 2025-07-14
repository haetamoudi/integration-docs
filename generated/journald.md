# Custom Journald logs

The `journald` input package for Elastic allows Filebeat to read and ingest log data directly from the systemd journal. This is particularly useful for Linux distributions that primarily use journald for system logging, providing access to
structured log data and associated metadata. It helps integrate system-level logs into the Elastic Stack for centralized analysis and monitoring.


## Setup

### Collecting logs from Custom Journald logs

#### Configuration Parameters

##### Condition
*Optional*

*type*: text

*description*: Condition to filter when to run this input. See [Dynamic Input Configuration](https://www.elastic.co/guide/en/fleet/current/dynamic-input-configuration.html) for details.
##### Include Matches
*Optional*

*type*: text

*description*: A list of filter expressions used to select the logs to read (e.g. `_SYSTEMD_UNIT=vault.service`). Defaults to all logs. See [include_matches](https://www.elastic.co/guide/en/beats/filebeat/7.x/filebeat-input-journald.html#filebeat-input-journald-include-matches) for details.


#### Advanced Parameters

#### Condition
*Optional*

*type*: text

*description*: Condition to filter when to run this input. See [Dynamic Input Configuration](https://www.elastic.co/guide/en/fleet/current/dynamic-input-configuration.html) for details.
#### Include Matches
*Optional*

*type*: text

*description*: A list of filter expressions used to select the logs to read (e.g. `_SYSTEMD_UNIT=vault.service`). Defaults to all logs. See [include_matches](https://www.elastic.co/guide/en/beats/filebeat/7.x/filebeat-input-journald.html#filebeat-input-journald-include-matches) for details.


