
Library Management System
==========================

This is a simple Library Management System built using HTML, CSS, Python, Flask, and MySQL. 
The system allows students to log in using their University Serial Number (USN). 
If the USN exists in the database, the system logs the login time and stores the USN in another table.

Features
--------

- **USN Authentication**: Checks if the entered USN exists in the database.
- **Login Time Recording**: Logs the login time and USN into a separate table.

Prerequisites
-------------

Before running this project, ensure you have the following software installed:

- **Python** (version 3.6 or higher)
- **Flask** (version 2.0 or higher)
- **MySQL** with **phpMyAdmin**
- **SQLAlchemy** (for database ORM)

### Python Libraries

Install the required Python libraries using pip:

```
pip install Flask
pip install SQLAlchemy
pip install MySQL-python
```

Setting Up the MySQL Database
------------------------------

1. **Create a Database**:
   Create a database in MySQL (you can use phpMyAdmin for this purpose). 
   Name the database as per your requirement, e.g., `library_management`.

2. **Create Tables**:
   Create two tables in the database:
   
   - **students**: This table should have at least the following fields:
     - `usn` (Primary Key)
     - `student_name`
     - `department`
   
   - **login_logs**: This table should have the following fields:
     - `id` (Primary Key, Auto Increment)
     - `usn`
     - `login_time`

3. **Populate the Students Table**:  
   Insert records into the `students` table, corresponding to the students allowed to log in.

Configuration
-------------

1. **Database Connection**:
   Update your Python code to connect to the MySQL database using SQLAlchemy. 
   Ensure that your connection string is correct. 
   It typically looks like this:

   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/library_management'
   ```

2. **Flask App**:
   Make sure the Flask app is correctly set up to handle HTTP requests.

Running the Application
------------------------

1. **Start the Flask Server**:
   Navigate to the project directory and run the Flask application:

   ```
   python app.py
   ```

2. **Access the Application**:
   Open your web browser and go to `http://127.0.0.1:5000/`.

3. **Login**:
   Enter a valid USN to log in and record the login time.

Additional Notes
----------------

- **Security**: This is a basic implementation. 
  For production, consider implementing proper security measures such as password hashing, 
  input validation, and HTTPS.
  
- **Error Handling**: Ensure that the application handles errors, 
  especially when connecting to the database or if the USN doesn't exist.

Contributing
------------

Feel free to contribute to the project by forking the repository and submitting pull requests. 
You can also open issues for feature requests or bugs.


