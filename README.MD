
## PYPROJECT.TOML

**Install dependencies:**

```bash
pip install -e .
```

```bash
pip install -e .[dev]
```

**Create virtual environment:**

```bash
python -m venv .venv
```

**Activate virtual environment:**

```bash
. .venv/Scripts/Activate.ps1
```

**Deactivate virtual environment:**

```bash
deactivate
```

## Pytest

### Project Structure

The project uses Pytest for testing. The test files are located in the `src/tests/` directory. This structure allows for organized and maintainable test code.

### Configuration

The project uses a `pytest.ini` file for configuration:

### Command to run tests

```bash
pytest
```

## How works pytest

Pytest is a powerful and flexible testing framework for Python. It allows for the creation of tests with a simple and readable syntax. Here's a basic overview of how pytest works:

1. **Test Discovery**: Pytest automatically discovers and organizes test functions in your codebase. It looks for functions prefixed with `test_` or `Test` (class methods) and treats them as test cases.

2. **Test Execution**: Pytest executes these test functions and provides detailed output on the console. It categorizes test results as pass or fail.

3. **Assertions**: Pytest uses assertions to validate the expected behavior of your code. Common assertion functions include `assert`, `assertEqual`, `assertTrue`, and `assertFalse`.

4. **Fixtures**: Pytest allows for the use of fixtures, which are functions that provide data or setup/teardown logic for tests. Fixtures can be used to ensure that tests have the necessary resources before running.

5. **Parametrization**: Pytest supports parametrization, allowing you to run the same test with different inputs. This is useful for testing with multiple sets of data.


## Snowflake

### Project Structure

The project uses Snowflake for testing. The test files are located in the `src/tests/` directory. This structure allows for organized and maintainable test code.

### Configuration

The project uses a `snowflake.ini` file for configuration:

### Command to run tests

```bash
pytest
```

### How works Snowflake

Snowflake is a cloud-based data platform that provides a scalable and secure environment for data storage and processing. It offers a range of services including data warehousing, data lakes, and data streaming. Here's a basic overview of how Snowflake works:

1. **Data Storage**: Snowflake provides a distributed storage system that allows for the storage of large datasets across multiple nodes. This storage is designed to handle high volumes of data and provide fast access times.

2. **Data Processing**: Snowflake offers a range of data processing services including data warehousing, data lakes, and data streaming. These services allow for the processing of large datasets and the creation of reports and insights.

3. **Data Streaming**: Snowflake offers a range of data streaming services including data lakes, data warehouses, and data streaming. These services allow for the streaming of data in real-time and the creation of reports and insights.

### Python with Snowflake

Python can be used to interact with Snowflake through the use of the `snowflake-connector-python` library. This library provides a range of services including data warehousing, data lakes, and data streaming.

### Python with Snowflake

Python can be used to interact with Snowflake through the use of the `snowflake-connector-python` library. This library provides a range of services including data warehousing, data lakes, and data streaming.

### Hierarchy

warehouse
database
schema
table
view

0. **Warehouse**: A warehouse is a collection of data organized in a structured format. It is the top-level container in Snowflake.
1. **Database**: A database is a collection of data organized in a structured format. It is the top-level container in Snowflake.
2. **Schema**: A schema is a collection of data organized in a structured format. It is a container for tables and views.
3. **Table**: A table is a collection of data organized in a structured format. It is a container for data.
4. **View**: A view is a virtual table based on the result of a SQL query. It is a container for data.

### Snowflake Create warehouse with Python

Creating a warehouse in Snowflake using Python involves the following steps:

1. **Connect to Snowflake**: Use the `snowflake-connector-python` library to establish a connection to your Snowflake account.

2. **Execute SQL**: Use the connection to execute a SQL command that creates the warehouse.

3. **Commit the changes**: Ensure the changes are committed to make them permanent.

Here's a script demonstrating how to create a warehouse using Python:  

```python 
import snowflake.connector

# Configurações de conexão
config = {
    "user": "seu_usuario",
    "password": "sua_senha",
    "account": "seu_conta",
    "warehouse": "seu_warehouse",
    "database": "seu_banco_de_dados",
    "schema": "seu_esquema"
}

# Conexão com o Snowflake
con = snowflake.connector.connect(**config)

# Criação do warehouse
con.cursor().execute("CREATE WAREHOUSE IF NOT EXISTS test_warehouse")
con.commit()


```

### Query Data
Of course, you'll want to query your data at some point. It's easy to do that within the Python Connector too. To view values from the table, you can do so easily with the print command.

col1, col2 = conn.cursor().execute("SELECT col1, col2 FROM test_table").fetchone()
print('{0}, {1}'.format(col1, col2))
This code snippet is using the SQL command SELECT col1, col2 FROM test_table to select specific columns, and then is printing the first values in each, or in other words, the first row.

If you'd like to print entire columns, you can do so in a similar manner.

for (col1, col2) in conn.cursor().execute("SELECT col1, col2 FROM test_table"):
	print('{0}, {1}'.format(col1, col2))
To efficiently use your resources, you'll want to remember to explicitly close your connection to Snowflake after performing queries.

connection.close()
Look at that! You have now implemented all the steps needed to manipulate data within Snowflake.




