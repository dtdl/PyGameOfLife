'''
Created on May 1, 2020

@author: GoldenSource
'''

import sqlite3

if __name__ == '__main__':
    pass

    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
    c = conn.cursor()
#     c.execute('''CREATE TABLE OID  (OID CHAR(10) PRIMARY KEY     NOT NULL);''')
#     print("Table created successfully")

    c.execute("INSERT INTO OID (OID) VALUES ('AAABBBCCDD' )")

    cursor = c.execute("SELECT oid from OID")
    for row in cursor:
        print("OID = ", row[0], "\n")

    conn.commit()
    conn.close()