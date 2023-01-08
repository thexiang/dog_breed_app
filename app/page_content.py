import sql_query
import pandas as pd


class BasePage:
    def __init__(self, conn):
        self.conn = conn

    def load_source_data(self):
        pass

    def get_transformed_data(self):
        pass

    def get_chart(self):
        pass


class RawDogPage(BasePage):

    def load_source_data(self):
        query = sql_query.RAW_DOG_QUERY
        df = pd.read_sql_query(sql=query, con=self.conn)
        return df

    def get_transformed_data(self):
        return self.load_source_data()



