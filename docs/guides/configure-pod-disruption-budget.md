# Configure PodDisruptionBudget

## Before you begin

- [PodDisruptionBudget](../concepts/pod-disruption-budget.md)
- [Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb/)

## Write manifest file

Here is an example of `PodDisruptionBudget` manifest yaml:

```
apiVersion: policy/v1beta1
kind: PodDisruptionBudget
metadata:
  name: mercari-echo-jp
  namespace: mercari-echo-jp-prod
spec:
  maxUnavailable: 33%
  selector:
    matchLabels:
      app: mercari-echo-jp
```

For example, with a `maxUnavailable` of 33%, evictions are allowed as long as no more than 33% of the desired replicas are unhealthy.

If you follow the [resource request/limit guidelines](../concepts/resource-requests-and-limits.md), it is recommended to use a `maxUnavailable: 33%` PDB.


### :warning: Avoid specifying number of replicas

If you specify number of replicas (e.g. `5`) instead of percentage (e.g. `33%`), you will get unexpected disruption when the pods auto scales.

For example, instead of using:

``` yaml
spec:
  maxUnavailable: 5   # bad: will cause problems with autoscaling
```

it is recommended to use a percentage:

``` yaml
spec:
  maxUnavailable: 33%   # good
```

### :warning: Do not use a non-resolvable combination of replicas and maxUnavailable values

When specifying `maxUnavailable`, either percentage or replicas, please make sure the deployment subject to the PDB doesn't break the PDB acceptance.

For example, if your Deployment has `replicas: 1` and a PDB with `maxUnavailable: 20%`, the PDB controller will not be able to drain your pods, freezing the draining process, thus affecting the whole cluster drain process. Same for `replicas: 2` and `maxUnavailable: 66%`. To make it resolvable, either change the `replicas` to `3` or `maxUnavailable` to `50%`. Please **always* make sure your PDB `maxUnavailable` value is resolvable.
