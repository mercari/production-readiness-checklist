# Production Readiness Checklist

You can use the production readiness checklist if a microservice is production ready or not. The checklists are divided into 2 phases:

- [Design checklist](design-checklist.md) (the checklist you must meet before beginning development of your microservice)
- [Pre-production checklist](pre-production-checklist.md) (the checklist you must meet before production deployment)

Please use these checklists for each phase.

## Production readiness level

There are no one-size-fits-all. So we defined some levels in the readiness:

- :star2: **Level A** - for a **critical** microservice
- :star: **Level B** - for a **standard** microservice
- :boom: **Level C** - for an **experimental** microservice

Use the level to decide which check to meet. See [Production Readiness Level](production-readiness-level.md) for details.

## Conventions used in readiness checklist

The following conventions are used for checklist items.

- `it`/`its` refers to the target microservice.
- :white_check_mark: indicates that passing the first check is required to meet the level.
- :soon: indicates that this check is currently not enforced, but it will be enforced in the future.
