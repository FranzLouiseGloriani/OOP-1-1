import pyodbc

msa_drivers = [x for drivers in pyodbc.drivers() if 'access']

print(f'MS-ACCESS Drivers:{msa_drivers}')
