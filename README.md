Use .ipynb file for verification locally as it contains the instruction to run the Ollama model on the same server as the application. 

# QA Bot System with LLM and Vector Database

**Note:** Use .py file for deployment. Below readme file details are given according to .py file.

This project implements a Question-Answering (QA) system using Large Language Models (LLM), embeddings, and a vector database. The system extracts text from PDFs, generates embeddings, stores them in a vector database, and retrieves relevant text chunks based on user queries. The architecture ensures scalability, performance, and security.

## Table of Contents
- [Architecture](#architecture)
- [Requirements](#requirements)
- [Setup and Installation](#setup-and-installation)
- [Deployment](#deployment)
- [Usage](#usage)
- [Performance Evaluation](#performance-evaluation)

## Architecture

Architecture Diagram and Explanation.pdf in source code

### Components
1. **Clients**: Web/Mobile Applications
2. **API Gateway**: Routes requests and provides load balancing.
3. **Security Layer**: Handles authentication, network security, encryption, and compliance monitoring.
4. **Infrastructure Layer**: Load balancer, auto-scaling, message queues, and cloud storage.
5. **Application Layer**: LLM Model, Embedding Generation Service.
6. **Data Layer**: Vector Database (Chroma/FAISS), Traditional Database.
7. **Monitoring & Logging Layer**: Monitoring and centralized logging.

## Requirements

- Docker
- Python 3.8+
- Virtualenv
- Google Cloud Platform (GCP) for cloud storage and security
- LangChain, FAISS, and Ollama packages
- PDF extraction libraries (PyPDF)

## Setup and Installation

### 1. Clone the Repository
```sh
git clone https://github.com/SunnySinghs/LLM.git
cd LLM
```

### 2. Create and Activate a Virtual Environment
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Environment Variables
Create a .env file and add the necessary environment variables:
```sh
GCP_PROJECT_ID = <gcp_project_id>
GCP_BUCKET_NAME = <gcp_bucket_name>
```

### 5. Set Up GCP Services
1. Cloud Storage: Create a bucket and upload your PDF files.
2. Security: Configure IAM roles and permissions.
3. Auto-scaling: Set up auto-scaling groups.


## Deployment

### 1. Dockerize the Application
Create a Dockerfile:
```sh
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

### 2. Build and Run the Docker Container
```sh
docker build -t LLM .
docker run -p 8000:8000 --env-file .env LLM
```

### 3. Deploy to GCP
**Google Kubernetes Engine (GKE)** : Deploy the Docker container to GKE.

We need to provide the URL of running Ollama model while generating the embeddings. Currently, it is assumed that the model is running on the same machine as the application.

## Usage(Needs to be develop)

### 1. API Endpoints:
1. **POST /upload** - Upload PDF files, create embedding and same in vector database
2. **POST /query** - Query the system with a question.

### 2. Querying the System:
1. Upload PDF files to the system.
2. Send a query to the system and get the relevant response.

## Performance Evaluation

1. **Load Testing**: Use tools like Apache JMeter to simulate multiple users and measure the system's performance.
2. **Monitoring**: Use Prometheus and Grafana to monitor system metrics.
3. **Logging**: Use the ELK stack (Elasticsearch, Logstash, Kibana) for centralized logging and analysis.




