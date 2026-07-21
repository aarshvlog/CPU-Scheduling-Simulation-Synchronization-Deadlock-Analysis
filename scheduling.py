from collections import deque

processes = [
    ("P1",0,5),
    ("P2",1,3),
    ("P3",2,8),
    ("P4",3,6),
    ("P5",4,2)
]

QUANTUM = 2


def print_result(name, wt, tat):
    print("\n",name)
    print("Process\tWT\tTAT")
    aw=0
    at=0
    for p in wt:
        print(p,"\t",wt[p],"\t",tat[p])
        aw+=wt[p]
        at+=tat[p]
    print("Average Waiting Time =",round(aw/len(wt),2))
    print("Average Turnaround Time =",round(at/len(tat),2))


def fcfs(data):
    time=0
    wt={}
    tat={}
    for pid,arr,burst in data:
        if time<arr:
            time=arr
        wt[pid]=time-arr
        time+=burst
        tat[pid]=wt[pid]+burst
    print_result("FCFS",wt,tat)


def sjf(data):
    n=len(data)
    done=[False]*n
    complete=0
    time=0
    wt={}
    tat={}
    while complete<n:
        ready=[]
        for i,(pid,a,b) in enumerate(data):
            if not done[i] and a<=time:
                ready.append((b,a,i,pid))
        if not ready:
            time+=1
            continue
        ready.sort()
        b,a,i,pid=ready[0]
        wt[pid]=time-a
        time+=b
        tat[pid]=wt[pid]+b
        done[i]=True
        complete+=1
    print_result("SJF",wt,tat)


def round_robin(data,q):
    remaining={p:b for p,a,b in data}
    arrival={p:a for p,a,b in data}
    burst={p:b for p,a,b in data}

    ready=deque()
    time=0
    completed={}
    visited=set()

    while len(completed)<len(data):

        for p,a,b in data:
            if a<=time and p not in visited and p not in completed:
                ready.append(p)
                visited.add(p)

        if not ready:
            time+=1
            continue

        p=ready.popleft()

        run=min(q,remaining[p])
        old=time
        time+=run
        remaining[p]-=run

        for x,a,b in data:
            if old<a<=time and x not in visited and x not in completed:
                ready.append(x)
                visited.add(x)

        if remaining[p]>0:
            ready.append(p)
        else:
            completed[p]=time

    wt={}
    tat={}
    for p,a,b in data:
        tat[p]=completed[p]-a
        wt[p]=tat[p]-b

    print_result("Round Robin",wt,tat)


fcfs(processes)
sjf(processes)
round_robin(processes,QUANTUM)
