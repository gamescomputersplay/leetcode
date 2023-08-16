''' https://leetcode.com/problems/rank-scores/
'''

import pandas as pd


def order_scores(scores):

    def addrank(group):
        nonlocal rank
        ranks = [rank for _ in range(len(group))]
        group["rank"] = ranks
        rank += 1
        return group

    rank = 1
    scores["rank"] = None
    
    scores = scores.groupby("score", sort=False).apply(addrank)
    scores.reset_index(drop=True, inplace=True)
    return scores[["score", "rank"]]

def order_scores_built_in(scores):
    scores.sort_values("score", ascending=False, inplace=True)
    scores["rank"] = scores["score"].rank(method="dense", ascending=False)
    return scores[["score", "rank"]]

if __name__ == "__main__":
    data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
    Scores = pd.DataFrame(data, columns=['id', 'score']).astype({'id':'Int64', 'score':'Float64'})
    result = order_scores(Scores)
    print(result)