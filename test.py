from flask import Flask, request, jsonify
import psycopg2
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        port="5432",
        database="your_database",
        user="your_user",
        password="your_password"
    )

def generate_sql_from_prompt(user_prompt):
    schema_info = """
    Table: products(id INT, description TEXT, price NUMERIC, category TEXT)
    Table: customers(id INT, name TEXT, email TEXT)
    Table: orders(id INT, customer_id INT, product_id INT, order_date DATE)
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",  # You can use gpt-3.5-turbo for cheaper cost
        messages=[
            {"role": "system", "content": f"You are a PostgreSQL expert. Use this schema: {schema_info}"},
            {"role": "user", "content": f"Convert this request into SQL: {user_prompt}"}
        ],
        temperature=0
    )

    sql_query = response["choices"][0]["message"]["content"].strip()
    return sql_query

@app.route("/nl-search", methods=["POST"])
def nl_search():
    data = request.json
    user_prompt = data.get("query")

    if not user_prompt:
        return jsonify({"error": "Missing 'query'"}), 400

    sql_query = generate_sql_from_prompt(user_prompt)

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(sql_query)
        results = cursor.fetchall()
    except Exception as e:
        return jsonify({"error": str(e), "generated_sql": sql_query}), 400
    finally:
        cursor.close()
        conn.close()

    return jsonify({"query": user_prompt, "sql": sql_query, "results": results})

if __name__ == "__main__":
    app.run(debug=True)
