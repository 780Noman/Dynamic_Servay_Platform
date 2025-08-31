---
title: Dynamic Survey App
emoji: 📝
colorFrom: indigo
colorTo: purple
sdk: docker
pinned: false
---

# Dynamic Survey Application

[![Hugging Face Spaces](https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/Nomi78600/dynamic-survey-app)

A robust and deployable web application built with Django that allows for the creation, administration, and analysis of dynamic surveys.

## Live Demo

You can view a live demo of this application deployed on Hugging Face Spaces:
[https://huggingface.co/spaces/Nomi78600/dynamic-survey-app](https://huggingface.co/spaces/Nomi78600/dynamic-survey-app)

## Key Features

- **Custom Surveys:** Create unique surveys with multiple question types, including text fields, radio buttons, and checkboxes.
- **Dynamic Interface:** A clean and simple interface for users to respond to surveys.
- **Results Visualization:** View aggregated results for each survey to gather insights.
- **Production Ready:** Securely configured and containerized with Docker for reliable deployment.
- **Automated Admin Creation:** Superuser is created automatically in production environments via environment variables.

## Technology Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript (with Chart.js for visualization)
- **Database:** SQLite
- **Deployment:** Docker, Gunicorn, Whitenoise

## Local Development Setup

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YourUsername/your-repo-name.git
    cd your-repo-name
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a local superuser:**
    ```bash
    python manage.py createsuperuser
    ```
    (Follow the prompts to create your local admin account.)

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000`.

## Usage

-   Access the admin panel at `/admin` to log in and create new surveys and questions.
-   The main page `/` lists all available surveys for users to take.
-   View the results of a survey by navigating to `/results/<survey_id>`.

## Deployment

This application is configured for deployment on Hugging Face Spaces using Docker. The `entrypoint.sh` script handles database migrations and automated admin user creation based on the following environment variables (secrets):
-   `SECRET_KEY`
-   `ALLOWED_HOSTS`
-   `CSRF_TRUSTED_ORIGINS`
-   `DJANGO_SUPERUSER_USERNAME`
-   `DJANGO_SUPERUSER_EMAIL`
-   `DJANGO_SUPERUSER_PASSWORD`
