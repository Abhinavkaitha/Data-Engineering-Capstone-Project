from airflow import DAG
from airflow.operators import BashOperator,PythonOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'Abhinav',
    'depends_on_past': False,
    'start_date': datetime.today(),
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
  }

dag = DAG('simple', default_args=default_args,description='Load and transform data',schedule_interval = '@once')

t1 = BashOperator(
task_id='Download',
bash_command='python Data-Engineering-Capstone-Project/src/data_extraction/Download_data.py',
dag=dag)

t2 = BashOperator(
task_id='Decompress',
bash_command='python Data-Engineering-Capstone-Project/src/data_extraction/Decompress.py',
dag=dag)

t3 = BashOperator(
task_id='Move to folders',
bash_command='python Data-Engineering-Capstone-Project/src/data_extraction/copy_bz2_to_multiple_folders.py',
dag=dag)

t1 >> t2
t2 >> t3
