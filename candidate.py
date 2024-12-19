#!/usr/bin/env python3

import etcd3
from sys import argv

chave_lider = "lider"
chave_lock = "eleicao_lider"

def busca_lideranca(candidato_id):
    client = etcd3.client()

    ultimo_lider = None

    while True:
        client.watch(chave_lider)

        with client.lock(chave_lock):
            lider = client.get(chave_lider)[0]
            
            if lider:
                lider = lider.decode('utf-8')
                if lider == candidato_id:
                    input("Press ENTER to finish...")
                    client.delete(chave_lider)
                    print("End")
                    break
                               
                elif lider != ultimo_lider:
                    print(f"{lider} is the leader...")
                    ultimo_lider = lider
            else:
                print("Attempting leadership...")
                print("I am the LEADER!")
                client.put(chave_lider, candidato_id)
                ultimo_lider = None

if __name__ == "__main__":
    candidato_id = argv[1]
    busca_lideranca(candidato_id)