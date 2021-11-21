# Graceful Degradation

Graceful Degradation is when a component (such as a microservice) continues to work with degraded functionality, when it is unable to function fully.

> Your service must not crash or fail to recover if a dependency becomes unavailable temporarily.

In practical terms, this means that in situations such as these, your service should still be able to keep running:

- It is unable to talk to another component (DB, another service, an external API)
- It is missing data (DB does not have the correct content)
- It is not ready to handle all requests (needs to populate a cache, or pre-calculate some responses)
- It is not able to handle all requests (e.g. the service itself, or one of its dependencies, is overloaded)
- An existing connection to another component stops working

In those sorts of situations, your service should try to respond to requests in a predictable way. There are many strategies, you should document the strategy you choose so any services which talk to your service can act appropriately.

## Why is it Important?

In a distributed system (such as a microservices architecture) there is no way to guarantee that all your dependencies will be available at all times. Other services may fail, change, be transiently unavailable or slow down and, for robustness, services must be designed and implemented so that the overall system keeps performing useful work.

## Tips and Tricks


- Define, in your API docs, what are the semantics of the API and what kind of responses can be returned during degradation scenarios
- Provide fallback data: e.g. in certain scenarios it may be appropriate to return stale data, or non-personalized data, or a limited amount of data instead of no data at all (provided this behavior is documented, see the previous point)
- Provide asynchronous state-changing operations: this is especially useful if the state change has critical dependencies on services that provide low or no SLOs
- Follow the [timeout and smart retry](smart-retries.md) guidelines, not just for the whole request but also for parts of the request; if possible run subrequests in parallel
- Keep things as simple as possible, and minimize the number of critical dependencies; in general, the simpler things are, and the lower the number of dependencies, the lower the probability that something will go wrong
- Throttle clients that are responsible for overloading your service, to ensure fairness

### Example Behaviors

These are some examples of responses you can give when in a degraded state:
 - Return a `HTTP:503 - Service Unavailable` or `GRPC:UNAVAILABLE` if it is not possible to respond to the request yet
 - Return a `HTTP:404 - Not Found` or `GRPC:NOT_FOUND` if the requested data does not currently exist
 - Tell the client to retry later. Note that `HTTP:503 - Service Unavailable` or `GRPC:UNAVAILABLE` is correct in this case too.
 - Tell the client the request was accepted, but not completed immediately with `HTTP:202 - Accepted` or `GRPC:OK`. Queue the work for later.

All of these options depend entirely upon how your service will be used. The most important part is documenting these cases, and ensuring that your service does not behave unpredictably in these situations. Your clients should know how your service will behave when a request cannot be handled.

## See Also

 - [GRPC Status Codes](https://github.com/grpc/grpc/blob/master/doc/statuscodes.md)
 - [HTTP Status Codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
 - [Relevant StackOverflow Discussion: How to Choose a Status Code for "API not ready yet, try again later?"](https://stackoverflow.com/q/9794696)
