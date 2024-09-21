import pytest
from config.setup_module import setup_connection, close_connection

@pytest.fixture(scope="session", autouse=True)
def db_connection():
    con, cs = setup_connection()
    yield con, cs
    close_connection(con, cs)


def test_create_warehouse(db_connection):
    con, cs = db_connection

    cs.execute("CREATE WAREHOUSE IF NOT EXISTS test_warehouse")
    con.commit()
    
    # Verificar se o warehouse foi criado
    cs.execute("SHOW WAREHOUSES LIKE 'test_warehouse'")
    result = cs.fetchone()
    assert result is not None, "O warehouse test_warehouse não foi criado"
    
    # Validar os detalhes do warehouse
    cs.execute("DESCRIBE WAREHOUSE test_warehouse")
    warehouse_details = cs.fetchone() 
    
    assert warehouse_details is not None, "Falha ao recuperar os detalhes do warehouse"
    
    # Validar o nome do warehouse
    assert warehouse_details[1] == 'TEST_WAREHOUSE', f"Nome do warehouse incorreto. Esperado: TEST_WAREHOUSE, Obtido: {warehouse_details[0]}"
    
    # Validar o tipo do warehouse
    assert warehouse_details[2] == 'WAREHOUSE', f"Tipo do warehouse incorreto. Esperado: WAREHOUSE, Obtido: {warehouse_details[1]}"
  
    cs.execute("DROP WAREHOUSE IF EXISTS test_warehouse")
    con.commit()



def test_delete_warehouse(db_connection):
    con, cs = db_connection

    # Create the warehouse for the test
    cs.execute("CREATE WAREHOUSE IF NOT EXISTS test_warehouse")
    con.commit()

    # Verify the warehouse was created
    cs.execute("SHOW WAREHOUSES LIKE 'test_warehouse'")
    result = cs.fetchone()
    assert result is not None, "Warehouse was not created for deletion test"

    # Delete the warehouse
    cs.execute("DROP WAREHOUSE IF EXISTS test_warehouse")
    con.commit()
    
    # Verify the warehouse was deleted
    cs.execute("SHOW WAREHOUSES LIKE 'test_warehouse'")
    result = cs.fetchone()
    assert result is None, "Warehouse was not deleted successfully"