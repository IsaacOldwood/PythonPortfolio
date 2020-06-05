import requests
import json

for pageNo in range(1,125):
    
    
    if pageNo % 20==0:
            
        print(f'Page {pageNo} complete')