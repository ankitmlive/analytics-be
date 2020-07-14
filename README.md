# analytics-be
BetterWorks Analytics assessment Repo

I am creating it as a scalable project structure, that's why created different app for different features:

Department is a unique entity in app
each department can have multiple teams with unique Team Leads

Team Leads:
team leads are the employees that can be the employee for other Teams.

I am assuming:
An Employee can belongs to only one team
A Team Lead can be a Lead only for one Team
A Team Lead can also be a employee of other team(not a lead)


## Url's
#### Acording to UI i am assuming that the mentioned page is homepage and all the objectives will be listed on the first render, so i will fetch all the current objectives on app with "pending" & "Complete" status. The First API will be :

##### http://127.0.0.1:8000/api/v1/analytics/


## Department api
### GET :
##### http://127.0.0.1:8000/api/v1/departments/
### POST :
##### http://127.0.0.1:8000/api/v1/departments/

