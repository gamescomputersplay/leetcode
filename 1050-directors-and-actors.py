''' https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/
'''

import pandas as pd

def actors_and_directors(actor_director):
    actor_director = actor_director.groupby(["actor_id", "director_id"]).agg(count=("timestamp","count"))
    actor_director.reset_index(inplace=True)
    actor_director = actor_director[actor_director["count"] >= 3]
    return actor_director[["actor_id", "director_id"]]

if __name__ == "__main__":
    data = [[1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 4], [2, 1, 5], [2, 1, 6]]
    ActorDirector = pd.DataFrame(data, columns=['actor_id', 'director_id', 'timestamp']).astype({'actor_id':'int64', 'director_id':'int64', 'timestamp':'int64'})
    result = actors_and_directors(ActorDirector)
    print(result)
