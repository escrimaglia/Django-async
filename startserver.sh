#!/bin/bash
gunicorn mixedproject.asgi:application -c gunicorn.conf.py
