# Custom macOS Unified Logs

The `unifiedlogs` input package for Elastic is specifically designed to collect log data from Apple's Unified Logging System, found on macOS, iOS, watchOS, and tvOS. Unlike traditional text-based logs, Unified Logs centralize telemetry
in memory and on disk. This input allows Filebeat to stream these structured events, including details like process ID, thread ID, and log message, providing comprehensive insights into Apple ecosystem devices within the Elastic Stack.


## Setup

### Collecting logs from Custom macOS Unified Logs


#### Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Must backfill | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | If set to true the input will process all available logs since the beginning of time the first time it starts.   |
| Include backtrace | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | Disable or enable backtrace level messages.   |
| Include debug | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | Disable or enable debug level messages.   |
| End date | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Shows content up to the provided date. The following date/time formats are accepted: `YYYY-MM-DD`, `YYYY-MM-DD HH:MM:SS`, `YYYY-MM-DD HH:MM:SSZZZZZ`.   |
| Include info | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | Disable or enable info level messages.   |
| Use mach continuous time | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | Use mach continuous time timestamps rather than walltime.   |
| Ingest Pipeline | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | The Ingest Node pipeline ID to be used by the integration.   |
| Predicate | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Filters messages using the provided predicate based on NSPredicate. A compound predicate or multiple predicates can be provided as a list.  For detailed information on the use of predicate based filtering, please refer to the https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/Predicates/Articles/pSyntax.html[Predicate Programming Guide].   |
| Process | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | A list of the processes on which to operate. It accepts a PID or process name.   |
| Include signpost | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | Disable or enable signpost level messages.   |
| Include source | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | Include symbol names and source line numbers for messages, if available.   |
| Start date | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Shows content starting from the provided date. The following date/time formats are accepted: `YYYY-MM-DD`, `YYYY-MM-DD HH:MM:SS`, `YYYY-MM-DD HH:MM:SSZZZZZ`.   |
| Annotate unreliable | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | Annotate events with whether the log was emitted unreliably.   |

#### Advanced Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Archive file | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Display events stored in the given archive. The archive must be a valid log archive bundle with the suffix `.logarchive`.   |
| Custom Configurations | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | yaml | YAML configuration options for the input. Be careful, this may break the integration.  |
| Tags | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Tags to include in the published event  |
| Trace file | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text | Display events stored in the given `.tracev3` file. In order to be decoded, the file must be contained within a valid `.logarchive`   |

