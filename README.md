# Production Readiness Checklist at Mercari

This repository
contains [Production Readiness Checklists](docs/references/production-readiness-checklist.md)
and related [documentation](docs) used internally at Mercari and Merpay to make its
microservices production-ready (service is ready for live customer requests). This is a
reference version of the checklist which excludes internal specific checks but, we
thought, can be used outside of Mercari and Merpay, too. Since our main technical stacks
are [Go](https://golang.org/), [Kubernetes](https://kubernetes.io/),
and [GCP](https://cloud.google.com/), some of the checklists are also specific to them.

The checklists are divided into 2 phases:

- [Design Checklist](docs/references/design-checklist.md): the checklist you must meet
  before beginning development of microservice
- [Pre-production Checklist](docs/references/pre-production-checklist.md): the checklist
  you must meet before production deployment

The check items in each phase vary by
its [Production Readiness Level](docs/references/production-readiness-level.md) which is
defined by its SLO. You can see the
guide [Check Production Readiness](docs/guides/check-production-readiness.md) to know
checklist usage and its review process. 
