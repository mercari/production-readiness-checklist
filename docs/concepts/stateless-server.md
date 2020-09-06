# Stateless Server

Running a stateless server means that all persistent data is stored outside of the server. 

## Why is it Important?

- Stateless servers are easier to deploy/upgrade.
- Stateless servers are much easier to recover in case something breaks.
- Managing persistent datastores correctly requires significant amount of engineering effort per datastore.
- Stateless servers can be scaled independently from their datastore.
- Multiple pods of your service can disappear (and lose their non-persistent state) at any time.
