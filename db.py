import pymysql


def get_conn():
    return pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='12345678',
        database='ds_database',
        charset='utf8'
    )


def query_data(sql):
    # connect to the database
    conn = get_conn()
    try:
        # get a obj of database ---- cursor
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        # execute the sql on the obj
        cursor.execute(sql)
        # get the result
        return cursor.fetchall()
    finally:
        conn.close()


def insert_or_updata_data(sql):
    conn = get_conn()
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        # update the database
        conn.commit()
        return cursor.fetchall()
    finally:
        conn.close()


def new_database(name):
    conn = get_conn()

    sql1 = f"""create table {name}( id int auto_increment, tag varchar(10) not null, info varchar(255) null, constraint {name}_pk primary key (id));"""
    sql2 = f"""create unique index {name}_tag_uindex ON {name} (tag);"""

    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql1)
        cursor.execute(sql2)
        # update the database
        conn.commit()
        return cursor.fetchall()
    finally:
        conn.close()


if __name__ == '__main__':
    name = 'luolie'
    new_database(name)


    # insert_or_updata_data(sql)
    #
    # sql = 'select * from user'
    # datas = query_data(sql)
    # import pprint
    #
    # pprint.pprint(datas)
