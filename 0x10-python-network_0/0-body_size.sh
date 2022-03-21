#!/bin/bash
# script to get the content length from url
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
