from creationalpatterns.objectpool.resource.db_connection import DBConnection


class DBConnectionPoolManager:
    INITIAL_POOL_SIZE = 3
    MAX_POOL_SIZE = 6

    def __init__(self):
        self.free_connections = [DBConnection() for _ in range(self.INITIAL_POOL_SIZE)]
        self.in_use_connections = []

    def get_db_connection(self):
        if not self.free_connections and len(self.in_use_connections) < self.MAX_POOL_SIZE:
            self.free_connections.append(DBConnection())
            print("New DBConnection created and added to freeConnections list.")
            print(f"freeConnections size: {len(self.free_connections)}")
            print(f"inUseConnections size: {len(self.in_use_connections)}")
        elif not self.free_connections and len(self.in_use_connections) >= self.MAX_POOL_SIZE:
            print("Pool is full. Cannot create new DBConnection.")
            return None
        conn = self.free_connections.pop()
        self.in_use_connections.append(conn)
        print("DBConnection retrieved from freeConnections list and added to inUseConnections list.")
        print(f"freeConnections size: {len(self.free_connections)}")
        print(f"inUseConnections size: {len(self.in_use_connections)}")
        return conn

    def release_db_connection(self, conn):
        if conn is not None:
            self.in_use_connections.remove(conn)
            self.free_connections.append(conn)
            print("DBConnection released from inUseConnections list and added to freeConnections list.")
            print(f"freeConnections size: {len(self.free_connections)}")
            print(f"inUseConnections size: {len(self.in_use_connections)}")
        else:
            print("DBConnection is null. Cannot release.")
