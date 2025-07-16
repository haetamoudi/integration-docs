# SQL Input

The `sql` input package for Elastic enables Logstash or Metricbeat to execute custom SQL queries against various relational databases. It retrieves the results of these queries and ingests them as structured events into Elasticsearch. This
input is highly flexible, supporting multiple database drivers (e.g., MySQL, PostgreSQL, Oracle, MSSQL) and allowing users to define specific SQL statements for pulling custom metrics or data.


## Setup


#### Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Driver | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text |   |
| Hosts | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | password |   |
| SQL Queries | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | yaml |   |

#### Advanced Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Condition | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Condition to filter when to apply this datastream. Refer to [Conditions](https://www.elastic.co/guide/en/fleet/current/dynamic-input-configuration.html#conditions) on how to use the available keys in conditions.  |
| Merge Results | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | Merge results from multiple queries to a single event (restrictions apply)  |
| Period | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text |   |
| Processors | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | Processors are used to reduce the number of fields in the exported event or to enhance the event with metadata. This executes in the agent before the events are shipped. See [Processors](https://www.elastic.co/guide/en/fleet/current/elastic-agent-processor-configuration.html) for details.  |
| SSL Configuration | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | SSL configuration options. See [documentation](https://www.elastic.co/docs/reference/integrations/sql) for details.  |
