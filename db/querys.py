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
        
    def listInventory(self):
        query = """
                    SELECT film.title as pelicula, inventory.store_id, inventory.last_update FROM inventory
                    INNER JOIN film ON inventory.film_id = film.film_id
                    ORDER BY film.title;
                """
        list_inventory = self.db.execute_query(query)
        self.db.close_connection()
        return list_inventory
    
    def listFilm(self):
        query = """
                    SELECT film.title as pelicula FROM inventory
                    INNER JOIN film ON inventory.film_id = film.film_id
                    GROUP BY film.title
                    ORDER BY film.title DESC;
                """
        list_film = self.db.execute_query(query)
        self.db.close_connection()
        return list_film
    
    def listStore1(self):
        query = """
                    select film.title as pelicula, count(inventory.store_id), inventory.last_update from inventory 
                    inner join film on inventory.film_id = film.film_id where inventory.store_id=1
                    group by film.title
                    order by film.title;
                """
        list_store = self.db.execute_query(query)
        self.db.close_connection
        return list_store
    
    def listStore2(self):
        query = """
                    select film.title as pelicula, count(inventory.store_id), inventory.last_update from inventory 
                    inner join film on inventory.film_id = film.film_id where inventory.store_id=2
                    group by film.title
                    order by film.title;
                """
        list_store = self.db.execute_query(query)
        self.db.close_connection
        return list_store
    def summary(self):
        query = """
                    select  film.film_id, film.title as pelicula, SUM(CASE WHEN inventory.store_id = '1' THEN 1 ELSE 0 END) AS count_1,
                    SUM(CASE WHEN inventory.store_id = '2' THEN 1 ELSE 0 END) AS count_2 from inventory
                    inner join film on inventory.film_id = film.film_id
                    GROUP BY inventory.film_id, film.title;
                """
        summary = self.db.execute_query(query)
        self.db.close_connection
        return summary