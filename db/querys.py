from .conexion_database import ConexionMysql

class Querys:
    def __init__(self) -> None:
        self.db = ConexionMysql()
        self.db.connection()
    
    def insertLanguage(self, language, date):
        query = """
                    INSERT INTO language(name, last_update) VALUES(%s, %s)
                """
        values = (language, date)
        self.db.execute_query(query, values)
        self.db.close_connection()
        
    def listLanguages(self):
        query = """
                    SELECT * FROM language
                """
        language = self.db.execute_query(query)
        self.db.close_connection()
        return language
    
    def updateLanguges(self, language, id):
        query = """
                    UPDATE language SET name=%s WHERE language_id=%s
                """
        values = (language, id)
        self.db.execute_query(query, values)
        self.db.close_connection()