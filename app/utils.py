
import streamlit as st
from environs import Env
from sqlalchemy import create_engine

env = Env()


class DBConnector:
    @st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})
    def init_connection():
        """
        Initialize connection with the SQLAlchemy engine

        Uses st.cache to only run once.
        """
        db_host = env.str("POSTGRES_HOST")
        db_user = env.str("POSTGRES_USER")
        db_port = env.int("POSTGRES_PORT")
        db_name = env.str("POSTGRES_DB")
        db_pass = env.str("POSTGRES_PASSWORD")
        engine = create_engine(
            f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
        )
        return engine.connect()



def inject_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
