# SOC Alert Triage Lab

Cybersecurity laboratory simulating the alert triage process performed by Security Operations Center (SOC) analysts.

This project demonstrates how security alerts can be analyzed and classified based on severity and indicators of suspicious activity.

The goal is to simulate the workflow of a SOC Level 1 analyst when receiving alerts from monitoring systems.

---

## Objective

Simulate the alert triage process used in SOC environments to determine the severity of security events and suggest investigation actions.

This project focuses on:

- Alert classification
- Suspicious activity identification
- SOC Level 1 triage workflow

---

## Technologies Used

Python  
Log Analysis  
Security Monitoring  
Incident Response Concepts  

---

## Project Structure
```
soc-alert-triage-lab
│
├── alerts
│ └── sample_alerts.txt
│
├── analysis
│ └── triage_engine.py
│
├── reports
│ └── triage_report.md
│
└── README.md


---

## SOC Alert Triage Workflow

Alert Generated
│
▼
Alert Analysis
│
▼
Severity Classification
│
▼
Recommended Action


This workflow represents the typical process used by SOC analysts when triaging alerts from monitoring tools such as SIEM, EDR, or XDR platforms.

---

## Example Alerts

Example input alerts used in this project:

Alert: Multiple failed login attempts
User: admin
Attempts: 12
IP: 185.220.101.12

Alert: Suspicious PowerShell execution
Process: powershell.exe
Command: whoami

Alert: Normal user login
User: employee01
IP: 192.168.1.10


---

## Example Output

Severity: High
Action: Possible brute force attack

Severity: Medium
Action: Suspicious PowerShell execution

Severity: Low
Action: Likely normal activity


---

## Severity Classification Logic

High Severity
- Multiple failed login attempts
- Potential brute force attack

Medium Severity
- Suspicious command execution
- PowerShell activity

Low Severity
- Normal user login activity

---

## Use Case

This project demonstrates how analysts can automate part of the alert triage process in SOC environments.

It helps simulate how alerts are analyzed and prioritized before deeper investigation.

---

## Learning Outcomes

This lab helps develop skills in:

- SOC alert triage
- Security event classification
- Log analysis
- Python automation for cybersecurity

---

## Author

José Barbosa Gomes Neto

Cybersecurity student focused on Security Operations Center (SOC), Threat Detection and Incident Response.

GitHub:  
https://github.com/sejosegomesneto-creator

