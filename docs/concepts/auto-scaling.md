# Auto Scaling

Auto scaling is when your service is configured to automatically increase or decrease the number of running instances based upon some metric. This can be based upon CPU usage, Memory, amount of traffic or other custom metrics.

## Why is it Important?

 - Handle sudden increases in traffic without manual operations
 - Doesn't require alerting on normal traffic increases (less impact on on-call members)
 - Cost efficient: save money by automatically scaling down when there is low traffic

## Tips and Tricks

 - [Capacity planning](./capacity-planning.md) is an essential pre-requisite for determining a good scaling configuration
 - There is a delay in autoscaling, if you can predict a sudden increase in traffic in advance you should still consider scaling for that manually (e.g. right before a major promotion)
 - Measure how long it takes to scale your service up, how much traffic each instance of your service should handle, and how much traffic you expect in normal operation. Based upon those, you can estimate at which point you should trigger a scaling event
 - Scaling values should be reviewed and modified over time to provide a good balance between stability and cost efficiency
 - Ideally your average CPU usage (`docker.cpu.usage` on Datadog) should be always the HPA target multiplied by the CPU request (e.g. if your CPU request is 500m and the HPA target is 65% then your CPU usage should always be around 325m)
 - For simple services that follow the [resource request/limit guidelines](resource-requests-and-limits.md) good HPA targets are unlikely to be outside the range 50% to 75%. 65% (i.e. ~2/3) is a good starting point.

## See Also

 - [Capacity Planning](./capacity-planning.md)
 - [Horizontal Pod Autoscaler Walkthrough](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/)
