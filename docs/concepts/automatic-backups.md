# Automatic Datastore Backups

Automatic Datastore Backups refer to automatically making a backup of all data in a database (or other kinds of datastore) to be able to restore to a previous state.

These backups should happen either on a schedule, or before important events depending on the data and datastore (e.g. before any event that may negatively impact the state of the database such as schema changes, manual operations, or service releases).

## Why is it Important?

There are many unpredictable issues that can occur when maintaining a datastore

- Accidental database deletion
- Corrupt data
- Bad schema migration
- Lost credentials
- Ransomware (e.g. [CryptoLocker](https://en.wikipedia.org/wiki/CryptoLocker))
- Mistake in manual operation
- Environmental disaster
- Power failure
- Hardware failure
- Sabotage

Losing data can

- Inconvenience customers
- Lower trust in the company
- Compromise compliance (e.g. lost <dfn title="Know Your Customer">KYC</dfn> or financial information)
- Cause irreparable damage through loss of data consistency
- Cause prolonged outages

## See Also

- [Gitlab Database Incident](https://about.gitlab.com/2017/02/01/gitlab-dot-com-database-incident/) 
- [Disaster Recovery](https://en.wikipedia.org/wiki/Disaster_recovery)
