from main import plot_csv_chart

payload = {
    "csv_file": "sample_data.csv",
    "x_col": "Year",
    "y_col": "Sales"
}

secrets = {} 
event_stream = []  

result = plot_csv_chart(payload, secrets, event_stream)
print(result)
