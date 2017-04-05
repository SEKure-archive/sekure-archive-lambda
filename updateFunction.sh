#!/bin/sh
name='upload-lambda'
aws lambda update-function-code --function-name $name --zip-file fileb://target/upload.zip
