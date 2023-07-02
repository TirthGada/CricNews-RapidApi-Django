Cricket Data Project

This project is a web application that displays live cricket data using the Cricket Live Data API. It fetches data from the API and presents it in a user-friendly format.

Features

Displays live cricket match results, including date, match title, venue, result, and status.
Allows users to search for specific matches using the search functionality.
Technologies Used

Django: A high-level Python web framework used for backend development.
RapidAPI: An API marketplace used to access the Cricket Live Data API.
HTML/CSS: Used for the frontend design and layout.
JavaScript: Used for dynamic interactions on the frontend.
React: A JavaScript library used for building user interfaces (optional if you choose to implement React in your project).
Setup and Installation

Clone the repository:

git clone https://github.com/yourusername/cricket-data-project.git

Install the required dependencies:

pip install -r requirements.txt
Obtain an API key from RapidAPI by signing up for an account and subscribing to the Cricket Live Data API.
Replace the placeholder YOUR_RAPIDAPI_KEY in the code with your actual RapidAPI key

Run the Django development server:
python manage.py runserver


Open your web browser and navigate to http://localhost:8000 to access the cricket data application.
Usage

Upon visiting the homepage, the live cricket data will be fetched and displayed.
Use the search functionality to search for specific matches by entering relevant keywords.
Click on the match cards to view detailed information about each match.
Contributing

Acknowledgements

Cricket Live Data API by SportContentAPI: https://rapidapi.com/sportcontentapi/api/cricket-live-data

Bootstrap CSS framework: https://getbootstrap.com/
