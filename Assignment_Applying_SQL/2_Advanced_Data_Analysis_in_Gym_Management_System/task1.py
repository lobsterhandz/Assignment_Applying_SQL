import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    """
    Create a database connection.
    """
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

def execute_query(connection, query):
    """
    Execute a single query.
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def fetch_query(connection, query):
    """
    Fetch the results of a query.
    """
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
        return result

def get_members_in_age_range(connection, start_age, end_age):
    """
    Retrieve members whose ages fall between start_age and end_age.
    """
    query = f"""
    SELECT * FROM Members
    WHERE age BETWEEN {start_age} AND {end_age};
    """
    results = fetch_query(connection, query)
    return results

# Example usage
if __name__ == "__main__":
    # Connect to the database
    connection = create_connection("localhost", "root", "password", "fitness_center")

    # Task 1: Retrieve members whose ages fall between 25 and 30
    members = get_members_in_age_range(connection, 25, 30)
    
    # Print the results
    if members:
        print("Members between the ages of 25 and 30:")
        for member in members:
            print(member)
    else:
        print("No members found in the specified age range.")
