# Configure Liveness Probe

## Before you begin

- [Liveness Probe](../concepts/liveness-probe.md)

## 1. Implement health check endpoint in your application

If your application already has a health check endpoint, you can skip this section.
Otherwise, you need to implement it in your application.

Here is a simple example for Go app:

``` go
http.HandleFunc("/healthz", func(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte("OK"))
}
http.ListenAndServe(":8080", nil)
```

## 2. Configure `livenessProbe` in deployment manifest

Add `livenessProve` to `.spec.template.spec.containers` of your deployment manifest like this:

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
        livenessProbe:
          initialDelaySeconds: 10
          periodSeconds: 10
          timeoutSeconds: 1
          successThreshold: 1
          failureThreshold: 3
          httpGet:
            path: /healthz
            port: 8080
            scheme: HTTP
```

You can configure the following fields of `livenessProbe`:

- `initialDelaySeconds`: Number of seconds after the container has started before liveness probe is initiated.
- `periodSeconds`: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.
- `timeoutSeconds`: Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1.
- `successThreshold`: Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness. Minimum value is 1.
- `failureThreshold`: When a Pod starts and the probe fails, Kubernetes will try failureThreshold times before giving up. Giving up in case of liveness probe means restarting the Pod. Defaults to 3. Minimum value is 1.

:warning: Please configure those parameters carefully. If you configure too short `timeoutSeconds` or `failureThreshold`, Kubernetes will restart more often than you expect. If you configure shorter `initialDelaySeconds` than an initialize duration required by your application, your container never be up. On the other hand, if you configure too long `periodSeconds`, `timeoutSeconds`, `failureThreshold`, Kubernetes can't catch dead containers quickly.

## References

- [Configure Liveness and Readiness Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/)
- [Kubernetes best practices: Setting up health checks with readiness and liveness probes](https://cloud.google.com/blog/products/gcp/kubernetes-best-practices-setting-up-health-checks-with-readiness-and-liveness-probes)
