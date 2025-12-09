# Weather Data Collection System

## 📌 Overview

This project is a **Weather Data Collection System** built using core DevOps and cloud concepts. It fetches real-time weather information from the **OpenWeather API**, processes it using Python, and stores the results in **AWS S3**. Infrastructure is managed using **Terraform**, and the system includes proper error handling, environment management, and version control.

---

## ⭐ Features

* Fetches real-time weather data for **multiple cities**.
* Retrieves **temperature (°F)**, **humidity**, and **weather conditions**.
* Automatically uploads data as **JSON files** to AWS S3.
* Creates **timestamped historical records**.
* Implements **clean architecture** in Python.
* Environment variables handled via `.env`.
* Infrastructure as Code using **Terraform**.

---

## 🏗️ Architecture Diagram

```
                +---------------------------+
                |     OpenWeather API       |
                +--------------+------------+
                               |
                               v
                    +----------+---------+
                    |   Python Script    |
                    | (weather_fetcher)  |
                    +----+----------+----+
                         |          |
                         v          v
              +----------+--+   +---+----------------+
              |  Process Data |   | Format  JSON      |
              +----------+----+   +------------------+
                         |
                         v
                +--------+--------+
                |   AWS S3 Bucket |
                | (Store Weather) |
                +-----------------+
```

---

## 📂 Project Structure

```
weather-data-collection-system/
│
├── main.py
├── weather_fetcher.py
├── utils.py
├── requirements.txt
├── README.md
├── .env.example
│
├── tests/
│   └── test_weather_fetcher.py
│
└── terraform/
    ├── main.tf
    ├── variables.tf
    ├── outputs.tf
    └── provider.tf
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/weather-data-collection-system.git
cd weather-data-collection-system
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure your `.env` file

Create a new `.env` file:

```
OPENWEATHER_API_KEY=your_api_key_here
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=ap-south-1
S3_BUCKET_NAME=your-bucket-name
CITIES=London,New York,Tokyo
```

---

## ▶️ Running the Application

Run the main script:

```bash
python main.py
```

Expected Output:

* Weather printed in terminal
* JSON files uploaded to S3 bucket

---

## ☁️ Terraform Deployment

Navigate to Terraform folder:

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

This will create:

* S3 bucket
* IAM policy
* IAM user

---

## 🧪 Running Tests

```bash
pytest
```

Expected: All tests should pass ✔️

---

## 📘 Technologies Used

* Python 3.x
* AWS S3
* Terraform
* Requests
* Boto3
* Python-dotenv
* Git & GitHub

---

## 🔗 Submit Required Artifacts

You must submit:

* Architectural Diagram
* GitHub Repository Link

---

## ✨ Author

Thanusha — Weather Data Collection System Project

---
