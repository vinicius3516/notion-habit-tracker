import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

DIAS_SEMANA = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]

def date_exists(data_iso):
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    body = {
        "filter": {
            "property": "Date",
            "date": {
                "equals": data_iso
            }
        }
    }
    response = requests.post(url, headers=HEADERS, json=body)
    if response.status_code == 200:
        results = response.json().get("results", [])
        return len(results) > 0
    else:
        print(f"⚠️ Erro ao consultar data {data_iso}: {response.status_code} - {response.text}")
        return False

def lambda_handler(event, context):
    start_day = datetime.today()

    for i in range(7):
        dia = DIAS_SEMANA[i]
        data_iso = (start_day + timedelta(days=i)).strftime("%Y-%m-%d")

        if date_exists(data_iso):
            print(f"⏭️ Já existe: {dia} - {data_iso}")
            continue

        payload = {
            "parent": { "database_id": DATABASE_ID },
            "properties": {
                "Dia": {
                    "title": [
                        { "text": { "content": dia } }
                    ]
                },
                "Date": {
                    "date": {
                        "start": data_iso
                    }
                }
            }
        }

        response = requests.post("https://api.notion.com/v1/pages", headers=HEADERS, json=payload)

        if response.status_code == 200:
            print(f"✅ Criado: {dia} - {data_iso}")
        else:
            print(f"❌ Erro: {response.status_code} - {response.text}")
