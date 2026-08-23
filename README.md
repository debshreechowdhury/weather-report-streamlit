# Weather Report App on Streamlit

This is a very simple weather report app built using Streamlit.

# Getting Started

## Prerequisites

    Python 3.9+

    Git

    Prior to running this app, please ensure that you have created an account in the
    openweathermap platform and collect the api key from the platform and save it in the
    .env file of your project file, name the key OPENWEATHER_API_KEY in the .env file.

## Installation

### Clone the repo

git clone https://github.com/debshreechowdhury/weather-report-streamlit.git

cd weather-report-streamlit

### Create and activate a virtual environment

python3 -m venv .venv

source .venv/bin/activate   # macOS/Linux

.\.venv\Scripts\Activate.ps1  # Windows PowerShell

### Install dependencies

pip install -r requirements.txt

### Running the App

streamlit run weather_report.py

Then open your browser at http://localhost:8501.

## Usage
 In the UI, you'll be asked to enter the name of a city, after entering the city name, either you can press enter or click on the "Get Weather Information" button to get the weather details of the city such as temperature (in celsius), humidity, wind speed, visibility, pressure and weather description. Apart from this, you'll see a temperature analysis bar chart that shows the current temperature, min temperature, max temperature and feels like temperature of the city.

## License
This project is licensed under the MIT License. See the LICENSE file for details.