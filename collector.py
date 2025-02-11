# src/data_collector.py
import psutil
from datetime import datetime

def collect_telemetry_data():
    data = {
        'timestamp': datetime.now().isoformat(),
        'cpu_usage': psutil.cpu_percent(interval=1),
        'memory_usage': psutil.virtual_memory().percent,
        'disk_usage': psutil.disk_usage('/').percent,
        'nic_usage': psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    }
  return data
