
# Automated UofT Course Enrollment

## Overview

This project automates the tedious and time-consuming task of monitoring and enrolling in courses at the University of Toronto (UofT). Designed initially for non-degree students who face long waitlists, this Python script uses Selenium and Chrome WebDriver to navigate UofT's ACORN enrollment system, constantly checking for course availability. When a spot opens, it enrolls the user automatically and sends an email notification. The script is designed to run 24/7 on an AWS EC2 instance.

## Features

- **Secure Login:** Safely logs into ACORN using environment variables for credentials.
- **Automated Navigation:** Automatically navigates to the desired courses' enrollment pages.
- **Real-time Monitoring:** Refreshes the page every 30 seconds to check for course availability.
- **Instant Enrollment:** Enrolls in the course immediately when a spot becomes available.
- **Email Notification:** Sends an email to notify the user of successful enrollment.
- **Cloud-based:** Runs on AWS EC2 to ensure constant uptime.

## Technology Stack

- Python
- Selenium WebDriver
- AWS EC2
