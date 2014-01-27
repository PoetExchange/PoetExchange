PoetExchange
============

This is a legacy repository for a project no longer under development. The repository remains mostly for referential purposes, and this document attempts to give a brief overview of what is present in the project.

## About PoetExchange

PoetExchange was being written as a web application which could be leveraged by students primarily in order to exchange used books, while allowing students to build more complete user profiles detailing their semester class schedule, extracurricular activities, and exchange other general campus-relevant information.

## Functionality

Functionality which was completed before work on the application was halted is detailed in this section.

#### Full complement of DB Models

This project includes a very feature rich set of database models, whith carfully planned relations. The models allow for the representation of a diverse array of activities and offerings on campus, and allow individual users to build profiles of themselves by declaring association with any activities or classes they may be involved with. Each user has a different profile each semester and all semesters for the user are persistently stored, so a complete running history of the user's on-campus involvement is available to recall at any time.

There is also a complete model set for representing academic courses and departments, which includes information on professors. Users who post books to exchange must associate them with an academic course, which is in turn associated with a Department and a Professor. This allows for the builing of an application which can quickly find books based on things students can remember, such as the professor, course name, or department.

The models can be viewed in the usual app-name/models.py

#### User registration and authentication

The user registration for PoetExchange is a 3 step process, the logic for which is implemented in users/views.py

- **Initial registration**: The user enters their school username and submits it. At this point, a confirmation code is generated, associated with the username in a validator object, and the object is written to storage. Then, the user's email is automatically built from the username, the activation code is used to build a link which recalls the validator, and the link is sent out to the user's email.
- **Email confirmaion**: The user logs into their email account and clicks the generated link. This link uses the confirmation code to recall the validator, which can then be used to confirm the vailidity of the user's email.
- **Main Registration**: If the confirmation code recalls a valid validator object, the user's main registration form is loaded. This allows the user to fill in the remainder of their account information, (e.g., password, full name) and any other elective information (profile information such as classes, extracurriculars, etc).

The authentication code is nothing unique to a Django project. This should be standard to anyone who has written authentication code in the framework.

#### Browsing of Departments, Classes, and Books

The browsing interface for Departments, Classes, and Books is implemented in academics/views.py

This interface and its accompanying templates handle the recalling and displaying of information for the models. Each model has a "modelnameDetail" view function, which passes the data provided by the instance of the model to the template. The templates implement these views in such a way that books can looked up with the following steps:

1. Find the desired Department, load the departmentDetail view
2. Of the Classes associated with the Department, find the desired Class and load the classDetail view
3. Of the Books associated with the Class, find the one you want and load the bookDetail view

This implementats a 3-click interface, where the user is at their desired destination within 3 page loads.
