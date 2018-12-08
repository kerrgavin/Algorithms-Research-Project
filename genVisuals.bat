@echo off
for /f %%f in ('dir data\ /b') do python graphit.py %%f %%f
