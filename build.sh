#!/bin/sh

rm deps/db.pyc
mkdir -p target

build()
{
    rm -f target/$1.zip
    cd src
    zip ../target/$1.zip $1.py db.py psycopg2/* psycopg2/.libs/*
    cd ..
}

build upload
