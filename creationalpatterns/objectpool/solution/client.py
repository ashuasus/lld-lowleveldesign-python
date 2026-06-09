from .db_connection_pool_manager import DBConnectionPoolManager


# Client - Object Pool Solution Demo
def main():
    print("======= Object Pool Design Pattern ======")

    # Creating a DBConnectionPoolManager
    pool_manager = DBConnectionPoolManager.get_instance()

    # Creating 6 DBConnections (MAX_POOL_SIZE is 6)
    db_connection1 = pool_manager.get_db_connection()
    db_connection2 = pool_manager.get_db_connection()
    db_connection3 = pool_manager.get_db_connection()
    db_connection4 = pool_manager.get_db_connection()
    db_connection5 = pool_manager.get_db_connection()
    db_connection6 = pool_manager.get_db_connection()

    # 7th DBConnection will not be created as the pool is full (returns null)
    null_db_connection = pool_manager.get_db_connection()
    print("DBConnection is null as POOL is full." if null_db_connection is None else "DBConnection is not null")
    pool_manager.release_db_connection(db_connection6)
    db_connection7 = pool_manager.get_db_connection()

    # ******** Solution Demo **********
    # What happens if another client tries to create a new DBConnectionPoolManager?
    pool_manager2 = DBConnectionPoolManager.get_instance()
    print("====== Same Instance? ======")
    print("Same instance of DBConnectionPoolManager" if pool_manager is pool_manager2 else "Different instances of DBConnectionPoolManager")


if __name__ == "__main__":
    main()
