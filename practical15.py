import gc
import tracemalloc


class Node:
    def __init__(self):
        self.data = [0] * 100
        self.ref = self


def create_objects(n):
    for _ in range(n):
        Node()


def show_memory(label):
    current, peak = tracemalloc.get_traced_memory()
    print(label, "->", round(current / 1024, 1), "KB")


tracemalloc.start()
gc.disable()

show_memory("Initial memory ")
create_objects(5000)
show_memory("After creating cycles")

gc.set_debug(gc.DEBUG_STATS)
collected = gc.collect()
gc.set_debug(0)

print("Objects collected:", collected)
show_memory("After gc.collect() ")

gc.enable()
