import psycopg2
host_name = "localhost"
data_base = "school"
user_name = "postgres"
password = "123456"
port_id = 5432
conn = psycopg2.connect(host = host_name, dbname = data_base, user = user_name, password = password, port = port_id)
cur = conn.cursor()

table_query = '''
create table if not exists teachers(
id int primary key, 
name varchar(40) not null,
salary int,
grade int)
'''
cur.execute(table_query)

insert_query = '''
insert into teachers (
id, name, salary, grade) values(
%s, %s, %s, %s)
'''
#insert_value = [(2, "Josh", 567, 6), (3, "Jack", 8900, 1), (4, "Jaxon", 7876, 10)]
#for v in insert_value:
#    cur.execute(insert_query, v)

cur.execute("select * from teachers")
for record in cur.fetchall():
    print(record[1], record [2])

update_query = "update teachers set salary = salary + salary"
cur.execute(update_query)

cur.execute("select * from teachers")
for record in cur.fetchall():
    print(record[1], record [2])

delete_query = "delete from teachers where name = 'Jhon'"
cur.execute(delete_query)

conn.commit()
cur.close()
conn.close()