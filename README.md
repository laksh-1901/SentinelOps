# SentinelOps

A lightweight Linux Server Monitoring and Health Dashboard built using **Python**, **Flask**, and **AWS**. SentinelOps provides real-time system monitoring, website health checks, service monitoring, resource threshold alerts, and application logging through a simple web interface.

---

## Features

### System Monitoring

* CPU Usage Monitoring
* Memory Usage Monitoring
* Disk Usage Monitoring
* System Uptime
* Hostname Information

### Service Monitoring

* Monitor Linux services
* Display service status
* Quickly identify stopped services

### Website Health Monitoring

* Check website availability
* Measure response status
* Monitor external service uptime

### Resource Threshold Alerts

* CPU usage alerts
* Memory usage alerts
* Disk usage alerts
* Automatic health checks

### Logging

* Application logging
* Event logging
* Error logging

---

## Tech Stack

### Backend

* Python 3
* Flask

### Libraries

* psutil
* requests
* python-dotenv

### Frontend

* HTML5
* Bootstrap
* Jinja2 Templates

### Deployment

* Ubuntu Server
* AWS EC2
* Gunicorn
* Nginx

### Version Control

* Git
* GitHub

---

## Project Structure

```text
SentinelOps/
│
├── app.py
├── requirements.txt
├── .env
│
├── modules/
│   ├── monitor.py
│   ├── services.py
│   ├── website_monitor.py
│   ├── health_checker.py
│   └── logger.py
│
├── templates/
│   └── index.html
│
├── static/
│
└── logs/
    └── sentinelops.log
```

---

## Features in Detail

### System Information

Displays:

* CPU Utilization
* Memory Usage
* Disk Usage
* Hostname
* Server Uptime

---

### Website Monitoring

Checks:

* Website availability
* HTTP response status
* Connectivity

Example:

```text
Google
Status : UP
HTTP Code : 200
```

---

### Linux Service Monitoring

Monitor important Linux services such as:

* nginx
* ssh
* cron
* apache2

Displays whether each service is:

* Running
* Stopped

---

### Automatic Resource Alerts

Generates alerts when:

* CPU usage exceeds threshold
* Memory usage exceeds threshold
* Disk usage exceeds threshold

Example:

```text
⚠ CPU Usage is above 80%
⚠ Disk Usage exceeded threshold
```

---

### Logging

Application logs are written to:

```text
logs/sentinelops.log
```

The log file stores:

* Application events
* Errors
* Resource alerts

---

## Installation

Clone the repository

```bash
git clone https://github.com/laksh-1901/SentinelOps.git
```

Enter the project directory

```bash
cd SentinelOps
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open

```text
http://127.0.0.1:5000
```

---

## AWS Deployment

The project is configured for deployment using:

* Ubuntu EC2
* Gunicorn
* Nginx
* Systemd

---

## Skills Demonstrated

* Python
* Flask
* Linux Administration
* AWS EC2
* Gunicorn
* Nginx
* Server Monitoring
* Linux Services
* Logging
* System Health Monitoring
* Website Monitoring
* Git & GitHub

---

## Future Improvements

* Email notifications
* Slack alerts
* Telegram integration
* CloudWatch integration
* Docker deployment
* Multi-server monitoring
* User authentication
* Historical performance charts
* Prometheus integration
* Grafana dashboard
* REST API
* Real-time monitoring using WebSockets

---

## Author

**Dhanalakshmi P**

GitHub: https://github.com/laksh-1901

---

## License

This project is developed for educational purposes and portfolio demonstration.
