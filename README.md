# Production Readiness Checklist at Mercari

This repository contains [production readiness checklists](docs/references/production-readiness-checklist.md) and related [documentation](/docs) used internally at Mercari and Merpay to make its microservices production-ready (service is ready for live customer requests). This is a reference version of a checklist which excludes internal specific checks but, we thought, can be used outside of Mercari and Merpay, too. Since our main technical stacks are [Go](https://golang.org/), [Kubernetes](https://kubernetes.io/), and [GCP](https://cloud.google.com/), some of the checklists are also specific to them. 

The checklists are divided into 2 phases:

- [Design checklist](/docs/references/design-checklist.md): the checklist you must meet before beginning development of microservice
- [Pre-production checklist](/docs/references/pre-production-checklist.md): the checklist you must meet before production deployment

You can see the guide [Check Production Readiness](/docs/guides/check-production-readiness.md) to know its usage and its review process. 
