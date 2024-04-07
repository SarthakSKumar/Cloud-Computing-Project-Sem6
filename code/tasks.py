# Python code snippet to create MySQL table for tasks
import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="$athishG5024",
    database="task_management_CS440_CS482_CS484_CS486"
)

# Create cursor object
cursor = db.cursor()

# Define SQL query to create tasks table
create_table_query = """
CREATE TABLE tasks (
  task_id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  status VARCHAR(20) DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)
"""

# Execute SQL query to create tasks table
cursor.execute(create_table_query)

# Commit changes and close connection
db.commit()
db.close()
