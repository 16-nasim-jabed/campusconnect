# CampusConnect — Architecture Documentation

## 1. Project Overview
CampusConnect is a Django-based university management platform.

## 2. Technology Stack
- Backend: Python, Django
- Database: SQLite
- Frontend: HTML, CSS
- Authentication: Django Authentication System

## 3. Project Structure
- config/: Project configuration and root URLs
- accounts/: User registration, login, and profile management
- core/: Student records and related views
- templates/: HTML templates
- static/: CSS and static assets
- docs/: Project documentation

## 4. Request Lifecycle
1. User sends an HTTP request.
2. Django checks the URL configuration.
3. The matching view processes the request.
4. The view interacts with models when required.
5. Django renders a template or returns a response.

## 5. Authentication and Authorization
- Authentication identifies the logged-in user.
- Authorization determines what the user is allowed to access.
- Login protection uses Django's login_required decorator.
- Student update and delete views restrict access to the record owner.

## 6. Existing Security Controls
- Django password hashing.
- Login protection on student management views.
- Object-level ownership checks.
- CSRF tokens in POST forms.
- Django ORM is used for database queries, reducing the need for raw SQL.

## 7. Preliminary Security Observations
- The homepage currently displays all registered student records.
- Student registration currently creates a Student record without admin approval.
- Edit and Delete links are visible for all students, although backend ownership checks exist.

These observations require further testing and policy review.

## 8. Existing Test Coverage
- Unauthenticated access restrictions.
- Unauthorized access to another student's record.
- Authorized access to own record.
- Own-record update and deletion.

## 9. Testing Gaps
- Homepage data exposure.
- CSRF enforcement.
- Invalid form submissions.
- GET request behavior for deletion.