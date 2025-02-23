#!/usr/bin/python
# -*- coding: utf-8 -*-

from mysql.connector import MySQLConnection, Error
from configparser import ConfigParser

def get_config(filename = 'connect.ini', section = 'mysql'):
    # create a parser and read the ini filename
    parser = ConfigParser()
    parser.read(filename)
    
    # by defult read from section mysql
    db = {}
    
    if parser.has_section(section):
        items = parser.items(section)
        
        for item in items:
            db[item[0]] = item[1]
            
    else:
        raise Exception('Error while reading connect.ini')
        
    return db

def connect():
    db_config = get_config()
    
    try:
        conn = MySQLConnection(**db_config)
        
        if conn.is_connected():
            print('Connection established.')
        else:
            print('Connection failed.')
            
    except Error as error:
        print(error)
        
    finally:
        conn.close()
        print('Connection closed.')
        
if __name__ == '__main__':
    connect()
    