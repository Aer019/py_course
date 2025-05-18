import sqlite3


conn = sqlite3.connect("db_api_bd_example.db")
print(type(conn))

cursor = conn.cursor()
print(type(cursor))

##<class 'sqlite3.Connection'>
##<class 'sqlite3.Cursor'>

cursor.execute("""CREATE TABLE IF NOT EXISTS user (
u_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
u_name TEXT NOT NULL,
u_surname TEXT NOT NULL
);
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS task (
t_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
t_name TEXT NOT NULL,
t_priority INTEGER NOT NULL,
u_id_fk INTEGER NOT NULL,
FOREIGN KEY(u_id_fk) REFERENCES user(u_id)
);
""")
conn.commit()

user_data1 = ('Kotik', 'asdasda')

##cursor.execute("""
##INSERT INTO user (u_name, u_surname) VALUES (?,?);""", user_data1)
##cursor.execute("""
##INSERT INTO user (u_name, u_surname) VALUES (?,?);""", ('Bob', 'fgfgfgf'))

conn.commit()

##cursor.execute("""
##INSERT INTO task (t_name, t_priority, u_id_fk) VALUES (?,?,?);""", ("EAT",100,1))
##cursor.execute("""
##INSERT INTO task (t_name, t_priority, u_id_fk) VALUES (?,?,?);""", ("RUN",10,1))
##cursor.execute("""
##INSERT INTO task (t_name, t_priority, u_id_fk) VALUES (?,?,?);""", ("SLEEP",5,2))
##cursor.execute("""
##INSERT INTO task (t_name, t_priority, u_id_fk) VALUES (?,?,?);""", ("READ",150,2))
##cursor.execute("""
##INSERT INTO task (t_name, t_priority, u_id_fk) VALUES (?,?,?);""", ("WALK",10,2))
conn.commit()

##for record in cursor.execute("""SELECT * FROM user;"""):
##    print(record)

##(1, 'Kotik', 'asdasda')
##(2, 'Bob', 'fgfgfgf')
##(3, 'Kotik', 'asdasda')
##(4, 'Bob', 'fgfgfgf')
##(5, 'Kotik', 'asdasda')
##(6, 'Bob', 'fgfgfgf')
##(7, 'Kotik', 'asdasda')
##(8, 'Bob', 'fgfgfgf')

##cursor.execute("""SELECT * FROM task;""")
##
##results = cursor.fetchall()
##print(results)
##print()
##
##for i in results:
##    print(i)

##[(1, 'EAT', 100, 1), (2, 'RUN', 10, 1), (3, 'SLEEP', 5, 2), (4, 'READ', 150, 2), (5, 'WALK', 10, 2), (6, 'EAT', 100, 1), (7, 'RUN', 10, 1), (8, 'SLEEP', 5, 2), (9, 'READ', 150, 2), (10, 'WALK', 10, 2), (11, 'EAT', 100, 1), (12, 'RUN', 10, 1), (13, 'SLEEP', 5, 2), (14, 'READ', 150, 2), (15, 'WALK', 10, 2)]
##
##(1, 'EAT', 100, 1)
##(2, 'RUN', 10, 1)
##(3, 'SLEEP', 5, 2)
##(4, 'READ', 150, 2)
##(5, 'WALK', 10, 2)
##(6, 'EAT', 100, 1)
##(7, 'RUN', 10, 1)
##(8, 'SLEEP', 5, 2)
##(9, 'READ', 150, 2)
##(10, 'WALK', 10, 2)
##(11, 'EAT', 100, 1)
##(12, 'RUN', 10, 1)
##(13, 'SLEEP', 5, 2)
##(14, 'READ', 150, 2)
##(15, 'WALK', 10, 2)

#UPDATE user SET u_name="Denis",u_surname="Gregoriev" WHERE u_id=1;
##cursor.execute("""DELETE FROM task WHERE t_id=?;""", (9,))
##cursor.execute("""DELETE FROM task WHERE t_id=?;""", (8,))
##conn.commit()
##conn.commit()
### READ
##cursor.execute("""SELECT * FROM task;""")
##
##results = cursor.fetchall()
##print(results)


#UPDATE
tp = ("sdadsa", "asdasdas", 1)
cursor.execute("""UPDATE user SET u_name=?,u_surname=? where u_id=?;""", tp)

conn.commit()


cursor.execute("""SELECT * FROM user;""")
result = cursor.fetchall()

for i in result:
    print(i)
    
##(1, 'sdadsa', 'asdasdas')
##(2, 'Bob', 'fgfgfgf')
##(3, 'Kotik', 'asdasda')
##(4, 'Bob', 'fgfgfgf')
##(5, 'Kotik', 'asdasda')
##(6, 'Bob', 'fgfgfgf')
##(7, 'Kotik', 'asdasda')
##(8, 'Bob', 'fgfgfgf')
