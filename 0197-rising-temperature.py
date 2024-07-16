''' https://leetcode.com/problems/rising-temperature/
'''

import pandas as pd


def rising_temperature(weather):
    # Sort, might be not sorted
    weather.sort_values("recordDate", inplace=True)

    # Calculate temperature difference between rows
    weather["temp_diff"] = weather['temperature'].diff()

    # Only keep rows from consequent days
    weather["day_diff"] = weather['recordDate'].diff().dt.days
    weather = weather[weather["day_diff"] == 1]

    # Return rows where temperature grew
    return weather[weather["temp_diff"] > 0][["id"]]

if __name__ == "__main__":
    data = [[1, '2015-01-01', 10], [2, '2015-01-02', 25], [3, '2015-01-03', 20], [4, '2015-01-04', 30]]
    weather = pd.DataFrame(data, columns=['id', 'recordDate', 'temperature']).astype({'id':'Int64', 'recordDate':'datetime64[ns]', 'temperature':'Int64'})
    days_with_rising_temperature = rising_temperature(weather)
    print(days_with_rising_temperature)
