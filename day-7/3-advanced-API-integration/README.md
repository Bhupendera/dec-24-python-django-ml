# **Advanced API Integration**

## **1. Introduction to Advanced API Integration**

### **Overview**
APIs (Application Programming Interfaces) play a vital role in connecting applications, enabling data exchange, and building scalable systems. 
---

## **2. Testing APIs in Different Environments**

### **2.1 Understanding Environments**

- **Development**: Local environment where the API is first built and tested.
  - Example: Running Flask locally on `http://127.0.0.1:5000`.
- **Staging**: A replica of production to test integration, workflows, and consistency.
  - Example: Running the API on a staging server like `http://staging.example.com`.
- **Production**: Live environment where the API is consumed by real users.
  - Example: `https://api.example.com` with production-ready configurations.

> **Why Different Environments?**
> - To safely test APIs without impacting live systems.
> - To identify issues early in a staging environment.
> - To allow developers to work in isolation while preparing production-ready APIs.

---

### **2.2 Managing Environment Variables**

Environment variables allow you to manage configurations, such as API keys, database URLs, and secret keys, securely without hardcoding them into your application.

#### **Flask Setup with Environment Variables**
1. Install `python-dotenv` to load environment variables:
   ```bash
   pip install python-dotenv
   ```
2. Create a `.env` file to store sensitive values:
   ```dotenv
   FLASK_ENV=development
   DATABASE_URL=sqlite:///dev.db
   SECRET_KEY=mysecretkey
   ```
3. Update `app.py` to load variables:
   ```python
   from flask import Flask
   from dotenv import load_dotenv
   import os

   load_dotenv()  # Load environment variables from .env

   app = Flask(__name__)
   app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
   app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

   @app.route('/')
   def home():
       return "Welcome to the API!"
   ```
4. Test the API by running the application:
   ```bash
   flask run
   ```
5. Confirm the environment variables are loaded correctly.
   - Open `http://127.0.0.1:5000`.
   - If no errors occur, the variables are loaded successfully.

---

#### **Django Setup with Environment Variables**
1. Install `python-decouple` for managing environment variables:
   ```bash
   pip install python-decouple
   ```
2. Create a `.env` file and add variables:
   ```dotenv
   DEBUG=True
   SECRET_KEY=mysecretkey
   DATABASE_URL=sqlite:///db.sqlite3
   ```
3. Update `settings.py` to load the variables:
   ```python
   from decouple import config

   SECRET_KEY = config('SECRET_KEY')
   DEBUG = config('DEBUG', cast=bool)
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': config('DATABASE_URL'),
       }
   }
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```
5. Confirm the setup by visiting `http://127.0.0.1:8000`.

---

### **2.3 Testing APIs Using Postman**

Postman is a tool for testing APIs by sending HTTP requests and receiving responses. It allows you to test different environments by setting variables.

1. **Setting Up Environments**:
   - Go to Postman and create a new **Environment**.
   - Add variables like `base_url`.

2. **Testing APIs**:
   - Send requests using `GET`, `POST`, `PUT`, and `DELETE` methods.
   - Example for `POST`:
     - URL: `{{base_url}}/employees`
     - Body (JSON):
       ```json
       {
           "name": "John Doe",
           "role": "Engineer"
       }
       ```

3. **Exporting and Importing Collections**:
   - Export a Postman collection:
     - Click **Collections > Export**.
     - Save the `.json` file.
   - Import a collection:
     - Go to **File > Import**.
     - Upload the exported `.json` file.

> **Why Export and Import Collections?**
> - Share API tests with teammates.
> - Save and version control test scripts.

---

### **2.4 API Testing**
1. **Step 1**: Build a Flask API with endpoints like:
   - `GET /employees` (Retrieve all employees).
   - `POST /employees` (Add a new employee).
2. **Step 2**: Test the endpoints in Postman.
   - Set up Development and Staging environments.
3. **Step 3**: Export the Postman collection and share it.
4. **Step 4**: Import the collection on another system.

---

## **3. Building APIs in Flask and Consuming Them in Django**

### **Learning Objectives**
- Build RESTful APIs in Flask.
- Consume Flask APIs in Django applications.
- Understand end-to-end integration workflows.

---

### **3.1 Building APIs in Flask**

1. **Setup Flask**:
   Install Flask:
   ```bash
   pip install flask
   ```
2. **Create Endpoints**:
   ```python
   from flask import Flask, request, jsonify

   app = Flask(__name__)
   employees = []

   @app.route('/employees', methods=['GET'])
   def get_employees():
       return jsonify(employees)

   @app.route('/employees', methods=['POST'])
   def add_employee():
       data = request.get_json()
       employees.append(data)
       return jsonify({"message": "Employee added successfully"}), 201

   if __name__ == '__main__':
       app.run(debug=True)
   ```
3. **Test in Postman**:
   - `GET /employees` should return an empty list initially.
   - `POST /employees` should add new employee data.

---

### **3.2 Consuming Flask APIs in Django**

1. **Install Requests Library**:
   ```bash
   pip install requests
   ```
2. **Django View to Consume Flask API**:
   ```python
   import requests
   from django.shortcuts import render

   def fetch_employees(request):
       response = requests.get('http://127.0.0.1:5000/employees')
       employees = response.json()
       return render(request, 'employees.html', {'employees': employees})
   ```
3. **Create a Template (`employees.html`)**:
   ```html
   <h1>Employees List</h1>
   <ul>
   {% for employee in employees %}
       <li>{{ employee.name }} - {{ employee.role }}</li>
   {% endfor %}
   </ul>
   ```
4. **Run the Django App** and confirm that data from the Flask API is displayed.

---

## **4. Integrating Flask and Django APIs**

### **Objective**
- Create a Flask API to send employee data.
- Build a Django app to fetch and display the data.

### **Steps**:
1. **Build the Flask API**:

2. **Fetch API Data in Django**:

3. **Test the Full Workflow**:


---

