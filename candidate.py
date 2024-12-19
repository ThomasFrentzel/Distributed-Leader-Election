#!/usr/bin/env python3

import etcd3
from sys import argv

leader_key = "leader"
election_lock_key = "election_leader"

def search_leadership(candidate_id):
    client = etcd3.client()

    last_leader = None

    while True:
        client.watch(leader_key)

        with client.lock(election_lock_key):
            leader = client.get(leader_key)[0]
            
            if leader:
                leader = leader.decode('utf-8')
                if leader == candidate_id:
                    input("Press ENTER to finish...")
                    client.delete(leader_key)
                    print("End")
                    break
                               
                elif leader != last_leader:
                    print(f"{leader} is the leader...")
                    last_leader = leader
            else:
                print("Attempting leadership...")
                print("I am the LEADER!")
                client.put(leader_key, candidate_id)
                last_leader = None

if __name__ == "__main__":
    candidate_id = argv[1]
    search_leadership(candidate_id)
