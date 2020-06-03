import pandas as pd
import glob
import SQL_utils
from ipdb import set_trace
import sys

# Variables de control
db_name = sys.argv[1]
table_name =  sys.argv[2]

# Carga de los datos
file = glob.glob('*csv')
data = pd.read_csv(file[0], sep = ',', index_col = 0)

# Condiciones de filtrado
condition_1 = (data['Year'] >= 2000).values
condition_2 = (data['Age'] == '18+').values
condition_final = condition_1 * condition_2

# Filtrado de los datos
target_data_raw = data[condition_final].reset_index()
target_data = [list(x) for x in target_data_raw.values]

# Verificacion de la base de datos
db = SQL_utils.connect_to_mysql()
if not SQL_utils.check_database(db, db_name):
    SQL_utils.create_db(db, db_name)
db.database = db_name

# Verificacion de la tabla_2
if not SQL_utils.check_table(db, table_name):
    SQL_utils.create_table(db, table_name)

# Llenado de la tabla
for movie in target_data:
    movie[2] = movie[2].upper()
    SQL_utils.insert_items(db, tuple(movie[2:]), table_name)

# Cerrado de la conexion
db.close()
