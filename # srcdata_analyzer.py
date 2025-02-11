# src/data_analyzer.py
import pandas as pd

class DataAnalyzer:
    def _init_(self, data):
        self.df = pd.DataFrame(data, columns=['id', 'timestamp', 'cpu_usage', 'memory_usage', 'disk_usage', 'nic_usage'])

    def calculate_statistics(self):
        stats = {
            'cpu_usage': self.df['cpu_usage'].describe(),
            'memory_usage': self.df['memory_usage'].describe(),
            'disk_usage': self.df['disk_usage'].describe(),
            'nic_usage': self.df['nic_usage'].describe()
        }
        stats_df = pd.DataFrame(stats)aac
        stats_df.to_csv('telemetry_statistics.csv')  # Save statistics to CSV
        return stats
