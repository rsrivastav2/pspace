import psycopg2
from openai import AzureOpenAI

# ---------- Azure OpenAI Client ----------
client = AzureOpenAI(
    api_key="YOUR_AZURE_OPENAI_KEY",
    api_version="2024-06-01",
    azure_endpoint="https://YOUR-RESOURCE-NAME.openai.azure.com/"
)

# ---------- Convert user input to SQL ----------
def natural_language_to_sql(user_input: str, table_schema: str) -> str:
    prompt = f"""
    You are an assistant that converts natural language to SQL queries.
    The database schema is: {table_schema}.
    Convert this request into a valid PostgreSQL SQL query:
    User request: "{user_input}"
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",   # Use your deployed model
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    
    sql_query = response.choices[0].message.content.strip()
    return sql_query

# ---------- Run SQL on PostgreSQL ----------
def run_query(sql_query: str):
    try:
        conn = psycopg2.connect(
            dbname="your_db",
            user="your_user",
            password="your_password",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        cur.execute(sql_query)
        
        # Fetch results
        rows = cur.fetchall()
        colnames = [desc[0] for desc in cur.description]
        
        cur.close()
        conn.close()
        
        return colnames, rows
    except Exception as e:
        return [], [("Error", str(e))]

# ---------- Main ----------
if __name__ == "__main__":
    # Example schema (important for GPT to generate correct SQL)
    schema = """
    Table: employees
    Columns: id (int), name (text), department (text), salary (int)
    """
    
    user_input = input("Enter your request: ")  # e.g., "Show me all employees in IT"
    
    sql = natural_language_to_sql(user_input, schema)
    print("Generated SQL:", sql)
    
    cols, results = run_query(sql)
    
    print("Results:")
    print(cols)
    for row in results:
        print(row)
