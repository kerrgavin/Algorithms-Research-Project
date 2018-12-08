@echo off
for /f %%f in ('dir graphs\ /b') do python analyze.py %%f %%f.json
