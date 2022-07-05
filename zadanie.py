import sqlite3
import random
from sqlite3 import Error

#CREATE
#Tworzę plik simple db a następnie tworzę tabelę scores

def create_connection(db_file):
    """ create a database connection to the SQLite database
    specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    
    return conn
    

def create_music_table(conn):
    db = sqlite3.connect("simple.db")
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS scores (
        id integer,
        name string,
        surname string,
        score integer)
    ''')
    db.commit()
    db.close()
    



#Dodawanie danych
#Wpisuje dane do utworzonej wcześniej tabeli scores
def add_scores(conn):
    """
    Add scores into the scores project
    :param conn:
    :return: 
    """

    db = sqlite3.connect("simple.db")
    cursor = db.cursor()
    print("Database opened")

    names = ['Mikel','Gregory','James','Max','Robert','Jack','Dawid','Enrique','Martin','Elizabeth']
    surnames = ['Smith','Johnson','Williams','Brown','Jones','Garcia','Davis','Martines']
    id = 0

    for _ in range(20):
        name = random.choice(names)
        surname = random.choice(surnames)
        result = random.randint(0,100)
            
            

        cursor.execute(f'''
            INSERT INTO scores (id, name, surname, score) values ({id}, "{name}", "{surname}", {result})
        ''')
            
            
        id += 1
    print('Done')

    db.commit()
    db.close()
    

#Dodanie elementów do tablicy music
def add_music(conn):
    """
    Add music into the music project
    :param conn:
    :return: 
    """
 
    db = sqlite3.connect("simple.db")
    cursor = db.cursor()
    print("Database opened")

    names = ['Mikel','Gregory','James','Max','Robert','Jack','Dawid','Enrique','Martin','Elizabeth']
    id = 0

    titles = ['For Those About To Rock','Balls to the wall','Restless and Wild','Let There Be Rock','Big Ones','Chop sue','Facelift','Audioslave','Base children','Out of Exile']
    for _ in range(20):
        name = random.choice(names)
        title = random.choice(titles)
        views = random.randint(0,100000)
            
            
        cursor.execute(f'''
            INSERT INTO music (id, title, artist, views) values ({id}, "{title}", "{name}", {views})
        ''')
            
        id += 1
    print('Done')

    db.commit()
    db.close()
    



#Pobieranie danych
#----------Faza wyświetlania zawartości bazy danych-----------
def get_all_data_from_scores(conn):
    print('Faza wyświetlania bazy danych scores: ')
    db = sqlite3.connect("simple.db")
    cursor = db.cursor()

    cursor.execute('''
        select *
        from scores
    ''')

    rows = cursor.fetchall()
    for r in rows:
        print(r[1], r[2], r[3])

    db.commit()
    db.close()


#Wszystkie elementy z tabeli music
def get_all_data_from_music(conn):
    print('Faza wyświetlania bazy danych music: ')
    db = sqlite3.connect("simple.db")
    cursor = db.cursor()

    cursor.execute('''
        select *
        from music
    ''')

    rows = cursor.fetchall()
    for r in rows:
        print(r[1], r[2], r[3])

    db.commit()
    db.close()


#Wyświetlenie wybranego elementu z bazy
def get_selected_data(conn, table, **query):
    """
    Query tasks from table with data from **query dict
    :param conn: the Connection object
    :param table: table name
    :param query: dict of attributes and values
    :return:
    """
    print('Selected data is: ')
    cur = conn.cursor()
    qs = []
    values = ()
    for k, v in query.items():
       qs.append(f"{k}=?")
       values += (v,)
    q = " AND ".join(qs)
    cur.execute(f'SELECT * FROM {table} WHERE {q}', values)
    rows = cur.fetchone()
    return print(rows)




if __name__ == "__main__":
    
    
    conn = create_connection(r"simple.db")
    if conn is not None:
   
        add_music(conn)
        get_all_data_from_music(conn)
        print('\n')
        get_all_data_from_scores(conn)
        print('\n')
        get_selected_data(conn, "music", id=14)
        
        conn.close()
    else:
        print('An error has occured')
        exit(1)