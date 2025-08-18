# Dynamic Survey Platform

A flexible and user-friendly survey platform built with Django. Create, share, and analyze surveys with ease.

This platform allows you to create dynamic surveys with various question types, including single-choice, multiple-choice, and open-ended questions. You can then share the surveys with your audience and collect their responses. The platform also provides a simple and intuitive interface for analyzing the survey results.

## Features

*   **Dynamic Survey Creation:** Create surveys with different question types, including single-choice, multiple-choice, and open-ended questions.
*   **User-Friendly Interface:** A simple and intuitive interface for creating, sharing, and analyzing surveys.
*   **Secure and Scalable:** Built with Django, a secure and scalable web framework.
*   **Easy to Deploy:** Deploy the application to Render with ease.

## Tech Stack

*   **Backend:** Django, Python
*   **Frontend:** HTML, CSS, JavaScript
*   **Database:** SQLite (for development), PostgreSQL (for production)

## Installation and Setup

To get a local copy up and running, follow these simple steps.

### Prerequisites

*   Python 3.8 or higher
*   pip

### Installation

1.  Clone the repo
    ```sh
    git clone https://github.com/780Noman/Dynamic_Servay_Platform.git
    ```
2.  Navigate to the project directory
    ```sh
    cd Dynamic_survey_app
    ```
3.  Install the dependencies
    ```sh
    pip install -r requirements.txt
    ```
4.  Apply the migrations
    ```sh
    python manage.py migrate
    ```
5.  Run the development server
    ```sh
    python manage.py runserver
    ```

The application will be available at `http://127.0.0.1:8000/`.

## Usage

1.  **Create a survey:**
    *   Go to the admin panel at `http://127.0.0.1:8000/admin/`.
    *   Create a new `CustomerFeedback` object.
    *   Add questions to the survey.
    *   For each question, you can specify the question type (Text, BigText, Radio, Checkbox).
    *   For Radio and Checkbox questions, you need to add options.
2.  **Share the survey:**
    *   Go to the home page at `http://127.0.0.1:8000/`.
    *   You will see a list of all the surveys.
    *   Click on the survey you want to share.
    *   Share the URL of the survey with your audience.
3.  **View the results:**
    *   Go to the home page at `http://127.0.0.1:8000/`.
    *   Click on the "All Results" button.
    *   You will see a list of all the surveys.
    *   Click on the survey you want to view the results for.

## Deployment

This application is ready to be deployed to Render. Here are the steps to deploy it:

1.  **Create a new web service on Render:**
    *   Go to the Render dashboard and create a new web service.
    *   Connect your GitHub repository.
    *   Select the `Dynamic_Servay_Platform` repository.
2.  **Configure the web service:**
    *   **Name:** Choose a name for your web service.
    *   **Region:** Choose a region for your web service.
    *   **Branch:** Select the `main` branch.
    *   **Build Command:** `pip install -r requirements.txt`
    *   **Start Command:** `gunicorn feedback.wsgi:application`
3.  **Add environment variables:**
    *   `SECRET_KEY`: Your Django secret key.
    *   `DEBUG`: `False`
    *   `ALLOWED_HOSTS`: Your domain name (e.g., `www.example.com`).
4.  **Deploy the web service:**
    *   Click on the "Create Web Service" button.
    *   Render will automatically build and deploy your application.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.
