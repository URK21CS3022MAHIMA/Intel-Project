# src/stress_test.py
import subprocess

def run_stress_test(cpu_percentage):
    duration = 60  # Run stress test for 60 seconds
    cpu_load = int(cpu_percentage / 100 * psutil.cpu_count())

    stress_cmd = f'stress-ng --cpu {cpu_load} --timeout {duration}s'
    subprocess.run(stress_cmd, shell=True)
