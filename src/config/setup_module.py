import os
import snowflake.connector
from snowflake.connector.errors import DatabaseError, ProgrammingError
from sqlalchemy import create_engine


snowflake_account = os.environ['SNOWFLAKE_ACCOUNT']
snowflake_user = os.environ['SNOWFLAKE_USER']
snowflake_password = os.environ['SNOWFLAKE_PASSWORD']
snowflake_warehouse = os.environ['SNOWFLAKE_WAREHOUSE']
snowflake_database = os.environ['SNOWFLAKE_DATABASE']
snowflake_schema = os.environ['SNOWFLAKE_SCHEMA']
snowflake_role = os.environ['SNOWFLAKE_ROLE']


def setup_connection():
    try:
        con = snowflake.connector.connect(
            user=snowflake_user,       # <-------- Bad user
            password=snowflake_password,   # <-------- Bad pass
            account=snowflake_account  # <-------- This is correct
        )
        cs = con.cursor() # object to execute queries
    except DatabaseError as db_ex:
        if db_ex.errno == 250001:
            print(db_ex)
            print(f"Invalid username/password, please re-enter username and password...")
            # code for user to re-enter username & pass
        else:
            raise
    except Exception as ex:
        # Log this
        print(f"Some error you don't know how to handle {ex}")
        raise

    return con, cs

def setup_sqlalchemy_connection():
    try:
        engine = create_engine(
            # 'snowflake://<user_login_name>:<password>@<account_identifier>/<database_name>/<schema_name>?warehouse=<warehouse_name>&role=<role_name>'
            f'snowflake://{snowflake_user}:{snowflake_password}@{snowflake_account}/{snowflake_database}/{snowflake_schema}?warehouse={snowflake_warehouse}&role={snowflake_role}'
        )
    except ProgrammingError as db_ex:
        print(f"Programming error: {db_ex}")
        raise
    try:
        connection = engine.connect()
        return connection, engine
    except ProgrammingError as db_ex:
        print(f"Programming error: {db_ex}")
        raise

def close_sqlalchemy_connection(engine, connection):
    connection.close()
    engine.dispose()


def execute_query(cs, query):
    try:
        cs.execute(query)
        results = cs.fetchone()
        print(results[0])
    except ProgrammingError as db_ex:
        print(f"Programming error: {db_ex}")
        raise
        
def close_connection(con, cs):
    con.close()
    cs.close()