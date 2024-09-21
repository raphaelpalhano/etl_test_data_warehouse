import pytest
import pandas as pd
#from config.setup_module import setup_sqlalchemy_connection
from utils.etl_utils import data_collect
import os

@pytest.fixture(scope="session", autouse=True)
def extraction_data():
    #connection, engine = setup_sqlalchemy_connection()
    #california_housing = fetch_california_housing(as_frame=True)
    # Create table for California housing prices
    #connection.exec_driver_sql('''
    #    CREATE TABLE IF NOT EXISTS casas_california (
    #        MedInc FLOAT,
    #        HouseAge FLOAT,
    #        AveRooms FLOAT,
    #        AveBedrms FLOAT,
    #        Population FLOAT,
    #        AveOccup FLOAT,
    #        Latitude FLOAT,
    #        Longitude FLOAT,
    #       MedHouseVal FLOAT
    #    )
    #''')
    
    # Load the dataset
    #df = california_housing.frame
    
    # Use SQLAlchemy to load data into the table
    # queryResult = connection.exec_driver_sql('SELECT * FROM casas_california LIMIT 1')
    # df.to_sql('casas_california', engine, if_exists='replace', index=False)
    
    #yield connection, engine
    #connection.execute('DROP DATABASE IF EXISTS etl_database')
    #close_sqlalchemy_connection(engine, connection)

    # Extraction
    data = data_collect(os.path.join(os.getcwd(), 'src', 'data', 'kc_house_data.csv'))
    yield data








def test_transform_data_save_database(extraction_data):
    pd.set_option('display.float.format', lambda x: '%3.f' % x)
    df_test = extraction_data.copy()
    df_test['price_m2'] = df_test['price'] / df_test['sqft_lot']
    df_test['level'] = df_test['price'].apply(lambda x: 0 if x <= 321950
    else 1 if (x > 321950) & (x <= 450000) else 2 if (x > 450000) & (x <= 645000) else 3)
    df_test['dormitory_type'] = df_test['bedrooms'].apply(lambda x: 'studio' if x == 1
    else 'apartament' if x == 2 else 'house')
    df_test['year'] = pd.to_datetime(df_test['date']).dt.strftime('%Y')
    df_test['day'] = pd.to_datetime(df_test['date']).dt.strftime('%Y-%m-%d')
    df_test['week'] = pd.to_datetime(df_test['date']).dt.strftime('%Y-%m-%d')
    df_test.to_csv(os.path.join(os.getcwd(), 'src', 'data', 'kc_house_data_transform.csv'), index=False)

    df_transform = pd.read_csv(os.path.join(os.getcwd(), 'src', 'data', 'kc_house_data_transform.csv'))
    assert df_transform.shape == df_test.shape


    
    
