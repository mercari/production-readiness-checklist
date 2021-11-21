# Request ID

## What is "Request ID"?

Request ID is unique identifier generated per each requests. It's generated at edge gateway and propagated to upstream microservices where the request goes. 

## Why is "Request ID"?

Request ID is used for tracing a request across the multiple microservices. Since one reuqest goes to multiple microservices, it's important to be able to debug across them. For examples, we annotate logs with the request ID, so we can search and extract logs of the requests from multiple services and see what happened. 
