from main import train_test_split_csv

payload = {
    "csv_file": "sample_data_split.csv",
    "features": ["Age", "Income"],
    "target": "Purchased",
    "test_size": 0.4
}

secrets = {}
event_stream = []

result = train_test_split_csv(payload, secrets, event_stream)
print(result)
