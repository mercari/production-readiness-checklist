# Configure Rolling Update

This articles will guide you how to configure rolling update for your service.

## Before you begin

You need to understand the following concepts:

- [Gradual Deployment](../concepts/gradual-deploy.md)

### 1. Configure deployment manifest

Configure rolling update with Kubernetes is pretty straight forward, we just need to configure strategy
to `rollingUpdate` in the deployment manifest.
```
...
  strategy:
    rollingUpdate:
      maxSurge: xx
      maxUnavailable: xx
...
```

`maxUnavailable` is an optional field to specify maximum number of pods that can be **unavailable** during the roll out
process. The value can be percentage and absolute number. Default value is 25%.

`maxSurge` is an optional field to specify maximum number of pods that can be **created** above the original number of pods. The value can be percentage and absolute number. Default value is 25%. 

These parameters can be tuned for availability and speed. For example:

- `maxUnavailable=0` and `maxSurge=20%` ensure number of pods is running as desired and rapid scale up
- `maxUnavailable=10%` and `maxSurge=0` performs update with no extra capacity
- `maxUnavailable=10%` and `maxSurge=10%` scales up and down quickly, but the number of running pods might be lower than desired
