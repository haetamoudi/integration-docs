# GCP Metrics Input

The `gcp_metrics` input package for Elastic is designed to collect custom metrics from any Google Cloud Platform (GCP) service. It integrates with the GCP Cloud Monitoring API to gather a wide range of performance and operational data. This
allows users to monitor the health and performance of their GCP resources within Elastic, providing insights into various services like Compute Engine and Firestore. It's important to note that this package primarily focuses on metric
collection and typically requires custom ingest pipelines for pre-ingest data processing.


## Setup

### Collecting logs from GCP Metrics Input

#### Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Credentials File | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text |   |
| Credentials Json | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text |   |
| Exclude Labels | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | bool | Exclude additional labels from metrics  |
| GCP Metrics | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text |   |
| Project Id | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text |   |
| GCP Regions | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text |   |
| GCP Service | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text |   |
| GCP Zone | ![Optional](https://img.shields.io/badge/✘-fed10c?style=flat) | text |   |

#### Advanced Configuration Parameters

| Parameter |  Required | Type | Description |
| --- | --- | --- | --- |
| Period | ![Required](https://img.shields.io/badge/✔-93c93e?style=flat) | text |   |

