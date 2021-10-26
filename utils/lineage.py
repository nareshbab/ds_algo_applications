import pandas as pd
from sqlalchemy import create_engine
import utils.config


# db_engine = create_engine('postgresql://localhost/mydatabase')
# table_name = "main_dag"
# all_dags = pd.read_sql(table_name, con=db_engine)
# all_dags.head()


def segment(x, space):
	mins = []
	for i in range(len(space)):
		elements = set()
		if len(space[i:i+x]) >= x:
			elements.update(set(space[i:i+x]))
		if len(elements) > 0:
			mins.append(min(elements))
	return max(mins)



print(segment(3, [2,5,4,6,8]))

