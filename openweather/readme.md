# OpenWeather


- Endpoint api.openweathermap.org
- Example of API call:
api.openweathermap.org/data/2.5/weather?q=London,uk&APPID={API_key}
- API documentation https://openweathermap.org/api
- Air pollution API https://openweathermap.org/api/air-pollution
- http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_key}

Example API response

{
  "coord":[
    50,
    50
  ],
  "list":[
    {
      "dt":1605182400,
      "main":{
        "aqi":1
      },
      "components":{
        "co":201.94053649902344,
        "no":0.01877197064459324,
        "no2":0.7711350917816162,
        "o3":68.66455078125,
        "so2":0.6407499313354492,
        "pm2_5":0.5,
        "pm10":0.540438711643219,
        "nh3":0.12369127571582794
      }
    }
  ]
}

Fields in API response

coord Coordinates from the specified location (latitude, longitude)
list
dt Date and time, Unix, UTC
main
main.aqi Air Quality Index. Possible values: 1, 2, 3, 4, 5. Where 1 = Good, 2 = Fair, 3 = Moderate, 4 = Poor, 5 = Very Poor.
components
components.co Сoncentration of CO (Carbon monoxide), μg/m3
components.no Сoncentration of NO (Nitrogen monoxide), μg/m3
components.no2 Сoncentration of NO2 (Nitrogen dioxide), μg/m3
components.o3 Сoncentration of O3 (Ozone), μg/m3
components.so2 Сoncentration of SO2 (Sulphur dioxide), μg/m3
components.pm2_5 Сoncentration of PM2.5 (Fine particles matter), μg/m3
components.pm10 Сoncentration of PM10 (Coarse particulate matter), μg/m3
components.nh3 Сoncentration of NH3 (Ammonia), μg/m3
