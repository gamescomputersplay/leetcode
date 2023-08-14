''' https://leetcode.com/problems/big-countries/
'''

import pandas as pd

def big_countries(world):

    big_countries = world[["name", "population", "area"]]
    big_countries = big_countries[
        (big_countries['area'] >= 3_000_000) |
        (big_countries['population'] >= 25_000_000)
        ]

    return big_countries

if __name__ == "__main__":
    data = [['Afghanistan', 'Asia', 652230, 25500100, 20343000000], ['Albania', 'Europe', 28748, 2831741, 12960000000], ['Algeria', 'Africa', 2381741, 37100000, 188681000000], ['Andorra', 'Europe', 468, 78115, 3712000000], ['Angola', 'Africa', 1246700, 20609294, 100990000000]]
    World = pd.DataFrame(data, columns=['name', 'continent', 'area', 'population', 'gdp']).astype({'name':'object', 'continent':'object', 'area':'Int64', 'population':'Int64', 'gdp':'Int64'})
    
    result = big_countries(World)
    print(result)