from main import feature_summary

payload = {
    "csv_file": "sample_data_feature_sum.csv"
}

secrets = {}
event_stream = []

result = feature_summary(payload, secrets, event_stream)
print(result)
