#!/bin/bash
exec gunicorn run:app \
    --bind 0.0.0.0:5000 \
    --workers 2