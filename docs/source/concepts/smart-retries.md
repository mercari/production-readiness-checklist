# Smart retries

All microservices (and, more in general, distributed system) developers should be intimately familiar with the [*fallacies of distributed computing*](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing), and especially with their first one:

1. **The <dfn title="“Network” in this context refers to anything that is part of the network, i.e. including remote endpoints">network</span> is reliable**
2. Latency is zero
3. Bandwidth is infinite
4. The network is secure
5. Topology doesn't change
6. There is one administrator
7. Transport cost is zero
8. The network is homogeneous

One of the ways to minimize the inherent unreliability of individual subsytems (e.g. a microservice) or infrastructure (e.g. network) that implement a distributed system (e.g. a microservice forest) is to provide countermeasures for such unreliability as part of the normal flow of execution. The simplest example of such coutnermeasures is to perform retries.

Retries have the unfortunate effect of increasing the load on all involved actors (clients, callers, callees and infrastructure). As points 2., 3. and 7. in the *fallacies* also highlight, resources are not infinite so **retries should be performed considering the situation at the time the failure is detected**. If the retry design and implementation is not done properly the increased load can potentially worsen the situation, making automatic recovery slower and/or impossible.

We call **smart retries** retries that are designed and implemented considering these aspects.

It is important to note that, as smart retries depend on the conditions at the time the failure is detected, different code paths (e.g. different services, endpoints, ...) are likely to need **different retry policies**. It is unlikely that a single retry policy will work for all backends, or in general for all possible callees your service interacts with.

## General policy

Microservices **SHOULD** retry requests to any of their dependencies (regardless of whether they are internal APIs, external APIs or other infrastructure like databases) whenever doing so has a signficant chance of improving latency, resource usage or user experience. Conversely, microservices should **not** retry requests when performing such retries has a even more significant chance of making latency, resource usage or user experience worse.

Retries should ideally be:

- bounded in number (e.g. "at most 3 retries")
- bounded in time for a single retry (e.g. "any of the single request should complete within 1 second")
- bounded in time for all retries (e.g. "all retry attempts should complete within 5 seconds")
- staggered in time (e.g. [use exponential retry intervals and jitter](https://landing.google.com/sre/sre-book/chapters/addressing-cascading-failures/))
- staggered in destination (e.g. ensure that subsequent retries are sent to different instances)
- tested by simulating the expected failure modes

Retries should normally not be attempted when:

- the callee returns a non-retryable error (e.g. the error is not due to the callee but rather it is the request itself that has a problem)
- either callee or caller are experiencing a resource shortage, and as a result either of them wish to shed some load as a result (note that this can apply to whole requests, not just to retries)
- there is no time to retry a request (e.g. when the deadline is so close that a retry can not possibly complete in time, or when the initial request has already been cancelled)
- the request to the callee is not idempotent and the caller is unsure whether the previous request completed or failed on the callee side (note: this should really never happen, as it means the API contract is misdesigned)
- you have out-of-band signals that indicate that the callee is unavailable for the time being (e.g. service discovery tells you no instances of the callee are available or able to process the request)

The list above is not exhaustive, as there may be other **specific** scenarios in which the conditions above may be inappropriate.

An example of this is in case the caller is performing a transaction involving multiple callees/susbystems: in such cases whether to retry or not depends on the semantics of the API contract that caller has with its clients, as well as the nature and state of the transaction itself (e.g. if not retrying would leave the whole system in a inconsistent state and the client has already cancelled the request, it is appropriate to keep retrying until the transaction has been rolled back)

## See Also

- [Addressing Cascading Failures (Google SRE book)](https://landing.google.com/sre/sre-book/chapters/addressing-cascading-failures/)
- [The tail at scale (the morning paper)](https://blog.acolyer.org/2015/01/15/the-tail-at-scale/) - Techniques (including request hedging/tieing) for controlling latency in distributed systems
- [ϕ Accrual Failure Detector](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.80.7427&rep=rep1&type=pdf) - Technique to more reliably detect failures in distributed systems
- [gRPC client retries](https://github.com/grpc/proposal/blob/master/A6-client-retries.md)
