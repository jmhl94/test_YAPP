import mysql.connector

# Creacion db
def create_db(db, db_name):
    cursor = db.cursor()
    cursor.execute(f"CREATE DATABASE {db_name}")

def connect_to_mysql():
    db = mysql.connector.connect(
      host="localhost",
      user="",
      passwd=""
    )
    return db

def check_database(db, db_name):
    cursor = db.cursor()
    cursor.execute(f"SHOW DATABASES LIKE '{db_name}'")
    if cursor.fetchall():
        return True
    else:
        return False

def check_table(db, table_name):
    cursor = db.cursor()
    cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
    if cursor.fetchall():
        return True
    else:
        return False

def create_table(db, table_name):
    cursor = db.cursor()
    cursor.execute(f'''
        CREATE TABLE {table_name}
        (ID INT AUTO_INCREMENT PRIMARY KEY,
        Title VARCHAR(255) CHARACTER SET utf16, Year INT, Age VARCHAR(255),
        IMDb FLOAT, Rotten_Tomatoes VARCHAR(10), Netflix BOOL,
        Hulu BOOL, Prime_Video BOOL, Disney_pluss BOOL,Type INT,
        Directors VARCHAR(255) CHARACTER SET utf16, Genres VARCHAR(255),
        Country VARCHAR(255), Language VARCHAR(255), Runtime INT);
        ''')

def insert_items(db, data, table_name):
    cursor = db.cursor()
    sql = f'''INSERT INTO {table_name} (Title, Year, Age, IMDb,
    Rotten_Tomatoes, Netflix, Hulu, Prime_Video, Disney_pluss,
    Type, Directors, Genres, Country, Language, Runtime)
    VALUES {data}'''.replace(' nan,', ' NULL,').replace(' nan)', ' NULL)')
    cursor.execute(sql)
    db.commit()
