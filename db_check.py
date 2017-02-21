import cx_Oracle
con = cx_Oracle.connect('your_user/users_password@your_db_name')
print "DB Version:",con.version
print "TNS name:",con.tnsentry
print "connected user:",con.username

cur = con.cursor()
cur.execute('select status from v$instance')
for result in cur:
    print result
    cur.close()
con.close()
