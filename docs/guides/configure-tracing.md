# Configure Distributed Tracing

Tracing is a very useful tool to be able to understand where are issues or bottlenecks in a distributed system, like the  microservices forest. For this reason distributed tracing instrumentation is mandatory (and checked during production readiness checking).

## What to trace

Ideally, every major operation that can independently fail or consume varying amount of resources should be traced. The tracing granularity can vary depending on the nature of the specific microservice, but as general guidelines the following events should be traced:

- [Incoming gRPC requests](#incoming-grpc-requests)
- [Outgoing gRPC requests](#outgoing-grpc-requests)
- [Internal operations](#internal-operations)

## How to trace

This section shows how to implement tracing for specific events. While currently the section is tailored for Go services, it similarly applies to [other languages (e.g. nodejs, Java or PHP)](https://docs.datadoghq.com/developers/libraries/#apm-tracing-client-libraries).

### Incoming gRPC requests

Add [`UnaryServerInterceptor`](https://godoc.org/gopkg.in/DataDog/dd-trace-go.v1/contrib/google.golang.org/grpc#UnaryServerInterceptor) and/or [`StreamServerInterceptor`](https://godoc.org/gopkg.in/DataDog/dd-trace-go.v1/contrib/google.golang.org/grpc#StreamServerInterceptor)to your gRPC server middlewares.

### Outgoing gRPC requests 

Add [`UnaryClientInterceptor`](https://godoc.org/gopkg.in/DataDog/dd-trace-go.v1/contrib/google.golang.org/grpc#UnaryClientInterceptor) and/or [`StreamClientInterceptor`](https://godoc.org/gopkg.in/DataDog/dd-trace-go.v1/contrib/google.golang.org/grpc#StreamClientInterceptor) to your gRPC client middlewares.

### Internal operations

As an example, let's assume the main logic in your request handling the function called `operationA`.

```go
a, err := operationA(ctx)
if err != nil {
    return nil, status.Errorf(codes.Internal, "failed to do A: %s", err)
}
```

To trace the operation, you can add the following lines at the beginning of the body of both functions, e.g.:

```go
func operationA() {
    span, ctx := tracer.StartSpanFromContext(ctx, "operationA")
    defer span.Finish()
}
```
