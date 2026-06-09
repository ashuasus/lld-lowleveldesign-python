import threading
from creationalpatterns.objectpool.resource.db_connection import DBConnection


class DBConnectionPoolManager:
    _instance = None
    _lock = threading.Lock()
    INITIAL_POOL_SIZE = 3
    MAX_POOL_SIZE = 6

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.free_connections = [DBConnection() for _ in range(cls.INITIAL_POOL_SIZE)]
                    cls._instance.in_use_connections = []
                    cls._instance._op_lock = threading.Lock()
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

    def get_db_connection(self):
        with self._op_lock:
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
        with self._op_lock:
            if conn is not None:
                self.in_use_connections.remove(conn)
                self.free_connections.append(conn)
                print("DBConnection released from inUseConnections list and added to freeConnections list.")
                print(f"freeConnections size: {len(self.free_connections)}")
                print(f"inUseConnections size: {len(self.in_use_connections)}")
            else:
                print("DBConnection is null. Cannot release.")
