from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('credbig.json')
client = bigquery.Client(credentials=credentials)

QUERY = """
SELECT * FROM `delman-interview.interview_mock_data.vaccine-data`
"""
q = "select count(no_ktp) from `delman-interview.interview_mock_data.vaccine-data`"

query_job = client.query(QUERY)
rows = query_job.result()
for row in rows:
    print(f"ktp: {row.no_ktp}")
    print(f"vaksin: {row.vaccine_type}")
    print(f"dosis: {row.vaccine_count}")
    print('-'*90)
