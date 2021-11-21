# PodDisruptionBudget

## What is "PodDisruptionBudget"?

"PodDisruptionBudget" is a Kubernetes object which limits the number pods of a replicated application that are down simultaneously from [voluntary disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#voluntary-and-involuntary-disruptions).

## Why "PodDisruptionBudget" is needed to be configured?

### If "PodDisruptionBudget" is not configured

Let's say, your microservice is running on a Kubernetes cluster with "PodDisruptionBudget" and configured 2 replicas like this:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: your-microservice
  namespace: your-namespace
spec:
  replicas: 2
...
```

The cluster has 3 nodes and your microservice's pods "app-1" and "app-2" are running on "node-1" and "node-2":

![1](https://user-images.githubusercontent.com/20374/47538880-7de62280-d908-11e8-9d48-b2a616eea888.png)


Now a cluster administrator (Microservices Platform member) is going to `drain` node-1 in order to upgrade the cluster:

![2](https://user-images.githubusercontent.com/20374/47538881-7e7eb900-d908-11e8-869d-e85f0f388162.png)


"app-1" is now terminating and a new pod "app-3" is pending state. At this point, if the cluster administrator tries to `drain` "node-2":

![3](https://user-images.githubusercontent.com/20374/47538882-7e7eb900-d908-11e8-953e-23e5a34b9b41.png)


What happened? Yes, you don't have any healthy pods now. 

`PodDisruptionBudget` protects your microservices from this situation.


### If "PodDisruptionBudget" is configured

Now you have same microservice with "PodDisruptionBudget" like this:
```yaml
apiVersion: policy/v1beta1
kind: PodDisruptionBudget
metadata:
  name: your-microservice
  namespace: your-namespace
spec:
  minAvailable: 50% # 50% is just to keep the example simple, it is not the recommended value
  selector:
# ...
```

Even if the cluster administrator tries to `drain` "node-2", it will block because there is only 1 available pod.

![4](https://user-images.githubusercontent.com/20374/47539175-fbf6f900-d909-11e8-8cb3-6d20c09cd6d2.png)

That's why "PodDisruptionBudget" is needed to be configured for your microservices.

## What's next

- [Configure PodDisruptionBudget](../guides/configure-pod-disruption-budget.md)
- [How Disruption Budgets Work](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#how-disruption-budgets-work)
