from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Helper function to execute SQL queries and fetch data from the database
def execute_query(query, args=()):
    with sqlite3.connect('data.db') as conn:
        cur = conn.cursor()
        cur.execute(query, args)
        return cur.fetchall()

# API endpoint to get data based on filters
@app.route('/api/data', methods=['GET'])
def get_data():
    year = request.args.get('year', type=int)
    topic = request.args.get('topic', type=str)
    sector = request.args.get('sector', type=str)
    region = request.args.get('region', type=str)
    # Add other filters as needed

    # Build the SQL query based on the selected filters
    query = "SELECT * FROM your_table_name WHERE Year=? AND Topic=? AND Sector=? AND Region=?"
    # Add other filters to the SQL query

    data = execute_query(query, (year, topic, sector, region))
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
