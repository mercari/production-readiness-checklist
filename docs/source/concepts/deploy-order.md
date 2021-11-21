# Deploy Order

Services need to be able to start in any order. When your service is deployed, it may start before other services or components it depends upon. For example, your service may start before the database it talks to is available.

## Why is it Important?

### Ease of Deployment
You can deploy services all at once, and eventually they will all work. If there is a fixed order you need to deploy services in, your deployment process will be complicated, and your re-deployment process even more so.

### Disaster Recovery
If many or all services stop running, they can all be started in any order and eventually everything will start to work.

### Proper Error Handling
Supporting any deploy order also means having correct error handling for when a dependency is not available. It requires you to consider how your service will respond to requests when you cannot yet talk to your database. It also means you need to consider how to handle the initial connection to that dependency, which may not exist yet.

## See Also

- [Graceful Degradation](graceful-degradation.md)
- [Truncated Exponential Backoff](https://cloud.google.com/storage/docs/exponential-backoff)
