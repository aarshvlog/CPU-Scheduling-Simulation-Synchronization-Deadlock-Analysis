import threading

counter = 0

# ---------- Unsynchronized Version ----------
barrier = threading.Barrier(2)

def race():
    global counter
    temp = counter          # Read
    barrier.wait()          # Force both threads to read same value
    counter = temp + 1      # Write


t1 = threading.Thread(target=race)
t2 = threading.Thread(target=race)

t1.start()
t2.start()

t1.join()
t2.join()

print("Unsynchronized Counter =", counter)
print("Expected = 2")
print("One increment is deterministically lost.\n")


# ---------- Synchronized Version ----------

counter = 0
lock = threading.Semaphore(1)

def safe_increment():
    global counter
    with lock:
        temp = counter
        counter = temp + 1


threads=[]

for i in range(2):
    t=threading.Thread(target=safe_increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Synchronized Counter =",counter)
print("Expected = 2")
