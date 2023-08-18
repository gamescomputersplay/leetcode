''' https://leetcode.com/problems/immediate-food-delivery-i/
'''

import pandas as pd

def food_delivery(delivery):
    result_value = 0
    if len(delivery) != 0:
        result_value = len(delivery[delivery["order_date"] == delivery["customer_pref_delivery_date"]]) * 100 / len(delivery)
    result_value = round(result_value, 2)
    result_df = pd.DataFrame([result_value], columns=["immediate_percentage"])
    return result_df

if __name__ == "__main__":
    data = [[1, 1, '2019-08-01', '2019-08-02'], [2, 5, '2019-08-02', '2019-08-02'], [3, 1, '2019-08-11', '2019-08-11'], [4, 3, '2019-08-24', '2019-08-26'], [5, 4, '2019-08-21', '2019-08-22'], [6, 2, '2019-08-11', '2019-08-13']]
    Delivery = pd.DataFrame(data, columns=['delivery_id', 'customer_id', 'order_date', 'customer_pref_delivery_date']).astype({'delivery_id':'Int64', 'customer_id':'Int64', 'order_date':'datetime64[ns]', 'customer_pref_delivery_date':'datetime64[ns]'})
    result = food_delivery(Delivery)
    print(result)
