import sqlite3

conn = sqlite3.connect("shop.db")
cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER,
    is_published BOOLEAN DEFAULT (false),
    name TEXT NOT NULL,
    FOREIGN KEY (parent_id) REFERENCES categories (id)
 );
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id NOT NULL,
    price REAL DEFAULT (0),
    total INTEGER DEFAULT (0),
    is_published BOOLEAN DEFAULT (false),
    name TEXT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories (id)    
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS languages(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    language_code TEXT NOT NULL
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS bot_users(
    id TEXT PRIMARY KEY,
    language_id INTEGER NOT NULL,
    is_blocked BOOLEAN DEFAULT (false),
    balance REAL DEFAULT (0),
    FOREIGN KEY (language_id) REFERENCES languages (id)
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS statuses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL 
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS invoices(
    id TEXT PRIMARY KEY,
    bot_user_id TEXT NOT NULL,
    status_id INTEGER NOT NULL,
    date_create INTEGER,
    total INTEGER DEFAULT (0),
    FOREIGN KEY (bot_user_id) REFERENCES bot_users (id),
    FOREIGN KEY (status_id) REFERENCES statuses (id)
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bot_user_id TEXT NOT NULL,
    status_id INTEGER NOT NULL,
    invoice_id TEXT NOT NULL,
    date_create INTEGER,
    FOREIGN KEY (bot_user_id) REFERENCES bot_users (id),
    FOREIGN KEY (status_id) REFERENCES statuses (id),
    FOREIGN KEY (invoice_id) REFERENCES invoices (id)
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS order_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    total INTEGER DEFAULT (0) 
);
""")

conn.commit()
