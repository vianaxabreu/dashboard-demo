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
        project=st.secrets["project_id_"],
    )

    # ----------------------------------------------------
    # Query BigQuery
    # ----------------------------------------------------
    PROJECT_ID = st.secrets["project_id_"]
    DATASET = "dbt_day02_prod_finance"
    TABLE = "mart_finance_campaigns_month"
    
    query = f"""
        SELECT 
        FORMAT_DATE('%b %Y', datemonth) as month,
        average_basket,
        revenue
        FROM `{PROJECT_ID}.{DATASET}.{TABLE}`
        order by datemonth asc
    """

    df = client.query(query, location="EU").to_dataframe()
    return df
