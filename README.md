# 📬 dockerized-flask-notification-service

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker)](https://docker.com)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-Pipeline-2088FF?style=for-the-badge)](ci/)

Dockerized Multi-Channel Notification Dispatcher Service (Email, Webhook, SMS mock) with CI/CD.

## Features
- **Strategy Pattern:** Decoupled dispatchers for Email, Webhooks, and SMS.
- **Containerized:** Lightweight multi-stage Docker build ready for AWS/GCP.
- **Continuous Integration:** Automated pipeline verifying builds on every commit.
