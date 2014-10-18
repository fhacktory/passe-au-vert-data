from datetime import time
import numpy as np
import pandas as pd

def xls_to_seconds(t):
    return t * 24 * 3600
for light_id in data.traffic_light_id.drop_duplicates():
    print light_id, ': ', xls_to_seconds(np.mean(data.loc[(data['traffic_light_id'] == light_id) & (data['changed_state'] == 3), 'created_at'].diff()))
for light_id in data.traffic_light_id.drop_duplicates():
    print light_id, ': ', xls_to_seconds(np.mean(data.loc[(data['traffic_light_id'] == light_id) & (data['changed_state'] == 1), 'created_at'].diff()))
