# Liveness Probe

## What is a "Liveness Probe"?

"Liveness Probe" is a kind of health check. Kubernetes (kubelet) performs and reacts to the probes on running containers. "Liveness Probe" indicates whether the Container is running. If the "Liveness Probe" fails, the kubelet kills the Container, and the Container is subjected to its restart policy. If a Container does not provide a liveness probe, the default state is `Success`.

In a nutshell, returning success to a liveness probe means: "the process is able to continue operating"; returning failure means "the process is unable to continue operating properly, and should be restarted to recover".

## Why is a "Liveness Probe" necessary?

For example, let's say your container is running but encounters an issue or becomes unhealthy (e.g. because a deadlock is detected). It is unable to make progress now. Restarting the container can recover it from unhealthy status. If you configure "Liveness Probe" properly, Kubernetes does it for you.

# What's next

- [Configure Liveness Probe](../guides/configure-liveness-probe.md)
- [Pod Lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle)
