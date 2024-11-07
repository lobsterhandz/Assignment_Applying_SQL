import mysql.connector
from mysql.connector import Error

# Create a connection to the database
def create_connection(host_name, user_name, user_password, db_name):
    """
    Establishes a connection to the MySQL database.
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

# Function to execute a query
def execute_query(connection, query, data=None):
    """
    Executes a query in the database.
    Parameters:
    - connection: MySQL connection object.
    - query: The SQL query to be executed.
    - data: Optional data for parameterized queries.
    """
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        connection.rollback()  # rollback to maintain data consistency
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()

# Function to fetch data from the database
def fetch_query(connection, query, params=None):
    """
    Fetches data from the database.
    Parameters:
    - connection: MySQL connection object.
    - query: The SQL query to be executed.
    - params: Optional parameters for the query.
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        return cursor.fetchall()
    except Error as e:
        print(f"The error '{e}' occurred")
        return []
    finally:
        cursor.close()

# Helper function to check if a record exists
def record_exists(connection, query, params):
    """
    Checks if a record exists in the database.
    """
    try:
        return bool(fetch_query(connection, query, params))
    except Error as e:
        print(f"Error while checking record existence: {e}")
        return False

# Task 1: Add a Member
def add_member(connection, member_id, name, age):
    """
    Adds a new member to the 'Members' table in the gym's database.
    """
    query = """
    INSERT INTO Members (id, name, age)
    VALUES (%s, %s, %s)
    """
    try:
        # Execute the query to add a new member
        execute_query(connection, query, (member_id, name, age))
        print(f"Member {name} added successfully.")
    except Error as e:
        # Handle duplicate ID or other constraint violations
        print(f"Failed to add member: {e}")

# Task 2: Add a Workout Session
def add_workout_session(connection, member_id, session_date, session_time, activity):
    """
    Adds a new workout session to the 'WorkoutSessions' table for a specific member.
    """
    query = """
    INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity)
    VALUES (NULL, %s, %s, %s, %s)
    """
    try:
        # Execute the query to add a workout session for the given member
        execute_query(connection, query, (member_id, session_date, session_time, activity))
        print(f"Workout session for member ID {member_id} added successfully.")
    except Error as e:
        # Handle invalid member ID or other constraint violations
        print(f"Failed to add workout session: {e}")

# Task 3: Updating Member Information
def update_member_age(connection, member_id, new_age):
    """
    Updates the age of a member in the 'Members' table.
    """
    check_query = "SELECT * FROM Members WHERE id = %s"
    update_query = "UPDATE Members SET age = %s WHERE id = %s"
    try:
        # Check if the member exists
        if record_exists(connection, check_query, (member_id,)):
            # If member exists, execute the query to update the age
            execute_query(connection, update_query, (new_age, member_id))
            print(f"Member ID {member_id}'s age updated to {new_age}.")
        else:
            # If the member does not exist, print an error message
            print(f"Member ID {member_id} does not exist.")
    except Error as e:
        # Handle any other errors that occur during the update
        print(f"Failed to update member age: {e}")

# Task 4: Delete a Workout Session
def delete_workout_session(connection, session_id):
    """
    Deletes a workout session from the 'WorkoutSessions' table based on session ID.
    """
    check_query = "SELECT * FROM WorkoutSessions WHERE session_id = %s"
    delete_query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
    try:
        # Check if the workout session exists
        if record_exists(connection, check_query, (session_id,)):
            # If the session exists, execute the query to delete it
            execute_query(connection, delete_query, (session_id,))
            print(f"Workout session ID {session_id} deleted successfully.")
        else:
            # If the session does not exist, print an error message
            print(f"Workout session ID {session_id} does not exist.")
    except Error as e:
        # Handle any other errors that occur during deletion
        print(f"Failed to delete workout session: {e}")

# Example usage
if __name__ == "__main__":
    # Establish a connection to the database
    connection = create_connection("localhost", "root", "password", "gym")

    if connection:
        # Example calls to the functions
        add_member(connection, 1, "John Doe", 30)
        add_workout_session(connection, 1, "2024-11-06", "10:00:00", "Cardio")
        update_member_age(connection, 1, 31)
        delete_workout_session(connection, 1)

        # Close the connection after operations are complete
        connection.close()
