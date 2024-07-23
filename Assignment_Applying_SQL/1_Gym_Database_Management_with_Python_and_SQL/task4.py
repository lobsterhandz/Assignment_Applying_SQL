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

def delete_workout_session(connection, session_id):
    check_query = "SELECT * FROM WorkoutSessions WHERE session_id = %s"
    delete_query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
    try:
        if fetch_query(connection, check_query, (session_id,)):
            execute_query(connection, delete_query, (session_id,))
            print(f"Workout session ID {session_id} deleted successfully.")
        else:
            print(f"Workout session ID {session_id} does not exist.")
    except Error as e:
        print(f"Failed to delete workout session: {e}")

if __name__ == "__main__":
    connection = create_connection("localhost", "root", "password", "fitness_center")
    delete_workout_session(connection, 2)
