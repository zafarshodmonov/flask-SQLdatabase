import sqlite3

class Smartphone:
    def __init__(self, db_name):
        self.db_name = db_name

    def get_connection(self):
        return sqlite3.connect(self.db_name, check_same_thread=False)

    def sql_get_all_smartphones(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM smartphone")
            table = cursor.fetchall()
        ress = {}
        for id, name, color, RAM, memory, price in table:
            ress[id] = {'name': name, 'color': color, 'RAM': RAM, 'memory': memory, 'price': price}
        return ress

    
    def sql_get_product_by_id(self, id):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM smartphone WHERE id = ?", (id,))
            table = cursor.fetchall()
        ress = {}
        for id, name, color, RAM, memory, price in table:
            ress[id] = {'name': name, 'color': color, 'RAM': RAM, 'memory': memory, 'price': price}
        return ress
    
    def sql_get_smartphone_by_name(self, name):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM smartphone WHERE name = ?", (name,))
            table = cursor.fetchall()
        ress = {}
        for id, name, color, RAM, memory, price in table:
            ress[id] = {'name': name, 'color': color, 'RAM': RAM, 'memory': memory, 'price': price}
        return ress
    
    def sql_get_smartphone_all_names(self):

        return
    
    def sql_get_smartphone_by_color(self, color):

        return
    
    def sql_get_smartphone_by_ram(self, ram):

        return
    
    def sql_get_smartphone_by_memory(self, memory):

        return
    
    def sql_get_smartphone_by_price(self, price):

        return
    
    def sql_add_smartphone(self, phone):

        return
    
    def sql_delete_smartphone(self, id):

        return 

def main():
    sp = Smartphone('smartphone_store.db')
    data = sp.sql_get_all_smartphones()
    print(data)

if __name__ == "__main__":
    main()
