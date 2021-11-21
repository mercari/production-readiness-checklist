# Check Production Readiness

This documentation describes the steps to do Production Readiness Check (PRC), which is required for all services **before receiving real production traffic**.

> As long as you make sure there are no side effect on production users, you should normally deploy your service to the production environment before opening the PRC. This is recommended because some of the points in the list below (e.g. capacity estimation, dashboards, screenboards, alerting, profiling, ...) can only be validated if the service is deployed in production and can receive some non-production traffic. 

## 1. Choose a level

Read [Production Readiness Level](../references/production-readiness-level.md) and decide which level is appropriate for your service (you need to have defined the SLIs/SLOs of your service to be able to do this). Also, see [Production Readiness Checklist](../references/production-readiness-checklist.md) to understand what's required for different levels.

## 2. Create a new GitHub issue

Create a new GitHub issue for production readiness review (Internally, we prepare GitHub Issue teamplate for production readiness check and the service owners create an issue by it. See an [example](https://github.com/mercari/production-readiness-checklist/issues/1)).

## 3. Verify the checklist

Verify if each item is satisfied or not **by your own team**.

- If it is not satisfied and it should be, work on satisfy it and then proceed as in the following point.
- If it is satisfied, check the item in the list and **provide evidence** (e.g. links to tickets, screenshots, documents, test results, ...) showing that it is satisfied. **If evidence is not provided the review process will take much longer**.
- If a specific item is not applicable to your service check the item and explain, as evidence, **why** it's not applicable.

## 4. Get reviews

After you have checked all items in the list, ask for review:

- If it's a Mercari microservice, please ask architect team
- If it's a Merpay microservice, please ask merpay SRE
