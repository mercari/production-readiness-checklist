# Readiness Probe

## What is a "Readiness Probe"?

"Readiness Probe" is a mechanism that can be used in case your process, before it is ready to start accepting traffic (normally at startup), needs to do substantial amounts of work - such as:

- Loading/parsing complex configuration
- Loading and/or parsing static assets
- Populating internal data structures
- Warming up internal caches
- Executing database migrations

This mechanism is normally employed during startup of the service (when work similar to the one listed above is likely to happen), but can potentially be also used during normal runtime in case the process decides/detects that some internal housekeeping (that is likely to impact its ability to handle traffic according to the service SLOs) is required. This latter case is extremely rare in practice.

In a nutshell, returning success to a readiness probe means: "the process is able to serve traffic"; returning failure means "the process is **temporarily** unable to serve traffic, so traffic should be routed to the other instances".

## Why and when is a "Readiness Probe" necessary?

If any of these steps can take significant time (e.g. more than a few seconds) then it is appropriate to use a readiness probe to signal when these initialization steps have completed, and therefore when your service can start handling traffic.

It is important to note that the **"readiness" refers to the service itself and not to its dependencies**. To understand why, consider that if all the pods of your service are not "ready", then no pod will be considered able to handle traffic, and callers will receive a DNS error (or other network-related errors) before even sending the request. At the same time, the callee (your service) may not even be able to detect the problem (since there is no traffic coming). For this reason, it is normally not appropriate to check in your readiness handler if services you depend on are ready, especially if your service can do any useful work without them. 

Also worth pointing out that the readiness mechanism is supposed to have a finite duration: conceptually, it is not appropriate for a service to never become ready.

# What's next

- [Configure Liveness Probe](../guides/configure-liveness-probe.md)
- [Pod Lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle)
