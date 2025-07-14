# StatsD Input

The `statsd_input` package for Elastic creates a UDP server that listens for metrics in the StatsD format. This allows Logstash or Elastic Agent to collect application-specific metrics like counters, gauges, and timers, emitted by various
services. It's a key component for gathering custom performance data and integrating it into the Elastic Stack for real-time monitoring and analysis.


## Setup

### Collecting logs from StatsD Input

#### Configuration Parameters

##### Listen Address
*Required*
*type*: text

*description*: Bind address for the listener. Use 0.0.0.0 to listen on all interfaces.

##### Listen Port
*Required*
*type*: text

*description*: Bind port for the listener.


#### Advanced Parameters

#### Listen Address
*Required*
*type*: text

*description*: Bind address for the listener. Use 0.0.0.0 to listen on all interfaces.

#### Listen Port
*Required*
*type*: text

*description*: Bind port for the listener.


