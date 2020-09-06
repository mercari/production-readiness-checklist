# Automated Rollback

Automated Rollback means that a service can be rolled back to an older version in one command. This can take many forms, including (but not limited to) a shell script, CI pipeline or Spinnaker configuration. The rollback procedure should also be documented.

## Why is it Important?

- If something breaks, it is very easy to go back to an older version
- Disaster recovery will be faster and simpler
- The downgrade procedure for your service is documented through code

## Tips and Tricks

- If your service has a good design which supports [graceful degradation](./graceful-degradation.md) and [gradual deployment](./gradual-deploy.md) your rollback procedure can be very simple, possibly the same as your upgrade procedure
- When you plan any upgrade, you should consider what might happen during rollback
- Keep in mind database migrations
  - If you update a database schema with a new column or similar, your old code might not support it
  - If you roll back a database schema, data may be lost
  - Your database upgrade and rollback might be better as asymmetric operations to prevent data loss, but only if the rolled back schema is still fully compatible with the old code (you need to test this before release too!). This would need careful design and testing
