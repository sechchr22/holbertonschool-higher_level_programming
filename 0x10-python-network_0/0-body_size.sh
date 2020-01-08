#!/bin/bash
# Script that shows up the body size of the response
curl -s -o . "$1" -w "%{size_download}"
