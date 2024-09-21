import pytest
from config.setup_module import setup_connection, close_connection

@pytest.fixture(scope="session", autouse=True)
def db_connection():
    con, cs = setup_connection()
    yield con, cs
    close_connection(con, cs)


def test_create_database(db_connection):
    con, cs = db_connection

    cs.execute("CREATE WAREHOUSE IF NOT EXISTS test_warehouse")
    con.commit()

    cs.execute("USE WAREHOUSE test_warehouse")

    cs.execute("CREATE DATABASE IF NOT EXISTS test_database")
    con.commit()
    
    cs.execute("USE DATABASE test_database")

   # validte database created
    # Validate database creation
    cs.execute("SHOW DATABASES LIKE 'test_database'")
    result = cs.fetchone()
    assert result is not None, "The database 'test_database' was not created"

    # Validate schema creation (default PUBLIC schema)
    cs.execute("SHOW SCHEMAS IN DATABASE test_database")
    schema_result = cs.fetchone()
    assert schema_result is not None, "No schema found in 'test_database'"

    # Cleanup
    cs.execute("DROP DATABASE IF EXISTS test_database")
    con.commit()

    cs.execute("DROP WAREHOUSE IF EXISTS test_warehouse")
    con.commit()



