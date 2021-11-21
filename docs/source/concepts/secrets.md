# Secrets

## What is a "Secret"?

A Secret is an object that contains a small amount of sensitive data such as a password, a token, or a key.
Secrets are stored and protected securely in Kubernetes (etcd).

## Why "Secrets" is necessary?

In most cases, your application needs some sensitive data such as a password to access databases, or a token to access other services.
As you know, You must not put them into your application source code, but also you must not put them in a Pod or Deployment manifest to reduce the risk of accidental exposure.

Let's say that you need to set a database password as an environment variable `DATABASE_PASSWORD` and its value is "greatpassword".
You must not put it in manifests like below:

``` yaml
# bad
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: your-microservice
  namespace: your-microservice-namespace
spec:
  template:
    spec:
      containers:
      - name: your-microservice
        env:
          - name: DATABASE_PASSWORD
            value: "greatpassword"     # <- DON'T DO THIS!
...
```

Instead, you can use "Secrets" for it like this so that sensitive information doesn't appear.

``` yaml
# good
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: your-microservice
  namespace: your-microservice-namespace
spec:
  template:
    spec:
      containers:
      - name: your-microservice
        env:
          - name: DATABASE_PASSWORD
            valueFrom:
              secretKeyRef:
                name: your-microservice-secret
                key: database-password
...
```

In this example manifest, `your-microservice-secret` is the name of "Secret" and you can get a value with `key` from the "Secret".
