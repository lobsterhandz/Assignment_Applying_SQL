import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query, data=None):
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def add_member(connection, member_id, name, age):
    query = """
    INSERT INTO Members (id, name, age)
    VALUES (%s, %s, %s)
    """
    try:
        execute_query(connection, query, (member_id, name, age))
        print(f"Member {name} added successfully.")
    except Error as e:
        print(f"Failed to add member: {e}")

if __name__ == "__main__":
    connection = create_connection("localhost", "root", "password", "fitness_center")
    add_member(connection, 5, 'Michael Jordan', 35)
