import sqlite3

def insert_results(address,res_url,birth_year,floor,seria,
                   house_type,house_crash,cadastr_number,
                   floor_type,walls_material):
    sql = ''' 
        INSERT INTO mytable(
        address,
        res_url,
        birth_year,
        floor,seria,
        house_type, 
        house_crash,
        cadastr_number,
        floor_type,walls_material) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
        '''
    conn=None
    try:
        conn=sqlite3.connect("mydatabase.db")
        cursor=conn.cursor()
        cursor.execute(sql,(address,
        res_url,
        birth_year,
        floor,seria,
        house_type,
        house_crash,
        cadastr_number,
        floor_type,walls_material))
        conn.commit()
        cursor.close()
    except (Exception,sqlite3.DatabaseError) as error:
        print(error)
conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""CREATE TABLE IF NOT EXISTS mytable(
                        id              SERIAL PRIMARY KEY, 
                        address          varchar(40),
                        res_url          varchar(40),
                        birth_year       integer,
                        floor            integer,
                        seria            varchar(40),
                        house_type       varchar(40),
                        house_crash      varchar(40),
                        cadastr_number   varchar(6),
                        floor_type       varchar(40),
                        walls_material   varchar(40))
               """)
# SELECT
#   (SELECT count(*)
#    FROM mytable
#    WHERE address IS NOT NULL) as is_not_null,
#   (SELECT count(*)
#    FROM mytable
#    WHERE address is NULL) as is_null;
