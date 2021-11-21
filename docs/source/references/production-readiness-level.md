# Production Readiness Level

This documentation describes some levels of production readiness.  Please refer [Production Readiness Checklist](production-readiness-checklist.md) for checks which are required to pass to meet a level. Choose a level for a microservice based on SLO.

## How to Choose a Level?

The main factor of choosing a Service Level is the expected SLO. i.e., You need to define your service SLO in order to choose your service level.

> New to SLO? See guidelines from [Google](https://landing.google.com/sre/sre-book/chapters/service-level-objectives/)

Here's the typical required SLO for each level:

| Service Levels | Required SLO |
| -------------  | ---------- |
| A | > 99.9%  |
| B | 99% ~ 99.9% |
| C | 95% ~ 99% |

When [checking production readiness](../guides/check-production-readiness.md), you will need to go through the [Production Readiness Checklist](production-readiness-checklist.md) which requires different check items for different levels.

If you find yourself having a hard time choosing the right level, a general advice is to start from Level B and work on improving it to meet Level A if necessary.  

## :star2: Level A
Level A is for **critical** microservices. Services that handle PII, contribute directly and significantly to company-level goals (e.g., GMV), or could lead to significant damage to the company during downtime (e.g., anti-social check), should usually be Level A.

## :star: Level B
Level B is for **standard** microservices. This applies to services that provide necessary functionality, but won't lead to significant usability downgrade during downtime, or can be remedied without largely affecting company-level goals. Examples: like-service, notification-service.

## :boom: Level C
Level C is for **experimental** microservices: services that provide experimental new features, or services that affect only a small part of users.
