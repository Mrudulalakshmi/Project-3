from main import select_model_llm

payload = {
    "description": "I have data on customer churn and want to predict if a customer will leave or not."
}

secrets = {
    "OPENAI_API_KEY": "" 
}

event_stream = []

result = select_model_llm(payload, secrets, event_stream)
print(result)
