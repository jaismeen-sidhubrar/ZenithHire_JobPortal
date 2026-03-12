# ZenithHire Job Portal

This project is a full-stack job portal built using Django that connects recruiters and job seekers through a structured recruitment platform.

The goal of this platform is to:

- Allow recruiters to post job opportunities
- Allow job seekers to explore and apply for jobs
- Provide role-based authentication for different users
- Manage job applications in a centralized system
- Send automated email notifications during authentication events

---

## Features

### User Authentication
- Single signup and login system
- Email and password based login
- Role-based user accounts
- Secure authentication using Django

Supported roles:
- Jobseeker
- Recruiter
- Admin

### Jobseeker Capabilities
- Create and manage profile
- Browse available job listings
- Apply for jobs posted by recruiters
- View applied jobs

### Recruiter Capabilities
- Recruiter dashboard
- Post new job openings
- Manage job listings
- View applicants for each job

### Admin Controls
- Manage users
- Monitor job postings
- Platform administration through Django Admin Panel

---

## Tools Used

- Python
- Django
- HTML
- CSS
- Bootstrap
- SQLite
- Django ORM
- Django Authentication System
- SMTP Email Service

---

## Project Pipeline

1. User registers on the platform.
2. User selects their role (Jobseeker or Recruiter).
3. Email notification is sent after signup.
4. User logs into the system using email and password.
5. System redirects users to their respective dashboards.

Recruiter workflow:

1. Recruiter logs in.
2. Recruiter posts job opportunities.
3. Jobs become visible to job seekers.

Jobseeker workflow:

1. Jobseeker logs in.
2. Jobseeker browses job listings.
3. Jobseeker applies for suitable jobs.
4. Recruiter can view the applicants for each job.

---

## System Architecture

The project follows Django's **MVT (Model View Template)** architecture.

User Request  
↓  
URL Routing  
↓  
Views (Business Logic)  
↓  
Models (Database Interaction)  
↓  
Templates (Frontend Rendering)  
↓  
Response Returned to User

---

## Learning Outcomes

This project demonstrates:

- Full stack web development using Django
- Role-based authentication systems
- Relational database modeling
- Backend logic implementation
- Job application workflow design
- Email notification integration

---

## Author

Jaismeen  
BE CSE (Artificial Intelligence)  
Chitkara University, Punjab
