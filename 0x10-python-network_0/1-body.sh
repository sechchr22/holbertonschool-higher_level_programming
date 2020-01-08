#!/bin/bash
# GET request to the URL and display the body only of a 200 status code
curl -s "$1" -X GET -L
