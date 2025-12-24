import requests

payload = {
    "dataframe_split": {
        "columns": ["pclass", "sex", "age", "sibsp", "parch", "fare"],
        "data": [[3, 1, 22.0, 1, 0, 7.25]]
    }
}

url = "http://127.0.0.1:1234/invocations"
try:
    response = requests.post(url, json=payload)
    print("Berhasil! Respon model:", response.json())
except Exception as e:
    print("Gagal terhubung:", e)