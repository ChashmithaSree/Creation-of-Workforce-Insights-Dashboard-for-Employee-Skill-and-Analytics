# AI-Powered Workforce Management Automation System

A production-oriented, database-driven workforce management platform built with **FastAPI, MongoDB (PyMongo), React 19, TypeScript, Tailwind CSS, and JWT authentication**.

The system provides role-based access control, employee management, attendance tracking, leave management, shift scheduling, timesheets, payroll, performance evaluation, workforce analytics, and AI-powered insights.

---

## 🌐 Live Cloud Deployment

| Component                                | Link                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------- |
| 🚀 **Live Frontend Application**         | [Open Application](https://ai-powered-workforce-management.vercel.app)          |
| ⚙️ **Backend API**                       | [Open API](https://ai-powered-workforce-management.onrender.com)                |
| 📖 **Interactive Swagger Documentation** | [View API Docs](https://ai-powered-workforce-management.onrender.com/docs)      |
| 🩺 **Backend Health Check**              | [Check API Health](https://ai-powered-workforce-management.onrender.com/health) |

### 🔑 Demo Login Credentials

All demo accounts use the password `Password123!`.

| Role                    | Email                          | Password       | Access Scope                                                   |
| ----------------------- | ------------------------------ | -------------- | -------------------------------------------------------------- |
| **HR Administrator**    | `sarah.jenkins@company.com`    | `Password123!` | Organization management, payroll, audit logs, and AI assistant |
| **Engineering Manager** | `alexander.wright@company.com` | `Password123!` | Team-scoped approvals, attendance, timesheets, and performance |
| **Employee**            | `josiah.harris@company.com`    | `Password123!` | Personal profile, clock-in/out, leave requests, and timesheets |

> **Security note:** These credentials are intended for demonstration purposes only. Do not use default credentials or expose real user credentials in a production deployment.

---

## 📌 Table of Contents

* [System Architecture](#-system-architecture)
* [Technology Stack](#-technology-stack)
* [Key Features](#-key-features)
* [User Roles and Organizational Structure](#-user-roles-and-organizational-structure)
* [Project Structure](#-project-structure)
* [AI Features](#-ai-features)
* [Prerequisites](#-prerequisites)
* [Installation and Setup](#-installation-and-setup)
* [Running the Application](#-running-the-application)
* [Running Automated Tests](#-running-automated-tests)

---

## 🏗️ System Architecture

The application follows a modular monolithic architecture with a clear separation between the frontend, API routers, business logic, security, and database layers.

```text
                  ┌──────────────────────────────┐
                  │       React Frontend         │
                  │ React 19 + TypeScript        │
                  │ Tailwind CSS                 │
                  └──────────────┬───────────────┘
                                 │
                                 │ REST API + Bearer JWT
                                 ▼
                  ┌──────────────────────────────┐
                  │       FastAPI Backend        │
                  │  61 Endpoints / 14 Modules   │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │ Authentication & RBAC        │
                  │ HR / MANAGER / EMPLOYEE      │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │       Service Layer          │
                  │ Business Logic & Validation  │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │       MongoDB Database       │
                  │   workforce_management       │
                  └──────────────────────────────┘
```

### Architecture Highlights

* **Modular monolithic design:** Organizes functionality into independent modules within a single backend application.
* **RESTful APIs:** Exposes backend functionality through FastAPI endpoints.
* **JWT authentication:** Secures authenticated requests using bearer tokens.
* **Role-based access control (RBAC):** Restricts functionality according to HR, Manager, and Employee roles.
* **Service layer:** Separates business logic from API routing.
* **Database-driven operations:** Uses MongoDB and PyMongo for persistent data storage and aggregation.
* **Automated testing:** Uses Pytest to validate application functionality, authorization, and business rules.

---

## 🛠️ Technology Stack

| Layer                   | Technologies                       |
| ----------------------- | ---------------------------------- |
| **Frontend**            | React 19, TypeScript, Tailwind CSS |
| **Backend**             | Python, FastAPI                    |
| **Database**            | MongoDB, PyMongo                   |
| **Authentication**      | JWT, Argon2id password hashing     |
| **Data Validation**     | Pydantic                           |
| **Testing**             | Pytest                             |
| **Frontend Deployment** | Vercel                             |
| **Backend Deployment**  | Render                             |

---

## ✨ Key Features

### 🔐 Authentication and Authorization

* Secure login using JWT authentication.
* Password hashing using Argon2id.
* First-time account activation.
* Forgot-password and password-reset workflows.
* Role-based access control for HR, Managers, and Employees.
* Team-boundary verification for managers.

### 👥 Employee Management

* Create, view, update, and manage employee records.
* Search and filter employee information.
* Pagination for employee directories.
* Employee status management.
* User provisioning and duplicate-account validation.

### ⏱️ Attendance Management

* Employee clock-in and clock-out.
* Attendance history and record management.
* Working-hour and overtime calculations.
* Duplicate check-in prevention.
* Attendance anomaly detection.

### 🏖️ Leave Management

* Submit and manage leave requests.
* Approve or reject requests through authorized managers.
* Validate leave balances and overlapping requests.
* Deduct leave balances after approval.
* Restore leave balances when eligible requests are cancelled.

### 📅 Shift Management

* Create and manage shift definitions.
* Assign shifts to employees.
* View employee shift schedules.

### 📝 Timesheet Management

* Submit and update timesheets.
* Review timesheets through manager workflows.
* Track employee working hours.

### 💰 Payroll Management

* Manage payroll inputs.
* Calculate payroll statements.
* Provide authorized access to payroll information.

### 📊 Performance Management

* Record employee performance evaluations.
* Manage ratings and review information.
* Analyze performance data.

### 📈 Workforce Analytics and Dashboards

* Role-specific HR, Manager, and Employee dashboards.
* Live workforce metrics calculated from MongoDB data.
* Attendance and leave analytics.
* Workforce demographics and overtime analysis.
* Notification management.
* Administrative audit logs.

### 🤖 AI-Powered Capabilities

* Natural-language queries against authorized workforce data.
* Automated attendance insights.
* Workforce trend analysis.
* Six-month workforce forecasting with upper and lower confidence intervals.

---

## 👥 User Roles and Organizational Structure

The database seed generator creates **exactly 200 synthetic users** with organizational relationships.

| Role         | Number of Users | Permissions and Scope                                                                              |
| ------------ | --------------: | -------------------------------------------------------------------------------------------------- |
| **HR**       |               5 | Organization-wide administration, payroll inputs, audit logs, and workforce analytics              |
| **MANAGER**  |              10 | Team-scoped attendance, leave approvals, shift assignments, timesheets, and performance management |
| **EMPLOYEE** |             185 | Personal profile, attendance, leave requests, timesheets, and personal dashboard                   |
| **Total**    |         **200** | Synthetic users with connected organizational relationships                                        |

### Default Test Accounts

All seed accounts are initialized with the password `Password123!`.

| Role                     | Email                          |
| ------------------------ | ------------------------------ |
| **HR Administrator**     | `sarah.jenkins@company.com`    |
| **Engineering Director** | `alexander.wright@company.com` |
| **Engineering Manager**  | `elena.rostova@company.com`    |
| **Head of Data Science** | `marcus.chen@company.com`      |
| **Finance Manager**      | `olivia.taylor@company.com`    |
| **Sample Employee**      | `liam.smith@company.com`       |

You can also use other employee accounts generated by the seed script.

> **Note:** The live demo accounts and locally seeded accounts may differ depending on the database used by the deployment. Use credentials corresponding to the environment you are accessing.

---

## 📁 Project Structure

The backend is organized into routers, schemas, services, utilities, and database initialization modules.

```text
backend/
├── main.py
├── config.py
├── database.py
│
├── models/
│   └── base.py
│
├── schemas/
│   ├── auth.py
│   ├── user.py
│   ├── employee.py
│   ├── attendance.py
│   ├── leave.py
│   ├── shift.py
│   ├── timesheet.py
│   ├── payroll.py
│   ├── performance.py
│   ├── dashboard.py
│   ├── analytics.py
│   ├── notification.py
│   ├── audit.py
│   └── ai.py
│
├── routers/
│   ├── auth.py
│   ├── users.py
│   ├── employees.py
│   ├── attendance.py
│   ├── leave.py
│   ├── shifts.py
│   ├── timesheets.py
│   ├── payroll.py
│   ├── performance.py
│   ├── dashboards.py
│   ├── analytics.py
│   ├── notifications.py
│   ├── audit.py
│   └── ai.py
│
├── services/
│   ├── auth_service.py
│   ├── employee_service.py
│   ├── attendance_service.py
│   ├── leave_service.py
│   ├── shift_service.py
│   ├── timesheet_service.py
│   ├── payroll_service.py
│   ├── performance_service.py
│   ├── analytics_service.py
│   └── ai_service.py
│
├── utils/
│   ├── security.py
│   ├── permissions.py
│   └── helpers.py
│
├── seed/
│   └── seed_database.py
│
└── tests/
    └── ...
```

### Important Modules

| Module                  | Responsibility                                                          |
| ----------------------- | ----------------------------------------------------------------------- |
| `main.py`               | Initializes the FastAPI application and manages its lifecycle           |
| `config.py`             | Loads environment-based configuration using Pydantic Settings           |
| `database.py`           | Initializes the MongoDB client and database indexes                     |
| `schemas/`              | Defines request and response validation models                          |
| `routers/`              | Exposes REST API endpoints                                              |
| `services/`             | Implements business logic and database operations                       |
| `utils/security.py`     | Handles password hashing and JWT-related security operations            |
| `utils/permissions.py`  | Implements role-based permissions and team-boundary checks              |
| `utils/helpers.py`      | Provides shared calculations, audit logging, and notification utilities |
| `seed/seed_database.py` | Generates synthetic workforce data                                      |
| `tests/`                | Contains automated tests for application functionality                  |

---

## 🤖 AI Features

### 1. HR Database Assistant

**Endpoint:** `POST /ai/assistant`

Allows authorized users to ask natural-language questions about workforce data.

**Capabilities:**

* Interprets workforce-related questions.
* Retrieves relevant information from the database.
* Applies role-based access restrictions.
* Prevents unauthorized access to private employee records.

**Example questions:**

* How many employees are currently active?
* Which departments have the highest overtime?
* What are the attendance trends across teams?

Employee queries attempting to access another employee's private information must be denied.

### 2. Attendance Insights

**Endpoint:** `GET /ai/attendance-insights`

Analyzes attendance records to identify workforce patterns and potential anomalies.

**Capabilities:**

* Detects departmental overtime increases.
* Identifies clusters of chronic late arrivals.
* Calculates week-over-week attendance trends.
* Highlights changes in attendance stability.

### 3. Workforce Forecasting

**Endpoint:** `GET /ai/workforce-forecast`

Analyzes historical workforce data to estimate future staffing requirements.

**Capabilities:**

* Analyzes historical onboarding rates.
* Examines headcount and retention trends.
* Projects workforce requirements over six months.
* Provides upper and lower confidence intervals for forecasts.

> Forecasts are estimates based on historical data and should be interpreted alongside business context and data quality.



## ⚙️ Prerequisites

Before running the application locally, ensure the following are installed:

* **Python 3.11 or later**
* **MongoDB 6.0 or later**, running locally or available through MongoDB Atlas
* **Node.js and npm**, if running the React frontend locally
* **Git**, for cloning the repository



## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <your-repository-directory>
```

Replace the placeholders with your actual repository URL and directory name.

### 2. Install Python Dependencies

From the directory containing `requirements.txt`, run:

```bash
pip install -r requirements.txt
```

Using a virtual environment is recommended.

**Create a virtual environment:**

```bash
python -m venv .venv
```

**Activate it on Windows:**

```bash
.venv\Scripts\activate
```

**Activate it on macOS/Linux:**

```bash
source .venv/bin/activate
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Copy `.env.example` to `.env` and update the values for your local environment.

**Windows Command Prompt:**

```cmd
copy .env.example .env
```

**macOS/Linux:**

```bash
cp .env.example .env
```

Configure the required settings, including your MongoDB connection string and JWT-related secrets, according to the application's configuration.

For local MongoDB, the connection string may look like:

```env
MONGO_URI=mongodb://localhost:27017
```

Use the actual variable names expected by your application.

> **Security:** Never commit `.env` files, database credentials, JWT secrets, or production secrets to GitHub. Keep `.env.example` limited to placeholder values.

### 4. Initialize the Database

The seed script resets and populates the database with synthetic workforce records.

Run:

```bash
python -m backend.seed.seed_database --reset
```

The seed process is designed to generate:

* 200 synthetic users.
* 4,600 attendance records.
* Leave requests.
* Shift assignments.
* Timesheets.
* Payroll statements.
* Performance evaluations.

> **Warning:** The `--reset` option is intended for database initialization or testing. Review the script before running it because it may delete existing data in the target database.



## ▶️ Running the Application

### 1. Start the FastAPI Backend

From the repository root, run:

```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

The backend should be available at:

| Resource                | Local URL                      |
| ----------------------- | ------------------------------ |
| **API Base URL**        | `http://localhost:8000`        |
| **Swagger UI**          | `http://localhost:8000/docs`   |
| **ReDoc Documentation** | `http://localhost:8000/redoc`  |
| **Health Check**        | `http://localhost:8000/health` |

### 2. Start the React Frontend

Open a new terminal and navigate to the frontend directory containing `package.json`.

Install dependencies:

```bash
npm install
```

Start the development server using the script defined in your `package.json`. For a Vite-based application, the command is typically:

```bash
npm run dev
```

Configure the frontend API base URL to point to the local backend:

```text
http://localhost:8000
```

Use the environment variable name expected by your frontend configuration.

### 3. Access the Application

Once both the backend and frontend are running:

1. Open the frontend development URL in your browser.
2. Sign in using a suitable seeded test account.
3. Explore the features available to that account's role.



## 🧪 Running Automated Tests

The project includes **32 automated Pytest test cases** designed to validate core application functionality.

Run the complete test suite from the repository root:

```bash
python -m pytest tests/ -v
```

### Test Coverage

| Area                          | Coverage                                                                                        |
| ----------------------------- | ----------------------------------------------------------------------------------------------- |
| **Authentication**            | Login validation, password hashing, JWT generation, account activation, and password reset      |
| **Role-Based Access Control** | HR permissions, manager team boundaries, and employee privacy                                   |
| **Attendance**                | Clock-in/out, duplicate check-in prevention, working hours, overtime, and anomaly detection     |
| **Leave Management**          | Leave balances, overlapping requests, approvals, rejections, and cancellations                  |
| **Employee Management**       | User provisioning, duplicate prevention, search, pagination, and status changes                 |
| **Dashboards and Analytics**  | Database-driven metrics for HR, Managers, and Employees                                         |
| **AI Features**               | Natural-language workforce queries, access-control checks, attendance insights, and forecasting |

To run a specific test file, use:

```bash
python -m pytest tests/test_filename.py -v
```

Replace `test_filename.py` with the actual test file name.


## 🔒 Security Considerations

Security is an important part of the platform's design.

* Passwords are hashed using Argon2id rather than stored in plaintext.
* JWT bearer tokens are used to authenticate protected API requests.
* Role-based access control restricts access according to user roles.
* Manager permissions are scoped to their authorized teams.
* Employee information is protected by authorization checks.
* Environment variables are used to configure sensitive settings.
* Audit logging supports administrative traceability.

**Production deployment recommendations:**

* Replace default demo credentials with secure credentials.
* Use strong, unique secrets for JWT signing.
* Restrict database network access and use least-privilege database credentials.
* Configure HTTPS and secure frontend/backend communication.
* Apply rate limiting and appropriate login protections.
* Avoid exposing sensitive payroll, employee, or audit information in logs.
* Validate all AI-generated database operations and enforce authorization independently of the AI model.


## ☁️ Deployment

The application is deployed using the following services:

| Component       | Platform |
| --------------- | -------- |
| **Frontend**    | Vercel   |
| **Backend API** | Render   |
| **Database**    | MongoDB  |

### Live Links

* **Application:** https://ai-powered-workforce-management.vercel.app
* **Backend:** https://ai-powered-workforce-management.onrender.com
* **API Documentation:** https://ai-powered-workforce-management.onrender.com/docs
* **Health Check:** https://ai-powered-workforce-management.onrender.com/health

The deployed backend must be configured with the correct MongoDB connection string and environment variables. The frontend must use the deployed backend URL for production API requests.



## 🎯 Project Objectives

The primary objectives of this project are to:

* Automate common workforce management operations.
* Centralize employee and organizational data.
* Improve attendance, leave, shift, timesheet, and payroll workflows.
* Enforce secure, role-based access to workforce information.
* Provide actionable workforce analytics and dashboards.
* Use AI-assisted analysis and forecasting to support workforce planning.
* Maintain a modular, testable, and maintainable application architecture.




