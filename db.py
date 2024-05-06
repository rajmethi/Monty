import sqlite3
import json
connection = sqlite3.connect('grailed_items.db')
from item import Item
print("Opened database successfully")

table_schema = """
CREATE TABLE items (
    title TEXT,
    price REAL,
    brands TEXT,
    discount_percent REAL,
    last_bump TEXT,
    original_list_date TEXT,
    size TEXT,
    condition TEXT,
    like_count INTEGER,
    seller_stars REAL,
    seller_transaction_count INTEGER,
    seller_listing_count INTEGER,
    tags TEXT,
    description TEXT,
    shipping_cost REAL,
    color TEXT,
    href TEXT,
    likes_per_hour REAL,
    trending_position INTEGER,
    specific_subcategory TEXT
    
);
"""
# connection.execute(table_schema)
# print("Table created successfully")
def insert_item_into_sqlite(item_obj):
    try:
        connection = sqlite3.connect('grailed_items.db')
        cursor = connection.cursor()
        insert_query = """
            INSERT INTO items (title, price, brands, discount_percent, last_bump,
                            original_list_date, size, condition, like_count, seller_stars,
                            seller_transaction_count, seller_listing_count, tags, description,
                            shipping_cost, color, href, likes_per_hour, trending_position, specific_subcategory)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            # Execute the SQL query with item_obj attribute values
        brands_json = json.dumps(item_obj.brands)
        cursor.execute(insert_query, (item_obj.title,
                                      item_obj.price, 
        
                                      brands_json, 
                                        item_obj.discount_percent, 
                                        item_obj.last_bump,
                                        item_obj.original_list_date, 
                                        item_obj.size,
                                        item_obj.condition, 
                                        item_obj.like_count,
                                        item_obj.seller_stars, 
                                        item_obj.seller_transaction_count,
                                        item_obj.seller_listing_count, 
                                        item_obj.tags,
                                        item_obj.description, 
                                        item_obj.shipping_cost,
                                        item_obj.color, 
                                        item_obj.href, 
                                        item_obj.likes_per_hour,
                                        item_obj.trending_position,
                                        item_obj.specific_subcategory
                                                                    ))
            
        connection.commit()
    
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    
    finally:
        if connection:
            connection.close()
        
    

def get_all_items_from_sqlite():
    try:
        connection = sqlite3.connect('grailed_items.db')
        cursor = connection.cursor()
        select_query = """
            SELECT * FROM items
            """
        cursor.execute(select_query)
        fetched = cursor.fetchall()
        items = []
        
        for item in fetched:
            
     
            item_obj = Item(
                item[1], 
                json.loads(item[2]),
                item[0],
                item[3],
                item[4],
                item[5],
                item[6],
                item[7],
                item[15],
                item[8],
                item[9],
                item[10],
                item[11],
                item[12],
                item[13],
                item[14],
                item[16],
                item[18],
                item[19]
            )
            items.append(item_obj)
            
        
        return items
    except sqlite3.Error as error:
        print("Failed to get data from sqlite table", error)
    finally:
        if connection:
            connection.close()
            

