import streamlit as st
import pandas as pd
import plotly.express as px

from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
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

def get_user_query(email):


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

    client = bigquery.Client(credentials=credentials, project=st.secrets["project_id_"])

    # use the email to filter the query later
    query = f"""
        SELECT

        SESSION_USER() AS run_by
    """
    job_query = client.query(query, location="EU")
    job_query.result()

    user_email = job_query.user_email
    return user_email
