import psycopg2

#Creating table
def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='12345' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS FORM_STORE1(NAME TEXT,CITY TEXT,STATE TEXT,PINCODE TEXT,LOCALITY TEXT,MOBILE_NO TEXT, ADHAAR_NUMBER TEXT,UCODE TEXT)")
    conn.commit()
    conn.close()

#inserting values
def insert_value(name, city,  state, pd, loca, mob, aadhnum, ucode):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='S510UN' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO FORM_STORE1 VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (name, city,  state, pd, loca, mob, aadhnum, ucode))
    conn.commit()
    conn.close()

#view contents
def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='S510UN' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM AADHAAR_STORE1")
    rows = cur.fetchall()
    conn.close()
    return rows

#delete contents
def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='S510UN' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM FORM_STORE1 WHERE UCODE='%s'" % (item,))
    conn.commit()
    conn.close()

#update contents
def update(name, mob, an):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='S510UN' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE FORM_STORE1 SET NAME='%s', MOBILE_NO=%s WHERE ADHAAR_NUMBER='%s'" % (name, mob, an))
    conn.commit()
    conn.close()

def validate(dotcode):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='S510UN' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT ADHAAR_NUMBER FROM FORM_STORE1 WHERE UCODE = '%s'" % (dotcode))
    rows = cur.fetchall()
    conn.close()
    return rows



#print(view())
#create_table()
#insert_value("RAHUL", 7379, 9914)

