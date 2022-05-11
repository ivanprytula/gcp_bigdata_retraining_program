# Elastic Storage with Google Cloud Storage

## Cloud Storage  bucket aka global durable "file system"

```shell
# CLI example
gsutil mb -p [PROJECT_NAME] -c [STORAGE_CLASS] -l [BUCKET_LOCATION] gs://[BUCKET_NAME]
```

## 4 storage classes for you (multi-regional / dual regional / regional location options, defer based on the access speed/cost):

- Standard storage (the fastest)

> Best for data that is **frequently accessed ("hot" data)** and/or **stored for only brief periods of time**

- Nearline storage

> A low-cost, highly durable storage service for data you plan to read or modify on average **once per month** or less.

- Coldline storage

> A very low-cost, highly durable storage service for data you plan to read or modify **at most once a quarter**.

- Archive storage (the least expensive)

> The lowest-cost, highly durable storage service for data archiving, online backup, and disaster recovery.

    Typical big data analytics workload run in Standard Storage within a region

