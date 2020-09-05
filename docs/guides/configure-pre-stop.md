# Configure PreStop

## Before you begin

- [PreStop](../concepts/container-lifecycle-hooks-pre-stop.md)

## 1. Configure `PreStop` in deployment manifest

Add `PreStop` to `.spec.template.spec.containers[*].lifecycle` of your deployment manifest like below.
If it is known that preStop+SIGTERM process requires over 30 seconds, specify `terminationGracePeriodSeconds` to `.spec.template.spec`. If it does not complete within 30 seconds, it switches over to SIGKILL in the next processing and error maybe slowed.

App e.g.:

``` yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: your-microservice
  namespace: your-microservice-namespace
...
spec:
  template:
    spec:
      containers:
      - name: your-microservice
        lifecycle:
          preStop:
            exec:
              command: ["/bin/sleep", "10"]
...
      terminationGracePeriodSeconds: 90
```

Nginx e.g.:

``` yaml
spec:
  template:
    spec:
      containers:
      - name: your-microservice
        lifecycle:
          preStop:
            exec:
              command: ["/bin/sh", "-c", "sleep 60; nginx -s quit; sleep 5"]
...
      terminationGracePeriodSeconds: 90
```

## References

- [Attach Handlers to Container Lifecycle Events](https://kubernetes.io/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/)
- [Kubernetes best practices: terminating with grace](https://cloud.google.com/blog/products/gcp/kubernetes-best-practices-terminating-with-grace)
