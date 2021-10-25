from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud.exceptions import NotFound

credentials = service_account.Credentials.from_service_account_file('credbig.json')
client = bigquery.Client(credentials=credentials)

table = 'delman-interview.interview_mock_data'
QUERY = """
SELECT * FROM `delman-interview.interview_mock_data.vaccine-data`
"""
q = "select * from `interview_mock_data.vaccine_data`"

qq = "show tables"

try:
    t = client.list_tables(table)  # Make an API request.
    for i in t:
        print(i.table_id)
    # print("Table {} already exists.".format(table))
except NotFound:
    print("Table {} is not found.".format(table))

# import sys
# sys.exit()

def sch():
    query_job = client.query(q)
    rows = query_job.result()
    # print(rows)
    data = {}
    for id, row in enumerate(rows):
        gen = 'male' if id % 2 == 0 else 'female'
        print(f"insert into patients(name, gender, birthdate, no_ktp, address) values('lori {id}', '{gen}', '2021-01-{id+1}', '{row.no_ktp}', 'Ende, Nangapanda');")
        # print(f"ktp: {row.no_ktp}")
        # print(f"vaksin: {row.vaccine_type}")
        # print(f"dosis: {row.vaccine_count}")
        # print('-'*90)
        data[str(row.no_ktp)] = [str(row.vaccine_type), row.vaccine_count]
    return data

sch()
# d = sch()
# for i in d:
#     print(d.get(i)[0])