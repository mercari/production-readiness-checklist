# Resource Requests and Limits

Resource Requests and Limits are a feature of Kubernetes Pods. They are used to help Kubernetes decide where pods can and should be deployed. There are two resources supported by Kubernetes, CPU and memory.

 - Requests: Reserved amount of a resource for a pod.
   - For example, if you `request` 1 CPU core then your pod will be allocated to a Kubernetes Node where there is at least 1 CPU core available.
 - Limits: The maximum amount of a resource a Pod will be allowed to use.
   - For example, if you `limit` your Pod's memory to 1GB and then try to use more than 1GB, Kubernetes will tell your Pod that it is out of memory.

## Why are they important?

 - To ensure your pods have enough resources to do their job
 - To ensure other pods do not affect your pod by using up resources you need
 - To ensure our Kubernetes cluster has enough Nodes to support our services
 - To ensure our Kubernetes cluster doesn't have too many nodes, which would waste our budget

## Tips and Tricks

### Measuring CPU and Memory Usage

- Try to measure how much CPU and Memory your service will use in production. During a load test is a good time to measure CPU and memory usage!
- Don't set very low limits or requests before the first deployment to production, it is better to lower the limits and requests after you know how much you really need.

If you are running your service in a Docker container locally, you can see current resource usage with: `docker stats`.
If you are running your service in Kubernetes (e.g. in Dev), you can see current resource usage with: `kubectl top pod -n ${NAMESPACE}`.

In addition to CPU usage, you should also monitor CPU throttling (`docker.cpu.throttled` on Datadog): under normal production load this metric should be almost always 0. If it's frequently non-0 it means your CPU limits are too low.

### Recommendations for initial limits and requests

The following are recommended initial limits/requests for a stateless microservice. 

You can use this until you have performed load tests to understand the actual resources needed by your service. Note that if your service keeps significant amount of data cached in memory, or has to handle a high number of concurrent requests, the following numbers may not be appropriate.

```yaml
  requests:
    cpu: 500m      # 1/3x as limits.cpu; should be low enough to keep CPU usage equal to
                   # the HPA target multipled by requests.cpu
    memory: 256Mi  # should be the same as limits.memory, and high enough to avoid
                   # OOM during normal operations and in case of dependency failures
  limits:
    cpu: 1500m     # 3x as requests.cpu; should be high enough to keep `docker.cpu.throttled`
                   # down to 0 during normal operations
    memory: 256Mi  # should be the same as requests.memory
```

After doing a representative load test of production workloads, and especially after releasing in production, you should review your resources requests and limits and fix them as needed. Refer to the [next section](#recommendations-for-limits-and-requests) for general recommendations regarding how to choose limits and requests.

### Recommendations for limits and requests

*NOTE*: These recommendations may not apply to all services or workloads. Do not blindly apply them without load tests!

- In general, it is advisable to have many small pods instead of very few big pods, and in any case you should have at least 3 pods for availability.
- It is normally not advised to run too many pods, as running too many pods can cause resource exhaustion or overload in your dependencies (e.g. too many open connections on your database or caching server), make debugging/troubleshooting more difficult, and slow down the deployment process. 
- In general, you should allocate just enough resource headroom to ensure that your pods can work correctly under nominal conditions and likely exceptional circumstances. Avoid needlessly reserving too many resources.
- Document the rationale for choosing specific values for the requests and limits.
- Memory limits should be equal to memory request: this makes it unlikely for kubernetes to kill your pod due to the memory consumption of **other** pods.
- The overall CPU utilization (`docker.cpu.usage`) of your deployment should ideally always be the one set for the HPA (e.g. if your CPU request is 500m and your HPA target is 65%, your CPU usage in each pod should always be 65% of 500m, i.e. ~325m[^metric]). Considering that the recommendation is to set HPA min replicas to 3, you may need to lower your CPU requests.
- Understand the differences between RSS and the size of the Go heap.
- If your service performs reads/writes on the filesystem during regular operations you should raise your memory request/limits to ensure there is enough memory for the page cache.
- Periodically review the historical resource usage of your services and perform corrective actions to ensure your service is not consuming too many resources.

#### Golang services

The golang GC can interact negatively with the CFS sched and cause high tail latencies. If tail latency is a concern:

- GOMAXPROCS should be set to `floor(limit.cpu * 2 / 3)` (or you should use something like `github.com/uber-go/automaxprocs` to do it automatically)
- CPU limit should be at 2x\~4x of CPU request
- CPU limit should not be less than `1000m`, and ideally at least `1500m`, since `GOMAXPROCS` can not be less than 1.


## See Also

- [Requests and Limits Best Practices (Kubernetes Documentation)](https://cloud.google.com/blog/products/gcp/kubernetes-best-practices-resource-requests-and-limits)
- [Managing Compute Resources for Containers (Kubernetes Documentation)](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container)
- [Assign Memory Resources to Containers and Pods (Kubernetes Documentation)](https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/)
- [Assign CPU Resources to Containers and Pods (Kubernetes Documentation)](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/)
