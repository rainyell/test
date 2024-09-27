import sqlite3
import sqlite3 as sql

import platform
import os

import datetime

system_os = platform.system()

path = os.path.dirname(os.path.abspath(__file__))

if system_os == "Windows":
    db = "database.db"
else:
    db = "database.db"

class Database():

    def __init__(self):
        global db
        self.con = sql.connect(db)
        self.con.row_factory = sql.Row
        self.cur = self.con.cursor()

    '''
    
    Region tables

    '''
    def list_region(self):
        self.cur.execute("select * from 'TBL_REGION'")
        result = self.cur.fetchall()
        result = [dict(row) for row in result]
        return result
    
    def view_region(self, region_id):
        self.cur.execute("select * from 'TBL_REGION' where region_id = " + region_id)
        result = self.cur.fetchall()
        return result
    
    def list_province(self):
        self.cur.execute("select * from 'TBL_PROVINCE'")
        result = self.cur.fetchall()
        return result

    def insert_region(self, region_name):
        date_now = datetime.datetime.now()
        
        self.cur.execute("""INSERT INTO TBL_REGION (region_name, created_date, modified_date) 
                        VALUES (?, ?, ?)""",(region_name, date_now.date(),  date_now.date()) )
        self.con.commit()
            
    def update_region(self, region_id, region_name):
        date_now = datetime.datetime.now()
        
        self.cur.execute("""UPDATE TBL_REGION set
                region_name = ?,
                modified_date = ?
                WHERE
                region_id = ? """,(region_name, date_now.date(), region_id) )
        self.con.commit()

    '''
    
    Province tables

    '''
    def list_province(self):
        self.cur.execute("select * from 'TBL_PROVINCE'")
        result = self.cur.fetchall()
        result = [dict(row) for row in result]
        return result
    
    def view_province(self, province_id):
        self.cur.execute("select * from 'TBL_PROVINCE' where province_id = " + province_id)
        result = self.cur.fetchall()
        return result
    
    def insert_province(self, province_name, region_id):
        date_now = datetime.datetime.now()
        
        self.cur.execute("""INSERT INTO TBL_PROVINCE (province_name, region_id, created_date, modified_date) 
                        VALUES (?, ?, ?, ?)""",(province_name, region_id, date_now.date(),  date_now.date()) )
        self.con.commit()
                        
    def update_province(self, province_id, province_name):
        date_now = datetime.datetime.now()
        
        self.cur.execute("""UPDATE TBL_PROVINCE set
                province_name = ?,
                modified_date = ?
                WHERE
                province_id = ? """,(province_name, date_now.date(), province_id) )
        self.con.commit()