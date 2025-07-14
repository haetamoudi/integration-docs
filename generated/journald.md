# Custom Journald logs

The `journald` input package for Elastic allows Filebeat to read and ingest log data directly from the systemd journal. This is particularly useful for Linux distributions that primarily use journald for system logging, providing access to
structured log data and associated metadata. It helps integrate system-level logs into the Elastic Stack for centralized analysis and monitoring.


## Setup

### Collecting logs from Custom Journald logs


#### Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Condition | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Condition to filter when to run this input. See [Dynamic Input Configuration](https://www.elastic.co/guide/en/fleet/current/dynamic-input-configuration.html) for details.  |
| Include Matches | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | A list of filter expressions used to select the logs to read (e.g. `_SYSTEMD_UNIT=vault.service`). Defaults to all logs. See [include_matches](https://www.elastic.co/guide/en/beats/filebeat/7.x/filebeat-input-journald.html#filebeat-input-journald-include-matches) for details.   |

#### Advanced Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Journal paths | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | List of journals to read from. Defaults to the system journal.   |
| Processors | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | Processors are used to reduce the number of fields in the exported event or to enhance the event with metadata.  This executes in the agent before the logs are parsed. See [Processors](https://www.elastic.co/guide/en/beats/filebeat/current/filtering-and-enhancing-data.html) for details.   |
| Tags | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text | Tags to include in the published event.   |

