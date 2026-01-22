# Basic-API-Test-Suite
Python-based API test suite for the endpoints of JSONPlaceholder. Demonstrates functional, negative, schema/contract, and performance testing using pytest and requests.

# Project Overview

This project is a Python-based API test suite for the /users endpoints of JSONPlaceholder, a free public API.

Skills demonstrated include:
-Functional testing (status codes, data correctness)
-Negative testing (non-existent resources)
-Schema / contract validation (required keys & data types)
-Performance testing (response time)

# Project Structure
   **test_users_basic.py**: GET requests, list validation
   **test_users_negative.py**: Negative testing
   **test_users_schema.py**: Schema / contract validation
   **test_users_performance.py**: Response time checks
   **requirements.txt**: Dependencies required to run the project.

# How to Run the Tests
1. Clone the repository:
   git clone https://github.com/<geanes85>/Basic-API-Test-Suite.git
   cd api_test_suite
2. Install dependencies:
   pip install -r requirements.txt
3. Run all tests:
   pytest -v

# Test Coverage
test_users_basic.py	# Validates GET requests for a single user and list of users, checks status codes and key data types
test_users_negative.py	# Ensures API handles invalid requests gracefully (non-existent users)
test_users_schema.py	# Confirms API responses contain all required fields and correct data types
test_users_performance.py	# Measures response time to ensure API performance (<500ms)
