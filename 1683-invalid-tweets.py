''' https://leetcode.com/problems/invalid-tweets/
'''

import pandas as pd

def invalid_tweets(tweets):
    df = tweets[tweets["content"].str.len() > 15]
    df = df[["tweet_id"]]
    return df

if __name__ == "__main__":
    data = [[1, 'Vote for Biden'], [2, 'Let us make America great again!']]
    Tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id':'Int64', 'content':'object'})
    result = invalid_tweets(Tweets)
    print(result)
