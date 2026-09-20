✌🏽 Expense Tracker API

A secure, stateless REST API for tracking personal expenses, built with Python and Django REST Framework. This repository is a submitted solution to the [Roadmap.sh Expense Tracker API Project](https://roadmap.sh/projects/expense-tracker-api).

## Features
*   **User Authentication:** Secure sign-up and login endpoints using JSON Web Tokens (JWT).
*   **Data Isolation:** Relational database design ensures users can only access their own expense records.
*   **CRUD Operations:** Full Create, Read, Update, and Delete functionality for expenses.
*   **Advanced Filtering:** Query parameters allow filtering expenses by timeframes (past week, past month, last 3 months) or custom start and end dates.
*   **Data Integrity:** Strict category enforcement (Groceries, Leisure, Electronics, Utilities, Clothing, Health, Others) at the database level.

## Tech Stack
*   **Backend:** Python, Django, Django REST Framework
*   **Authentication:** djangorestframework-simplejwt
*   **Database:** SQLite (Development)

## Local Setup

1. **Clone the repository:**
   git clone <your-github-repo-url>
   cd ExpenseTrackerAPI

2. **Create and activate a virtual environment:**
   python -m venv venv
   source venv/Scripts/activate  # Windows
   # source venv/bin/activate    # macOS/Linux

3. **Install dependencies:**
   pip install django djangorestframework djangorestframework-simplejwt django-filter

4. **Run database migrations:**
   python manage.py migrate

5. **Start the development server:**
   python manage.py runserver

