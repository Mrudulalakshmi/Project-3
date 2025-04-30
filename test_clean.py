from main import auto_clean_dataset

payload = {
    "csv_file": "sample_dirty_data.csv",
    "all_columns": ["Name", "Age", "City", "Income"]
}

secrets = {}
event_stream = []

result = auto_clean_dataset(payload, secrets, event_stream)
print(result)
