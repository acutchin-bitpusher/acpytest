##  FROM: https://github.com/mattixtech/stress/blob/master/stress/stress.py

def _spin():
  while True:
    pass

def stress_processes(num_processes):
  import multiprocessing
  for _ in range(num_processes):
    multiprocessing.Process(target=_spin).start()

def stress_ram(ram_to_allocate_mb):
  import time
  try:
    _ = [0] * int(((ram_to_allocate_mb / 8) * (1024 ** 2)))
    while True:
      time.sleep(1)
  except MemoryError:
    stress_ram(int(ram_to_allocate_mb * 0.9))

def stress(cores_to_stress,memory_to_allocate):
  import multiprocessing
  import psutil
  import signal
  import sys
  signal.signal(signal.SIGINT, lambda x, y: sys.exit(1))
  if not cores_to_stress and not memory_to_allocate:
    cores_to_stress = multiprocessing.cpu_count()
    memory_to_allocate = psutil.virtual_memory().total
  if cores_to_stress:
    multiprocessing.Process(
      target=stress_processes,
      args=(
        cores_to_stress,
      )
    ).start()
  if memory_to_allocate:
    stress_ram(memory_to_allocate)
