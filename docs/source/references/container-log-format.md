# Container Log Format

This reference shows you the recommended log format that your services should emit.

## Why this log format is required?

Various technologies and applications tend to use different log format in a Log Management environment. In other words, our microservices tend to use different attributes for the same meaning. For instance, a client IP might have the following attributes within your logs: `clientIP`, `client_ip_address`, `remote_address`, `client.ip`.

As same as [distributed tracing](../guides/configure-tracing.md), in microservices world, we often want to see logs **across multiple microservices**. In order to see logs across microservices, we need to correlate logs with something which is standardized log attribute such as request ID.

Also, following the format is important in order to fully leverage all of Datadog's functionalities. For instance, if every microservices use same `http.referer` attribute, we can create request count grouped by referer in specific time range across microservices.

## Format

The container log format is JSON, with a standardized structure and well-known fields. Please follow the format defined in [Datadog naming convention for log attributes](https://docs.datadoghq.com/logs/processing/attributes_naming_convention/).
