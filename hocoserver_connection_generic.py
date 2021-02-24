import pyodbc 
conn_string = ("Driver={SQL Server Native Client 11.0};"
                      #"Server=.\SQLEXPRESS, 1433;"
                      "Server=192.168.2.64, 1433;"
                      "Database=hocoDB;"
                      #"Trusted_Connection=yes;")
                      "UID=sa;"
            		  "PWD=hocopass123;")

conn = pyodbc.connect(conn_string)
cursor = conn.cursor()
#push data
cursor.execute('''
                INSERT INTO inputs (Name, Value, Status)
                VALUES
                ('shower water temperature',101,'1'),
                ('python insert value',66,'0')
                ''')
conn.commit()
#pull data
cursor.execute('SELECT * FROM inputs')

for row in cursor:
    print(row)