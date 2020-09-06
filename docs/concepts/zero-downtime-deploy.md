# Zero Downtime Deploy

Zero downtime deploys refer to being able to re-deploy a service without having any noticeable impact on clients. Correspondingly, you should also not have any increase in error rates in logs, monitoring etc.

## Why is it Important?

- Errors received by customers or connected services are undesirable, and use up your error budget
- Alerts or errors that will be ignored (as they are caused by the release) can lead to complacency which makes it hard to see real issues quickly
- Service downtime leads to stampeding traffic and other cascading issues that can make small errors much worse
  
## See Also

- [Strategies for Migrating Databases](https://www.brunton-spall.co.uk/post/2014/05/06/database-migrations-done-right/)
