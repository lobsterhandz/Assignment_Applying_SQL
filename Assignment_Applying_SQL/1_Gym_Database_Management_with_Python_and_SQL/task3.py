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

def fetch_query(connection, query, data=None):
    cursor = connection.cursor()
    result = None
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
        return result

def update_member_age(connection, member_id, new_age):
    check_query = "SELECT * FROM Members WHERE id = %s"
    update_query = "UPDATE Members SET age = %s WHERE id = %s"
    try:
        if fetch_query(connection, check_query, (member_id,)):
            execute_query(connection, update_query, (new_age, member_id))
            print(f"Member ID {member_id}'s age updated to {new_age}.")
        else:
            print(f"Member ID {member_id} does not exist.")
    except Error as e:
        print(f"Failed to update member age: {e}")

if __name__ == "__main__":
    connection = create_connection("localhost", "root", "password", "fitness_center")
    update_member_age(connection, 5, 36)
