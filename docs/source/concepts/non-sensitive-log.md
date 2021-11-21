# Non-sensitive log

## What does "Non-sensitive log" mean?

"Non-sensitive log" means that your application doesn't write any sensitive information to application log such as user's password, email address, credit card information.

## Why should we make our log "Non-sensitive"?

We must make our log "Non-sensitive" in order to prevent those sensitive information exposed accidentally.
Once those sensitive information exposed and malicious attackers get it, it will cause huge security incident.

For example, personal data is a sensitive log. This is a definition of "personal data" in GDPR:

> ‘personal data’ means any information relating to an identified or identifiable natural person (‘data subject’); an identifiable natural person is one who can be identified, directly or indirectly, in particular by reference to an identifier such as a name, an identification number, location data, an online identifier or to one or more factors specific to the physical, physiological, genetic, mental, economic, cultural or social identity of that natural person;

https://gdpr-info.eu/art-4-gdpr/
