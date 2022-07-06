import pypyodbc

SQL_SERVER = 'denys-ws\main'
SQL_DB = 'Northwind'
SQL_USER = '<user name>'
SQL_PASSWORD = '<password>'

try:
    connection = pypyodbc.connect('Driver={SQL Server};'
                                  f'Server={SQL_SERVER};'
                                  f'Database={SQL_DB};'
                                  #f'UID={SQL_USER};'
                                  #f'PWD={SQL_PASSWORD};'
                                    )
except Exception:
    print('Some error with SQL Server')
else:
    cursor = connection.cursor()
    SQL_QUERY = ('''
        SELECT CompanyName, City, Country FROM dbo.Customers
        WHERE Country = 'Germany' 
    ''')

    cursor.execute(SQL_QUERY)

    results = cursor.fetchall()

    # Выведем запрос простым образом (НЕ красиво)
    print('- Выведем запрос простым образом (НЕ красиво)')
    print(results)

    # А теперь выведем красиво
    print('- А теперь выведем красиво')
    for i in results:
        print(f'Company: \"{i[0]}\", Country: \"{i[2]}\", City: \"{i[1]}\"')

    connection.close()
