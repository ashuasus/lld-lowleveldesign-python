class DBConnection:
    def __init__(self):
        self.mysql_connection = None
        try:
            # In Python we simulate the connection rather than using JDBC
            self.mysql_connection = "jdbc:mysql://localhost:3306/DB"
        except Exception as e:
            print(e)
