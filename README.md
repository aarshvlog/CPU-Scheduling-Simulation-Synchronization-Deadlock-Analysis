# CPU-Scheduling-Simulation-Synchronization-Deadlock-Analysis

Deadlock Analysis
Scenario

Resources:

R1 = Database Connection
R2 = Cache Lock
R3 = File Lock

Processes:

P1
P2
P3
Resource Allocation Graph
R1 → P1
P1 → R2

R2 → P2
P2 → R3

R3 → P3
P3 → R1
Four Necessary Conditions
Mutual Exclusion

Each resource can be allocated to only one process at a time.

Hold and Wait

Each process holds one resource while requesting another.

No Preemption

Resources cannot be forcibly taken away from a process until it voluntarily releases them.

Circular Wait

P1 waits for P2, P2 waits for P3, and P3 waits for P1, creating a cycle.

Remove One Edge

Remove

P3 → R1

Breaking this request removes the circular wait and prevents the deadlock.

Deadlock Prevention Strategy

Resource Ordering

Assign every resource a fixed order:

Database
↓

Cache
↓

File

Processes must always request resources in this order.

Limitation

Resource ordering can reduce flexibility and may force processes to acquire resources earlier than needed, potentially lowering concurrency and resource utilization.
