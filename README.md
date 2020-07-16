# analytics-be
BetterWorks Analytics assessment Repo

##### It's a scalable project structure, that's why created different app for different features.
##### Department & Employees are unique entity in app.
##### Each department can have multiple teams with unique Team Leads.
##### Team leads are the employees that can be the employee for other Teams.
##### An Employee can belongs to only one team or multiple team (based on requirements so not applied contraints yet)
##### A Team Lead can be a Lead only for one Team
##### A Team Lead can also be a employee of other team (not a lead)
##### An objective is direclty belongs to employee
##### A key is a status for an objective

### Installation 

    1 - Make sure python3.3+ is installed on the host system
    2 - Python 3.3+ comes with virtualenv if not install it (can be avoided if host machine have python3.3+)
    3 - git clone https://github.com/ankitmlive/analytics-be.git
    4 - cd analytics-be
    5 - python3 -m venv env
    6 - source env/bin/activate
    7 - pip install -r requirements.txt

### Start the Server
    python manage.py runserver

### Home Api's
    1 - http://127.0.0.1:8000/api/v1/analytics/ --> GET Method will return all the objective with status (keyresults) for Pending or Complete.

### Employee Api's
    1 - http://127.0.0.1:8000/api/v1/employees/ --> GET Method to list all employees
    2 - http://127.0.0.1:8000/api/v1/employees/ --> POST Method to new employee
    3 - http://127.0.0.1:8000/api/v1/employees/<employee-id>/ --> GET Method for viewing detail of an employee 

### Department Api's
    1 - http://127.0.0.1:8000/api/v1/departments/ --> GET Method to list all departments
    2 - http://127.0.0.1:8000/api/v1/departments/ --> POST Method to new department
    3 - http://127.0.0.1:8000/api/v1/departments/<department-id>/ --> for viewing detail and team of department

### Team Api's
    1 - http://127.0.0.1:8000/api/v1/team/  --> GET Method to list all team
    2 - http://127.0.0.1:8000/api/v1/team/create/ --> POST Method to new team

### Objective Api
    1 - http://127.0.0.1:8000/api/v1/objectives/create/ --> POST Method to new objective
    2 - http://127.0.0.1:8000/api/v1/objectives/<objective-id>/ --> GET Method for viewing detail of objective

### KeyResuls Api
    1 - http://127.0.0.1:8000/api/v1/key/create/ --> POST Method to new key

## Model Schema
##### I have used Django ORM to achieve DB goals.
##### To achieve the assessment goal and depending on my understanding with the assessment and also keeping django(python) specification standard, i have created these Models :
    Employee Model
    Department Model
    Team Model
    Member Model
    Objective Model
    KeyResult Model
#### For Employee, Team & Member Model Schema. Go To :
    https://github.com/ankitmlive/analytics-be/blob/master/employees/models.py
#### For Department Model Schema, Go to :
    https://github.com/ankitmlive/analytics-be/blob/master/department/models.py
#### For Objective & KeyResult Model Schema, Go to :
    https://github.com/ankitmlive/analytics-be/blob/master/objectives/models.py

#### Model Features :
    1 - Employee & Department are unique entity
    2 - Team has a unuque Lead related with one-to-one with employee table
    3 - For linking team member to employee, i have used django through table mechanism.
        (when we have to use extra information in any model, django allows us to do it with through table)
    4 - objective are assigned to employee, so created a ForeignKey relation between Employee & Objective 
        (because it is based on requirements if only one objective can be assigne to employee of multiple.)
    5 - KeyResult are related with objective with ForeignKey to hold objective status.
        (it is based on requirements, if only two identity (Pending & Complete), we can solve it in the same table with a boolean flag)
    6 - Member & Team relation are also requirement based, There are multiple scenario :
        1 - an employee can be added only one team
        2 - an employee can be added in multiple team
        3 - multiple employee can be added in multiple team
    so constraints are not applied yet to Member Table

## Api's for UI explantion

#### 1 - Use Home Api to fullfill the api requirement of first image card UI, where all objectives will be shown with status
#### 2 - When click on (objectives on track) card we will fetch all departments with 1st api of Department api, It will return all the department object with employee and objective count to show colored status and pop-up window on department cards.
#### 3 - When click on any department card we will fetch the department details using 3rd api of department api's, which will return all the child   teams in department with team lead. It will fullfill second pirtures requirements.

## Database
##### For Development & Testing Purpose , Django comes with a lightweight & convenient SQLite Database, which makes life easier for testing purpose, in this repo i have pushed a .sqlite file with dummy data that will make it easy to test this app, however i have implemneted PostgreSQL setting in project setting, it will reruire "psycopg2" library on host.
##### To connect with PostgreSQL goto analytics->settings->DATABASES and switch the default code and also provide DB SERVER Details.