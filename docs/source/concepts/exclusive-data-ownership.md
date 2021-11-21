# Exclusive Data Ownership

Exclusive data ownership is a design decision which involves making sure that all data has just one clear owner. Exclusive data ownership is considered to be a good general practice to ensure services have one set of responsibilities, that don't overlap with other services.

## Why is it Important?

Exclusive data ownership means:
- It is easy to see where changes to data can come from
- Services are not tightly coupled by their dependence on a shared datastore
- Rules about data which cannot be enforced at the datastore level, can be enforced consistently by the owning application
