# Custom macOS Unified Logs

The `unifiedlogs` input package for Elastic is specifically designed to collect log data from Apple's Unified Logging System, found on macOS, iOS, watchOS, and tvOS. Unlike traditional text-based logs, Unified Logs centralize telemetry
in memory and on disk. This input allows Filebeat to stream these structured events, including details like process ID, thread ID, and log message, providing comprehensive insights into Apple ecosystem devices within the Elastic Stack.


## Setup

### Collecting logs from Custom macOS Unified Logs

#### Configuration Parameters

##### Must backfill
*Optional*

*type*: bool

*description*: If set to true the input will process all available logs since the beginning
of time the first time it starts.

##### Include backtrace
*Optional*

*type*: bool

*description*: Disable or enable backtrace level messages.

##### Include debug
*Optional*

*type*: bool

*description*: Disable or enable debug level messages.

##### End date
*Optional*

*type*: text

*description*: Shows content up to the provided date.
The following date/time formats are accepted:
`YYYY-MM-DD`, `YYYY-MM-DD HH:MM:SS`, `YYYY-MM-DD HH:MM:SSZZZZZ`.

##### Include info
*Optional*

*type*: bool

*description*: Disable or enable info level messages.

##### Use mach continuous time
*Optional*

*type*: bool

*description*: Use mach continuous time timestamps rather than walltime.

##### Ingest Pipeline
*Optional*

*type*: text

*description*: The Ingest Node pipeline ID to be used by the integration.

##### Predicate
*Optional*

*type*: text

*description*: Filters messages using the provided predicate based on NSPredicate.
A compound predicate or multiple predicates can be provided as a list.

For detailed information on the use of predicate based filtering,
please refer to the https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/Predicates/Articles/pSyntax.html[Predicate Programming Guide].

##### Process
*Optional*

*type*: text

*description*: A list of the processes on which to operate. It accepts a PID or process name.

##### Include signpost
*Optional*

*type*: bool

*description*: Disable or enable signpost level messages.

##### Include source
*Optional*

*type*: bool

*description*: Include symbol names and source line numbers for messages, if available.

##### Start date
*Optional*

*type*: text

*description*: Shows content starting from the provided date.
The following date/time formats are accepted:
`YYYY-MM-DD`, `YYYY-MM-DD HH:MM:SS`, `YYYY-MM-DD HH:MM:SSZZZZZ`.

##### Annotate unreliable
*Optional*

*type*: bool

*description*: Annotate events with whether the log was emitted unreliably.


#### Advanced Parameters

#### Must backfill
*Optional*

*type*: bool

*description*: If set to true the input will process all available logs since the beginning
of time the first time it starts.

#### Include backtrace
*Optional*

*type*: bool

*description*: Disable or enable backtrace level messages.

#### Include debug
*Optional*

*type*: bool

*description*: Disable or enable debug level messages.

#### End date
*Optional*

*type*: text

*description*: Shows content up to the provided date.
The following date/time formats are accepted:
`YYYY-MM-DD`, `YYYY-MM-DD HH:MM:SS`, `YYYY-MM-DD HH:MM:SSZZZZZ`.

#### Include info
*Optional*

*type*: bool

*description*: Disable or enable info level messages.

#### Use mach continuous time
*Optional*

*type*: bool

*description*: Use mach continuous time timestamps rather than walltime.

#### Ingest Pipeline
*Optional*

*type*: text

*description*: The Ingest Node pipeline ID to be used by the integration.

#### Predicate
*Optional*

*type*: text

*description*: Filters messages using the provided predicate based on NSPredicate.
A compound predicate or multiple predicates can be provided as a list.

For detailed information on the use of predicate based filtering,
please refer to the https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/Predicates/Articles/pSyntax.html[Predicate Programming Guide].

#### Process
*Optional*

*type*: text

*description*: A list of the processes on which to operate. It accepts a PID or process name.

#### Include signpost
*Optional*

*type*: bool

*description*: Disable or enable signpost level messages.

#### Include source
*Optional*

*type*: bool

*description*: Include symbol names and source line numbers for messages, if available.

#### Start date
*Optional*

*type*: text

*description*: Shows content starting from the provided date.
The following date/time formats are accepted:
`YYYY-MM-DD`, `YYYY-MM-DD HH:MM:SS`, `YYYY-MM-DD HH:MM:SSZZZZZ`.

#### Annotate unreliable
*Optional*

*type*: bool

*description*: Annotate events with whether the log was emitted unreliably.


