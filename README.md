ZenithHire is a full-stack recruitment platform designed to connect job seekers with recruiters in a structured hiring environment. The platform allows recruiters to post job opportunities and enables job seekers to search and apply for jobs through a centralized web interface.
The system is built using the Django web framework and implements role-based authentication, job management, and application tracking. The platform also integrates an automated email notification system that informs users during login and registration events.
The project demonstrates the implementation of authentication systems, relational database design, and real-world recruitment workflow automation.

Key Features
Role-Based Authentication
The platform supports three user roles.

Jobseeker:
    Register and create a professional profile
    Browse job listings
    Apply for available jobs

Recruiter:
    Post job opportunities
    Manage job postings
    View applicants for posted jobs

Admin:
    Platform monitoring through Django admin panel
    Manage users and job listings

Authentication is handled using Django's built-in authentication system with email-based login.

Email Notification System
    The platform integrates an email notification system that automatically sends messages when users:
    Register for a new account
    Log into the system
    This feature demonstrates backend event handling and communication systems within a web application.


System Architecture
ZenithHire follows the Model View Template (MVT) architecture used by Django.

User Request
     │
     ▼
URL Routing
     │
     ▼
Views (Business Logic)
     │
     ▼
Models (Database Interaction)
     │
     ▼
Templates (Frontend Rendering)
     │
     ▼
Response to User



Tech Stack
  Backend:
    Django
    Python
    
  Frontend:
    HTML
    CSS
    Bootstrap
    
  Database:
    SQLite (default Django database)

  Additional Functionalities:
    Django Email Backend
    Django Authentication System
    Role-based access control



Application Workflow:
User Registration
    A new user registers using the signup form.
    The user selects their role (Jobseeker or Recruiter).
    The system sends an email confirmation.
    The user can now log in.

Job Posting
    Recruiters log into the recruiter dashboard.
    Recruiters create a new job posting.
    The job becomes visible to job seekers.

Job Application
    Jobseekers browse available jobs.
    Jobseekers apply for suitable jobs.
    Recruiters can view applicants for each job posting.



Security Implementation
    Django authentication system
    Password hashing
    Role-based access control
    Protected views using login validation
    Form validation for user input


Learning Outcomes
    Through this project, the following concepts were implemented:
    Full stack web development using Django
    Role-based authentication systems
    Relational database modeling
    Email notification systems
    Backend logic implementation
    Real-world recruitment workflow design
