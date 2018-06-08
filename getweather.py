from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location('irvine')
condition = location.condition
print(condition.text)
print(condition.temp)
# for forecast in forecasts:
#     print(forecast.text)
    # print(forecast.date)
    # print(forecast.high)
    # print(forecast.low)