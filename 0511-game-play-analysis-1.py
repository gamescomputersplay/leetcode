''' https://leetcode.com/problems/game-play-analysis-i/
'''

import pandas as pd

def game_analysis(activity):
    activity.sort_values("event_date", inplace=True)
    activity = activity.groupby(["player_id"]).agg("first")
    activity.reset_index(drop=False, inplace=True)
    activity.rename(columns={"event_date": "first_login"}, inplace=True)
    return activity[["player_id", "first_login"]]

if __name__ == "__main__":
    data = [[1, 2, '2016-03-01', 5], [1, 2, '2016-05-02', 6], [2, 3, '2017-06-25', 1], [3, 1, '2016-03-02', 0], [3, 4, '2018-07-03', 5]]
    Activity = pd.DataFrame(data, columns=['player_id', 'device_id', 'event_date', 'games_played']).astype({'player_id':'Int64', 'device_id':'Int64', 'event_date':'datetime64[ns]', 'games_played':'Int64'})
    result = game_analysis(Activity)
    print(result)
