# Connecting to the Database
def DbConnect(query):
    
    conn = psycopg2.connect(host="localhost",database="TwitterDB",port=5432,user=<user>,password=<password>)
    curr = conn.cursor()
    
    curr.execute(query)
    
    rows = curr.fetchall()
    
    return rows