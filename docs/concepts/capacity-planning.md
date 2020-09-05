# Capacity Planning

Capacity Planning is measuring the performance of a service and working out the limits of it's operation. From this information you can estimate if a service will be able to handle the amount of traffic you expect it to receive.

## Why is it Important?

 - To predict in advance if your service will be able to serve all the customers you need it to serve
 - To be able to plan and justify performance work
 - To be able to plan for [auto scaling](./auto-scaling.md)
 - To be able to configure better monitoring and alerting for your service
 - To understand failure conditions of your service

## Tips and Tricks

- When testing performance of your application, you should test ALL OF (in order of importance):
  - Each function of your application in isolation
  - Many functions at once based upon an estimate of real-world traffic
  - Randomized testing or "Fuzzing" of different functions
- We are capable of mirroring traffic for services which use the Gateway, this may be a good method of testing real traffic against unreleased versions of some services. Please talk to the Architect team if you would like to discuss this possibility!

### Testing in Isolation

You should have a way to performance test each function of your application in isolation. That means if your application has multiple different API endpoints, each one should be tested as independently as possible. The purpose of this is to ensure that you have a known baseline of performance. This follows the scientific practice of testing variables in isolation.

### Testing based upon Real World Estimates

You should be able to performance test your application in some estimate of a real world scenario. This means you should measure what sort of requests your application will receive and try to mimic those requests in a test environment. As these numbers will change over time, the test should be updated periodically to ensure the testing is still valid.

While testing in isolation would ideally be enough, there are often complex interactions between different parts of an application. This testing intends to detect if any of these complex interactions exist under expected conditions.

### Randomized Testing ("Fuzzing")

Common test scenarios tend to be based upon ideal conditions. Randomized Testing intends to measure if the performance is still consistent (or at least meeting expectations) with less-than-ideal input. This is particularly important for services which receive user traffic, as you cannot always guarantee that your application will receive good input.

In certain scenarios, bad input can cause an applications performance to be significantly worse. Applications involving caches are a common example of this, where bad input can evict important data from a cache and cause the performance of other requests to be degraded.

## See Also

 - [Google SRE Book - Auxon Case Study](https://landing.google.com/sre/sre-book/chapters/software-engineering-in-sre/#auxon-case-study-project-background-and-problem-space)
 - [Capacity Planning - USENIX Paper [PDF]](https://www.usenix.org/system/files/login/articles/login_feb15_07_hixson.pdf)
 - [Fuzzing](https://en.wikipedia.org/wiki/Fuzzing)
