Weather Data Collection System

A complete end-to-end DevOps project that collects real-time weather data from the OpenWeather API, processes it using Python, and stores timestamped results in AWS S3 for historical analysis.

This project demonstrates essential DevOps practices including:

External API Integration

Cloud Storage (AWS S3)

Infrastructure as Code (Terraform)

Secure Environment Management

Python Development

CI/CD readiness

Error handling & logging

Version control (Git + GitHub)

📘 1. Project Overview

The system performs the following tasks:

1️⃣ Reads city names and credentials from environment variables
2️⃣ Fetches real-time weather data using the OpenWeather API
3️⃣ Extracts temperature, humidity, and weather conditions
4️⃣ Adds a UTC timestamp
5️⃣ Stores data in AWS S3 as JSON files
6️⃣ Maintains directory structure:

weather/YYYY/MM/DD/HHMMSS_city.json


This lets you build historical weather datasets for analytics or dashboards.

🏗️ 2. Architecture Diagram
               ┌────────────────────┐
               │    User / Cron     │
               └─────────┬──────────┘
                         │ Triggers
                         ▼
                ┌────────────────────┐
                │   Python App       │
                │  (app.py)          │
                └─────────┬──────────┘
                          │
        ┌─────────────────┼─────────────────────┐
        ▼                 ▼                     ▼
┌───────────────┐  ┌───────────────┐   ┌───────────────────┐
│ Weather Client │  │ Data Processor│   │   S3 Uploader     │
│ OpenWeather API│  │ timestamping  │   │  boto3 library    │
└───────┬────────┘  └──────┬────────┘   └─────────┬────────┘
        │ API Response      │ JSON object          │
        ▼                   ▼                      ▼
                 ┌──────────────────────┐
                 │ AWS S3 Bucket       │
                 │ (Historical Storage)│
                 └──────────────────────┘

📂 3. Project File Structure
weather-devops-demo/
├── README.md
├── .env.example
├── requirements.txt
├── .gitignore
├── infra/
│   └── main.tf
├── src/
│   ├── app.py
│   ├── config.py
│   ├── utils.py
│   ├── weather_client.py
│   └── s3_uploader.py
└── tests/
    ├── test_weather_client.py
    └── test_s3_uploader.py


This structure cleanly separates:

Application logic (src/)

Infrastructure (infra/)

Tests (tests/)

Documentation (README.md)

🔧 4. Technologies Used
Component	Technology
Language	Python 3.x
API	OpenWeather API
Cloud	AWS S3
IaC	Terraform
SDK	boto3
Config	python-dotenv
HTTP	requests
Testing	pytest + moto
CI-ready	Git + GitHub
🛠️ 5. Setup Instructions
Step 1 — Clone the project
git clone https://github.com/<your-username>/weather-devops-demo.git
cd weather-devops-demo

Step 2 — Install dependencies
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt

Step 3 — Configure environment variables

Copy the example file:

cp .env.example .env


Fill in:

OPENWEATHER_API_KEY=your_api_key
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_REGION=us-east-1
S3_BUCKET_NAME=your-bucket
CITIES=London,New York,Tokyo
LOG_LEVEL=INFO


⚠️ Never commit .env to GitHub.

Step 4 — Run the application
python -m src.app


Expected output example:

Fetching weather for London...
Uploaded to s3://your-bucket/weather/2025/12/09/113005_london.json

☁️ 6. AWS S3 Output Structure

Each run generates files like:

weather/
 └── 2025/
     └── 12/
         └── 09/
             └── 113005_london.json


Example stored JSON:

{
  "city": "London",
  "timestamp": "2025-12-09T11:30:05Z",
  "temperature_f": 61.2,
  "humidity": 70,
  "conditions": "broken clouds",
  "raw": { ... }
}

🔨 7. Infrastructure as Code (Terraform)

Inside /infra/main.tf you have:

S3 bucket creation

Versioning

Lifecycle rules

Tags

Run:

cd infra
terraform init
terraform plan -var="bucket_name=your-bucket"
terraform apply -var="bucket_name=your-bucket"

🧪 8. Testing the Project

Run all tests:

pytest -q


Testing covers:

API client behavior

S3 uploads using moto mock

Error handling

🔄 9. CI/CD (Optional)

You can add GitHub Actions:

Automatic tests on every push

Auto-run app on a schedule (e.g., hourly)

Deployment workflows

(Ask me and I will generate the workflow file.)

🧩 10. Key Features Explained
✅ Multi-city support

Load unlimited cities via .env like:

CITIES=London,Delhi,Paris,Sydney

✅ Robust error handling

Retries

Timeout control

Logging

✅ Timestamped historical data

Optimized for analytics and future visualization.

✅ Highly scalable

Add more cities or more AWS services easily.

🧭 11. Future Improvements

Dockerize and deploy using AWS ECS or Lambda

Add SNS alerts for failure notifications

Add Athena + Glue database for SQL analytics

Build a visualization dashboard (Streamlit / Grafana)

Add CI/CD automation for Terraform

👨‍💻 Author

Thanusha
DevOps Engineer | AWS | Terraform | Python
GitHub: https://github.com/
<your-username>

🎉 12. Summary

This Weather Data Collection System is a complete DevOps-driven project demonstrating:

API consumption

Cloud data storage

Infrastructure as Code

Automation

Python engineering

Logging, retries, and proper error control

Structured project architecture

You can proudly submit or showcase this project as a real-world DevOps mini-project.
