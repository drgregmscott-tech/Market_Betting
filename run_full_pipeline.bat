@echo off
cd /d C:\Users\gmsco\Desktop\Market_Betting
C:\Users\gmsco\AppData\Local\Python\pythoncore-3.14-64\python.exe scripts\ingestion\ingest_pickem.py
C:\Users\gmsco\AppData\Local\Python\pythoncore-3.14-64\python.exe scripts\estimation\pickem_model.py --season 2025
C:\Users\gmsco\AppData\Local\Python\pythoncore-3.14-64\python.exe scripts\calibration\clv_logger.py
