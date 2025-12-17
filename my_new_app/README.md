# Django Project

## Requirements
- Python 3.x
- pip
- Make
- Uvicorn

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project
You can run the Django project using Uvicorn and Make:

### Using Make
1. Make sure to add the following targets in your `Makefile`:
   ```makefile
   run:
    	uvicorn <your_project_name>.asgi:application --host 0.0.0.0 --port 8000
   ```
2. Run the project:
   ```bash
   make run
   ```

### Directly Using Uvicorn
You can also run the project directly using Uvicorn:
```bash
uvicorn <your_project_name>.asgi:application --host 0.0.0.0 --port 8000
```

## Accessing the Application
Open your web browser and go to `http://127.0.0.1:8000/` to view the application.

## Additional Information
- Make sure your database is set up and migrated before running the server.
- Check your `.env` file (if applicable) for environment variables needed by the project.