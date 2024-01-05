import pymysql

#DB연결
conn = pymysql.connect(host='localhost', port=3306, user='tpa', password='210302', db='tpadb')
curs = conn.cursor(pymysql.cursors.DictCursor)

clear_tbl = 'drop table if exists local_voucher'
curs.execute(clear_tbl)

mk_table = 'create table if not exists local_voucher (voucher_name text, voucher_phone text, voucher_category text, voucher_add text)'
curs.execute(mk_table)

conn.commit()

#종료
curs.close()
conn.close()
