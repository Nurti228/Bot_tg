import sqlite3
from pathlib import Path
from pprint import pprint


def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent / "db.sqlite3")
    cursor = db.cursor()


def create_tables():
    cursor.execute(
        """
        DROP TABLE IF EXISTS category
        """
    )
    cursor.execute(
        """
        DROP TABLE IF EXISTS products
        """
    )
    # cursor.execute(
    #     '''
    #      DROP TABLE IF EXISTS orders
    #     '''
    # )
    cursor.execute(
        """
        DROP TABLE IF EXISTS user
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price DECIMAL,
            image TEXT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES category (id)
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            user_name TEXT
        )
        """
    )
    # cursor.execute(
    #     '''
    #     CREATE TABLE IF NOT EXISTS Orders(
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     user_id INTEGER,
    #     product_id INTEGER
    #     )
    #     '''
    # )
    db.commit()


def populate_tables():
    cursor.execute(
        '''
        INSERT INTO category (name) VALUES
        ('Cars'), ('Services')
        '''
    )
    cursor.execute(
        '''
        INSERT INTO products (name, price, image, category_id) VALUES
        ('Lixiang l9', 70000, 'https://e-n-cars.ru/wp-content/uploads/2023/06/l9-scaled.webp', 1),
        ('EXEED RX', 35000, 'https://rg.ru/uploads/images/2023/07/11/22-2_627.jpg', 1),
        ('Voyah Free',45000,'https://www.gscarbuy.com/images/virtuemart/product/2022-voyah-free-ev-dna-edition.jpg', 1),
        ('Translation', 1000, '0', 2)
        '''
    )
    db.commit()


def get_products():
    cursor.execute(
        '''
        SELECT * FROM products
        '''
    )
    return cursor.fetchall()


def get_product_by_category_name(cat_name: str):
    cursor.execute(
        """
        SELECT * FROM products WHERE category_id = 
        (
            SELECT id FROM category WHERE name = :cat_name
        )
        """, {"cat_name": cat_name}
    )
    return cursor.fetchall()


def subscribe_user(user_id: str, user_name: str):
    cursor.execute(
        '''
        INSERT INTO user (user_id, user_name) VALUES (?, ?)
        ''', (user_id, user_name)
    )
    db.commit()


# def create_order(user_id: int, product_id: int):
#     cursor.execute(
#         '''
#         INSERT INTO Orders (user_id, product_id) VALUES (?, ?)
#         ''', (user_id, product_id)
#     )
#     db.commit()

def get_user_id():
    cursor.execute(
        '''
        SELECT * FROM user
        '''
    )
    return cursor.fetchall()


if __name__ == '__main__':
    init_db()
    create_tables()
    populate_tables()
    pprint(get_products())
