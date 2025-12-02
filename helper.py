import streamlit as st
import pandas as pd
import plotly.express as px

from google.oauth2 import service_account
from google.cloud import bigquery

def get_data():
    # ----------------------------------------------------
    # Load credentials from Streamlit secrets (very safe)
    # ----------------------------------------------------
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"]
    )

    client = bigquery.Client(
        credentials=credentials,
        project=st.secrets["gcp_service_account"]["project_id"],
    )

    # ----------------------------------------------------
    # Query BigQuery
    # ----------------------------------------------------
    PROJECT_ID = st.secrets["gcp_service_account"]["project_id"]
    DATASET = "jaffle_shop"
    TABLE = "orders"

    query = f"""
    SELECT 
    extract(MONTH FROM ORDER_DATE) as month,
    count(distinct ID) as total_orders,
    count(distinct USER_ID) as nb_users
    FROM `{PROJECT_ID}.{DATASET}.{TABLE}`
    GROUP BY month
    """

    df = client.query(query).to_dataframe()
    return df
