# Gematria Calculator

## Overview
This project is a web-based Gematria Calculator that allows users to input Hebrew text and calculate its Gematria value. Gematria is an alphanumeric code of assigning a numerical value to a name, word or phrase based on its letters. This application uses the Hebrew alphabet and traditional Gematria values.

## Features
- Web interface for easy input of Hebrew text
- Server-side calculation of Gematria values
- Supports both standard Hebrew letters and sofith (final) forms
- Responsive design for use on various devices

## Technologies Used
- Backend: Python with Flask framework
- Frontend: HTML, CSS, JavaScript
- API: RESTful API for Gematria calculations

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Steps
1. Clone the repository:
   git clone https://github.com/ohadbenisti/gematria-calculator.git
   cd gematria-calculator

2. Install the required dependencies:
   pip install flask

3. Run the application:
   python app.py

4. Open a web browser and navigate to `http://127.0.0.1:5000/` to use the application.

## Usage
1. Enter Hebrew text in the input field on the web page.
2. Click the "Calculate" button.
3. The Gematria value will be displayed below the input field.

## Project Structure
- `app.py`: Main Flask application file containing the backend logic and Gematria dictionary
- `templates/index.html`: HTML template for the web interface
- `static/`: Directory for static files (CSS, JavaScript) if any

## How It Works
1. The `gimatriya_dict` in `app.py` contains the Gematria values for Hebrew letters, including final forms.
2. The `gimatria()` function calculates the total Gematria value of the input text.
3. When a POST request is made to `/calculate`, the server calculates the Gematria value and returns it as JSON.

## Contributing
Contributions to improve the Gematria Calculator are welcome. Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Contact
Ohad Benisti -ohadbenisti@gmail.com

Project Link: https://github.com/ohadbenisti/gematria-calculator

## Acknowledgements
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Hebrew Gematria](https://www.hebrew-gematria.com/)
