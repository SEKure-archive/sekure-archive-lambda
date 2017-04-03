#!/usr/bin/env python

import os
import sys

import db

# Connect to the database
connection = db.connect()
cursor = connection.cursor()

def handler(event, context):
    # Execute the stored procedure
    cursor.callproc('insert_file', (event['folder'], event['name'], event['mime'], event['size'], event['created'], event['s3']))
    success = cursor.fetchone()[0]

    # Commit the transaction
    if success:
        connection.commit()
    else:
        raise Exception('Database error.')

    # Close database connections
    cursor.close()
    connection.close()

    return True
