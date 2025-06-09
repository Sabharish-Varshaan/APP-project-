# Fitness Tracker

Fitness Tracker is a Django-based web application designed to help users monitor their fitness journey. It provides features such as active tracking, health monitoring, data analysis, and custom workout plans.

## Features

- **User Registration and Authentication**: Secure user registration, login, and logout functionality.
- **Active Tracking**: Track fitness activities like workout type, duration, calories burned, stress level, and hydration level.
- **Health Monitoring**: Record and monitor health metrics such as sleep time, heart rate, blood pressure, and weight.
- **Data Analysis**: Visualize fitness and health trends using interactive charts.
- **Custom Workouts**: Explore and select personalized workout plans based on difficulty levels.

## Project Structure

```
APP-project--master/
├── manage.py
├── fitness_tracker/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/
├── tracker/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   └── templates/
│       ├── base.html
│       ├── register.html
│       ├── login.html
│       ├── home.html
│       ├── active_tracking.html
│       ├── health_monitoring.html
│       ├── data_analysis.html
│       └── custom_workout.html
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd APP-project--master
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser for the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000`.

## Usage

- **Register**: Create a new account.
- **Login**: Access your personalized dashboard.
- **Track Activities**: Log your workouts and health metrics.
- **Analyze Data**: View trends and insights through interactive charts.
- **Explore Workouts**: Browse and select custom workout plans.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS (Dark Theme), JavaScript
- **Database**: MySQL
- **Charts**: Chart.js
- **Styling**: Crispy Forms with Bootstrap 4

## Screenshots

### Home Page
![Home Page](#)
![image](https://github.com/user-attachments/assets/891f5380-5ead-4a72-b7e4-3471a96ad722)


### Data Analysis
![Data Analysis](#)
![image](https://github.com/user-attachments/assets/cbe0b853-46d8-4a0a-b2aa-647349370add)

### Custom Workouts
![Custom Workouts](#)
![image](https://github.com/user-attachments/assets/e9542203-188b-4498-bba1-f909f10fa9d1)


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Contact

For any inquiries, please contact:
- **Email**: sabharishvarshaans@gmail.com
