import sqlite3

class Smartphone:
    def __init__(self, db_name):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()

    def sql_get_all_smartphones(self):

        return
    
    def sql_get_product_by_id(self, id):

        return
    
    def sql_get_smartphone_by_name(self, name):

        return
    
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