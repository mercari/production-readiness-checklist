# PreStop

## What is "PreStop"?

"PreStop" is a kind of container lifecycle hooks. Kubernetes provides Containers with lifecycle hooks. The hooks enable Containers to be aware of events in their management lifecycle and run code implemented in a handler when the corresponding lifecycle hook is executed.
"PreStop" is called immediately before a container is terminated due to an API request or management event such as liveness probe failure, preemption, resource contention and others.

## Why "PreStop" is necessary?

A new connection may be established during executing a Pod Rolling Upgrade even though an old version of the Pod is being deleted. It is due to Kubernetes specifications.
To avoid this, it is necessary to wait for a time when a new connection may be established with the sleep command, and execute a graceful shutdown when a new connection can no longer be established.

## What's next

- [Configure PreStop](../guides/configure-pre-stop.md)
- [Container Lifecycle Hooks](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/)
