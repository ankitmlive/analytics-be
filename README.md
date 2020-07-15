# analytics-be
BetterWorks Analytics assessment Repo

I am creating it as a scalable project structure, that's why created different app for different features:

Department & Employees are unique entity in app
each department can have multiple teams with unique Team Leads

Team Leads:
team leads are the employees that can be the employee for other Teams.

I am assuming:
An Employee can belongs to only one team
A Team Lead can be a Lead only for one Team
A Team Lead can also be a employee of other team(not a lead)


## Url's
#### Acording to UI i am assuming that the mentioned page is homepage and all the objectives will be listed on the first render, so i will fetch all the current objectives on app with "pending" & "Complete" status. The First API will be :

## Home Api
    http://127.0.0.1:8000/api/v1/analytics/

## Employee Api
    http://127.0.0.1:8000/api/v1/employees/ GET to all employees
    http://127.0.0.1:8000/api/v1/employees/ POST to new employee

## Department api
    http://127.0.0.1:8000/api/v1/departments/ to all departments
    http://127.0.0.1:8000/api/v1/departments/ to new department

## Objective Api
    http://127.0.0.1:8000/api/v1/objectives/create/ for creating new objective
    http://127.0.0.1:8000/api/v1/objectives/objective-id/  for viewing detail of objective

## Key api
#### for creating a new status key
    http://127.0.0.1:8000/api/v1/key/create/

