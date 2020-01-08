#!/bin/bash
# GET request to the URL and display the body only of a 200 status code
# Send a GET request to get new location of file
curl "$1" -X GET -L
