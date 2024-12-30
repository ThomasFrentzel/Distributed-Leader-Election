# Distributed Leader Election

A Python implementation of a Distributed Leader Election system using the etcd library. This project demonstrates how to ensure that only one process becomes the leader at a given time by using basic etcd API operations (`get`, `put`, `delete`, `lock`, `lease`, `refresh`, `watch`, `watch_once`).

## Features

- Automatic waiting for leader availability.
- Fault-tolerant: automatically elects a new leader if the current leader crashes or exits.
- Each candidate has a unique identifier.
- Candidates compete to become the leader by interacting with the etcd key-value store.
- If a leader already exists, candidates wait for the leader to terminate or abort before trying again.


The implementation ensures that only one process can become the leader at any time, providing a simple, robust solution to leader election in distributed systems.

## Operations Used
- `get`: Checks the current leader stored in `leader_key`.
- `put`: Claims leadership by writing the candidate's ID to `leader_key`.
- `delete`: Removes the leader's ID from `leader_key` once the leader has finished their execution.
- `lock`: Ensures only one candidate can attempt leadership at a time by preventing concurrent access to the critical section of code.
- `watch`: Tracks changes in the leadership key (`leader_key`), allowing candidates to react when the leadership status changes.


# Usage  

Run the program with a unique identifier for each candidate:  

```bash
python candidate.py <CANDIDATE_ID>
```

# Example Execution
Three candidates (A, B, C) competing for leadership:

Example with three candidates:

```bash
python candidate.py A
python candidate.py B
python candidate.py C
```

```bash

$ python candidate.py A            $ python candidate.py B              $ python candidate.py C
Candidate A                        Candidate B                          Candidate C
Attempting leadership...           Attempting leadership...             Attempting leadership...
I am the LEADER!                   A is the leader...                   A is the leader...
Press ENTER to finish...

<ENTER>
End                                 Attempting leadership...             Attempting leadership...
                                    I am the LEADER!                     B is the leader...
                                    Press ENTER to finish

                                    <CRASH/CTRL-C>
                                                                         Attempting leadership...
                                                                         I am the LEADER!
                                                                         Press ENTER to finish

                                                                         <ENTER>
                                                                         End
```

## Clone the repository:
   ```bash
   git clone https://github.com/ThomasFrentzel/Distributed-Leader-Election
 ```
