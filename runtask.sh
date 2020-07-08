#!/bin/bash
python manage.py scanner
timestamp=`date +%Y/%m/%d-%H:%M:%S`
echo "Scanner has run at $timestamp"