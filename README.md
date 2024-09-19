YeneTech E-Learning Platform
An YeneTech e-learning platform built using Django, allowing users to register, take courses, complete quizzes, and track progress. It supports multiple course categories, user roles, and rich content including videos and quizzes.

Features
User authentication (registration, login, logout, password reset)
User roles: Admin, Instructor, Student
Course management: Instructors can create, edit, and delete courses
Module-based course structure
Rich content support: Videos, PDFs, Quizzes, Assignments
Student progress tracking
Quiz system with auto-grading
Discussion forums for students
Responsive UI
Technologies Used
Django 4.x
Django REST Framework
PostgreSQL (or SQLite for development)
Bootstrap for frontend
Celery (for background tasks like email notifications)
Redis (for caching and task queue)
Installation
Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.x
Django 4.x
PostgreSQL (or SQLite for local development)
Redis (for background task management)
Steps
Clone the repository:
https://github.com/Hlinawondwossen/YeneTech
Set up a virtual environment:
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the dependencies:
pip install -r requirements.txt
Set up environment variables:

Create a .env file in the root directory with the following values:
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://user:password@localhost:5432/yourdb
EMAIL_HOST=smtp.yourmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email
EMAIL_HOST_PASSWORD=your-passwor
Set up the database:
python manage.py migrate
Create a superuser:
python manage.py createsuperuser
Run the development server:
Access the site at http://127.0.0.1:8000/.
API Documentation
If you are using Django REST Framework for API, you can access the API docs at http://127.0.0.1:8000/api/docs/.

Testing
To run the unit tests, execute:
python manage.py test
