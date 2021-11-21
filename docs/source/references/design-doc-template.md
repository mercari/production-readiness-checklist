# Service Design

- Author(s)
  - (Authors of this proposal)
  - @CAFxX (Carlo Alberto Ferraris)
- Histroy
  - (List major version changes)
  - 2018/10/1: initial design
  - 2018/10/5: Reviewed with @tcnksm, @dragon3
  - 2019/12/1: added gRPC interface

## Summary

> The contents of the Summary section (and subsections) should answer the question: "why do we need to build/do what is described in the rest of this document"?

## Service description

> Provide a brief description of the service. This should include a description of the concerns of the service, and how other services can interact with these concerns.

## Background

> Explain why we need the service (from a business perspective) and the context in which the service operates (e.g. main relationships with other existing or future services, co-existence with related/similar services).

## Goals

> List in this section which goals you are trying to achieve.

### Non-goals

> List in this section which goals you are <span style="text-decoration:underline;">not</span> trying to achieve, especially if these non-goals are closely related with, or could be assumed to be included in, the goals stated above.

## Useful Links 

> If any of useful links.

- Github repos
- Related design docs
  - Design docs this doc updates/obsoletes
  - Design docs that update/obsolete this doc
  - Design docs of related services (clients, dependencies)

## System Design

### Architecture Diagram / Data Flow Diagram

> Provide the architecture diagram. As they say, a picture is worth a thousand words :)

### Interfaces

> Describe about the service interface.

- Does the service provide HTTP APIs or gRPC APIs, or both? 
  - If gRPC, provide the list of RPC calls
  - If HTTP, provide the list of endpoints
  - Regardless of protocol, a high-level description of what function each call/endpoint does is recommended (detailed parameters are not required unless you want feedback on details of the API design)
- Does the service publish or subscribe to pubsub streams?
  - For each stream, give a high-level description of its contents and purpose
  - Streams should normally contain protobuf messages defined in platform-proto
- Does the service implement any batch/offline jobs?
  - For each job, give a high-level description of its inputs, outputs, and purpose

### Traffic Migration (Optional)

> If the service is going to replace any existing monolith endpoint, consider how to migrate existing traffic to the new service. 

### Expected Clients

> List the clients that are expected to use the service. If possible, also explain how they will use it, what kind of SLOs they will require, and roughly what kind of load they will add to the APIs.

### Dependencies

> List the services (including 3rd party services, database tables or pubsub) that your service will depend upon. If possible, include information about which dependencies are critical (i.e. they are potential causes of SLO violations for your service) and which are not (in which case describe how your service will react), as well as any information about the expected load and SLOs. Example (assuming /xxx is an HTTP endpoint exposed by the service being proposed in this document). 

### SLO

> Propose here any [SLOs](https://landing.google.com/sre/sre-book/chapters/service-level-objectives/) for your service. You should discuss the required SLO with your stakeholders (especially with the relevant product managers). Details must be figured out **before Production Readiness Check**, and must be consistent with the SLOs of clients and dependencies described above. 

### Database

> List all the tables that the service will directly access. 

#### Database Migration

> If the service is going to migrate an existing table in monolith, consider how to do it. 

#### Database Backups

> If the service is going to have a database, specify the legal and product requirements and your target RTO/RPO.

#### PII Considerations

> Does the service save any personal information? If so, list what, why and how the service deals with PII.

### Security Considerations

> Write about security considerations.

## Alternatives (Optional) 

> If you have considered other solutions, mention them here, along with their pros, cons, and the reason they were discarded. This may include potential future evolutions/extensions of your service that are not part of the current effort, but are expected in the future.

## New Technologies Introduced (Optional) 

> If the service introduces a new technology that hasn’t been widely used in Mercari, introduce it and explain why it’s necessary.

## References

> Add here any reference to additional discussions, material, etc. for context.
