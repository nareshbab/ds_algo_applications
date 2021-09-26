import pandas as pd
from sqlalchemy import create_engine
import utils.config
db_engine = create_engine('postgresql://localhost/mydatabase')
table_name = "main_dag"
all_dags = pd.read_sql(table_name, con=db_engine)
all_dags.head()


