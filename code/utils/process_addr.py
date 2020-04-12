from description import cities_mrs
import multiprocessing as mp
# import pycep_correios as pc
import pandas as pd
import datetime
import requests
import time
import glob
import env
import os
import re

def get_address(cep) -> {}:
    api = (
        'https://webmaniabr.com/api/1/cep/{}/'
        f'?app_key={env.app_key}'
        f'&app_secret={env.app_secret}'
    )
    return requests.get(api.format(cep)).json()

def process_addr(row: int, df: pd.DataFrame) -> pd.DataFrame:
    aux = df.loc[[row]]
    cep = str(aux.loc[row, 'CEP'])
#     addr = pc.get_address_from_cep(cep)
    addr = get_address(cep) # blocked by flood

    aux.loc[row, 'BAIRRO_RES'] = addr.get('bairro', '')
    
    id_city = str(aux.loc[row, 'MUNIC_RES'])
    aux.loc[row, 'MUNIC_RES'] = cities_mrs.get(id_city, id_city)
    
    id_city = str(aux.loc[row, 'MUNIC_MOV'])
    aux.loc[row, 'MUNIC_MOV'] = cities_mrs.get(id_city, id_city)
    
    return aux

# Directory for output
if not os.path.exists('.process'):
    os.mkdir('.process')

files = glob.glob('.buffer/*.gz')
for file in files:
    df = pd.read_csv(file, low_memory=False, compression='gzip')
    pool = mp.Pool(mp.cpu_count())
    results = pool.starmap_async(
        process_addr,
        [(row, df) for row in range(len(df))]
    ).get()
    pool.close()
    pool.join()
    
    out = f".process/{file.split('/')[-1]}"
    aux = pd.concat(list(results))
    aux.to_csv(out, index=False, compression='gzip')
    
    os.remove(file)
    print(f"[INFO] Done {file} (processed)")
    time.sleep(10)

path = f".process/*.csv.gz"
f_outs = glob.glob(path)

aux = pd.DataFrame()
for file in f_outs:
    print(f"[INFO] Merging [{file}]")
    df = pd.read_csv(file, low_memory=False, compression='gzip')
    aux = pd.concat([df, aux], ignore_index=True)

aux.to_csv("RD.csv.gz", index=False, compression='gzip')
print(f"[INFO] Done [RD.csv.gz]")