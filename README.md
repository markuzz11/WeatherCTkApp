# WeatherCTkApp

## Description

WeatherCTkApp is an application for displaying weather information using the customtkinter (CTk) library and Object-Oriented Programming (OOP) pattern.

With this simple application, you can retrieve weather data for your desired city and country and also get the current time at the specified location.

## Installation

1. Download this repository to your device.
2. Install the required packages using the following command:
   ```
   pip install -r requirements.txt
   ```
3. Create a file named `keys.py`, and insert your API key from openweathermap.org as the value for the `owmkey` variable. Also, specify your email address as the value for the `mail` variable to enable geopy functionalities.

## Usage

To run the application, execute the following command:
```
python main.py
```

The application will be ready to use after the execution.


---

### P.S. Several encountered problems with CTk
1) 'no icon for toplevel window' and 'toplevel window is set back behind the upper root window':
https://github.com/tomschimansky/customtkinter/issues/1198
(I didn't risk changing anything in the source files, so I just leave the solution discusion here.)

2) problem converting python file to executable (This problem still being problem...)
In the documentation, the creators touch on this topic, but problems may remain after it, and many people on the network have various exceptions when converting files
