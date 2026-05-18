import os
from dotenv import load_dotenv
import requests

load_dotenv(".env")
webhook_url = os.environ.get("WEBHOOK_URL")

weather_api_url = "https://www.jma.go.jp/bosai/forecast/data/overview_forecast/260000.json"
response = requests.get(weather_api_url)
weather_data = response.json()

target_area = "吉田キャンパス(京都府南部)"
weather_text = weather_data["text"]

message = f"【{target_area}の天気情報】\n{weather_text}"

slack_data = {
    "text": message,
    "username": "吉田キャンパスの天気を知らせるアザラシ",
    "icon_url": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Spotted_Seal_mombestu2.jpg",
}
r = requests.post(webhook_url, json=slack_data)




