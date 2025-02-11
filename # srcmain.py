# src/main.py
import time
import sys
from data_collector import collect_telemetry_data
from database_manager import DatabaseManager
from data_analyzer import DataAnalyzer
from data_visualizer import DataVisualizer
from stress_test import run_stress_test

def main(cpu_utilization):
    db_manager = DatabaseManager()

    # Run stress test to utilize CPU
    run_stress_test(cpu_utilization)

    # Collect and store data
    for _ in range(10):  # Collect data 10 timesa
        data = collect_telemetry_data()
        db_manager.insert_telemetry_data(data)
        time.sleep(1)  # Wait for 1 second before collecting the next data

    # Retrieve and analyze data
    data = db_manager.get_all_data()
    analyzer = DataAnalyzer(data)
    stats = analyzer.calculate_statistics()
    print(stats)

    # Visualize data
    visualizer = DataVisualizer(data)
    visualizer.plot_data()

if _name_ == "_main_":
    if len(sys.argv) != 2:
        print("Usage: python main.py <cpu_utilization_percentage>")
    else:
        cpu_utilization = int(sys.argv[1])
        main(cpu_utilization)
