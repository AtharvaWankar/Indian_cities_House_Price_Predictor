import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price_delhi(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    d = np.zeros(len(__data_columns))
    d[0] = sqft
    d[1] = bath
    d[2] = bhk

    if loc_index >= 0:
        d[loc_index] = 1

    return round(__model.predict([d])[0], 2)

def get_location_names_delhi():
    return __locations

def load_saved_artifacts_delhi():
    global __data_columns
    global __locations
    global __model

    with open("./artifacts_delhi/columns_delhi.json", 'r') as f:
        __data_columns = json.load(f)['data_columns_delhi']
        __locations = __data_columns[3:]  # Extracting location names from data_columns

    if __model is None:
        with open("./artifacts_delhi/delhi_home_prices_model.pickle", 'rb') as f:
            __model = pickle.load(f)

if __name__ == '__main__':
    load_saved_artifacts_delhi()
    print(get_location_names_delhi())
    print(__data_columns)
    print(__locations)

    print(get_estimated_price_delhi('Noida', 4000, 4, 2))
