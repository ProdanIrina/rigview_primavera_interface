import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=159.69.61.211,1433;"
    "DATABASE=RigView;"
    "UID=irina.prodan;"
    "PWD=parola123;"
    "TrustServerCertificate=yes;"
    "Encrypt=no"
)
cursor = conn.cursor()
cursor.execute("SELECT GETDATE()")
print(cursor.fetchone())
cursor.close()
conn.close()
