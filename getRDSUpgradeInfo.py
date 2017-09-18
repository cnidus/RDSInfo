import boto3
import pymysql
import os


def lambda_handler(event, context):

    cnx= {'host': os.environ['DBHost'],
          'username': os.environ['DBUser'],
          'password': os.environ['DBPass'],
          'db': os.environ['DBName'],
          'port': os.environ['DBPort']}

    try:
        db = pymysql.connect(cnx['host'],cnx['username'],cnx['password'],cnx['db'])
        print "Connected to RDS successfully. Hazah!"

        with db.cursor() as cur:
            sql = "show variables like '%version';"
            cur.execute(sql)
            result = cur.fetchone()
            print str(result)

    except Exception as e:
        print "Exception connecting to RDS: " + str(e)
        raise

    finally:
        db.close()
