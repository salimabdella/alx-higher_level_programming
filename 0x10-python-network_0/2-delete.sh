#!/bin/bash
# script that sends a DELETE request to $1 -> first arg
curl -sX DELETE "$1"
