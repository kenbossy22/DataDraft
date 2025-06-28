import json
import os
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine, text
import openai
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AZURE_SQL_CONN = os.getenv("AZURE_SQL_CONNECTION_STRING")

openai.api_key = OPENAI_API_KEY


def connect_to_sql():
    """Create a SQLAlchemy engine for the Azure SQL database."""
    if not AZURE_SQL_CONN:
        st.error("AZURE_SQL_CONNECTION_STRING not set")
        return None
    try:
        engine = create_engine(AZURE_SQL_CONN)
        return engine
    except Exception as e:
        st.error(f"Failed to connect to SQL: {e}")
        return None


def generate_sql(user_prompt: str) -> str:
    """Use OpenAI to generate a SQL query from a natural language prompt."""
    if not OPENAI_API_KEY:
        st.error("OPENAI_API_KEY not set")
        return ""
    system_prompt = (
        "You are a helpful assistant that writes parameterized SQL for the DataDraftDB. "
        "Only return the SQL query without additional commentary."
    )
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": system_prompt},
                     {"role": "user", "content": user_prompt}],
        )
        sql_query = response.choices[0].message.content.strip()
        return sql_query
    except Exception as e:
        st.error(f"OpenAI error: {e}")
        return ""


def run_query(sql_query: str) -> pd.DataFrame:
    engine = connect_to_sql()
    if not engine or not sql_query:
        return pd.DataFrame()
    try:
        with engine.connect() as conn:
            result = conn.execute(text(sql_query))
            df = pd.DataFrame(result.fetchall(), columns=result.keys())
        return df
    except Exception as e:
        st.error(f"SQL execution error: {e}")
        return pd.DataFrame()

st.set_page_config(page_title="DataDraft Development", page_icon="🏒", layout="wide")

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    with open(path, 'r') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    return df

# Load dataset
DATA_PATH = "scatter_data.json"
df = load_data(DATA_PATH)

st.title("DataDraft Development App")

st.sidebar.header("Filters")
player_name = st.sidebar.text_input("Search player")

filtered_df = df
if player_name:
    filtered_df = df[df['Player Name'].str.contains(player_name, case=False, na=False)]

st.write(f"Showing {len(filtered_df)} of {len(df)} players")
st.dataframe(filtered_df)

st.markdown("---")
st.header("Natural Language Query")
user_prompt = st.text_input("Ask a question about the database")
if st.button("Run Query") and user_prompt:
    sql = generate_sql(user_prompt)
    if sql:
        st.code(sql, language="sql")
        result_df = run_query(sql)
        if not result_df.empty:
            st.dataframe(result_df)
        else:
            st.write("No results returned.")

