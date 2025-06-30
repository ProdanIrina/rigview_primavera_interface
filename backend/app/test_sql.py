import pyodbc
import getpass

password = getpass.getpass("Introdu parola pentru irina.prodan: ")

conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER=159.69.61.211\\TEST,1434;"
    f"DATABASE=RigView;"
    f"UID=irina.prodan;"
    f"PWD={password};"
    "TrustServerCertificate=yes;"
    "Encrypt=no"
)
print("Conexiune reușită!")
