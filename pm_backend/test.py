#!/usr/bin/python3
"""Simple test file.
"""
from database.db_procedure import DBProcedures


uuuser = DBProcedures.users_login('javier.pilco', 'ja-pi')

print(uuuser)
print(uuuser.to_dict())
