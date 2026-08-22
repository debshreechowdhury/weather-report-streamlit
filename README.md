# Weather Report App on Streamlit

This is a very simple weather report app built using Streamlit.

Prior to running this app, please ensure that you have created an account in the
openweathermap platform and collect the api key from the platform and save it in the
.env file of your project file, name the key OPENWEATHER_API_KEY in the .env file.

In your project's venv please install streamlit, requests and python-dotenv, refer the requirements.txt file for more details.

After completing the above, in your project's terminal simply execute: streamlit run weather_report.py
After executing, you can see the UI on a browser using the local url populated in the terminal (for example: http://localhost:8502), in the UI, you'll be asked to enter the name of a city, after entering the city name, either you can press enter or click on the "Get Weather Information" button to get the weather details of the city such as you'll  temperature (in celsius), humidity, wind speed, visibility, pressure and weather description. Apart from this, you'll see a temperature analysis bar chart that shows the current temperature, min temperature, max temperature and feels like temperature of the city.