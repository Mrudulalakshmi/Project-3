from main import generate_synthetic_data

payload = {
    "row_count": 20,
    "schema": [
        {"name": "Income", "type": "numeric"},
        {"name": "Gender", "type": "categorical", "values": ["Male", "Female", "Other"]},
        {"name": "JoinDate", "type": "date"}
    ]
}

secrets = {}
event_stream = []

result = generate_synthetic_data(payload, secrets, event_stream)
print(result)
