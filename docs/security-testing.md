# CampusConnect Security Testing Report

## 1. Overview

**Project:** CampusConnect
**Testing Type:** Manual Web Application Security Testing
**Environment:** Local Development Environment
**Base URL:** http://127.0.0.1:8000/
**Framework:** Django
**Testing Scope:** Authentication and Authorization

## 2. Testing Objectives

- Verify authentication enforcement on protected endpoints.
- Verify session invalidation after logout.
- Test object-level authorization.
- Identify potential Insecure Direct Object Reference (IDOR) issues.
- Verify that users can access and modify only their own student records.

## 3. Test Cases and Results

| Test ID | Test Description | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| AUTH-01 | Access update endpoint without login | Redirect to login page | Redirected to login page | PASS |
| AUTH-02 | Access delete endpoint without login | Redirect to login page | Redirected to login page | PASS |
| AUTHZ-01 | User accesses own student record | Access allowed | Edit page opened | PASS |
| AUTHZ-02 | Send GET request to another user's update endpoint | Access denied | HTTP 404 | PASS |
| AUTHZ-03 | Send GET request to another user's delete confirmation endpoint | Access denied | HTTP 404 | PASS |
| AUTHZ-04 | User updates own student record | Update successful | Redirected to home; database verified | PASS |
| SESSION-01 | Logout invalidates current session | Session cookie removed | Cookie removed; session count decreased from 2 to 1 | PASS |

## 4. Security Observations

### 4.1 Authentication Enforcement

Protected student update and delete endpoints require authentication through Django's `login_required` decorator.

Unauthenticated requests are redirected to the login page.

### 4.2 Object-Level Authorization

The update and delete views filter student records using both the requested record ID and the currently authenticated user.

This prevents users from accessing another user's student record through direct object references.

### 4.3 Session Invalidation

After logout, the current session cookie was removed from the browser and the database session count decreased.

This indicates that Django successfully invalidated the current session.

## 5. Limitations

- Testing was performed only in a local development environment.
- Cross-user delete access was tested using a GET request only. Unauthorized POST deletion has not yet been independently verified.
- Only selected authentication and authorization endpoints were tested.
- No automated security scanning or penetration testing was performed during this phase.
- The absence of vulnerabilities in tested endpoints does not establish that the entire application is secure.

## 6. Conclusion

The initial authentication and authorization tests indicate that the tested student update and delete endpoints enforce login requirements and object-level ownership restrictions.

Users were able to access and update their own student records, while attempts to access another user's records were denied.

Further security testing is required to evaluate other application components, including input validation, file handling, session configuration, CSRF protection, and sensitive data exposure.