import logging
import os
import requests
import time
from flask import Flask, request, jsonify
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)
sentry_sdk.init(dsn=os.getenv("SENTRY_DSN"), integrations=[FlaskIntegration()])

messages = {
    'bot_about': 'Я тестовая версия бота!',
    'dns_about': 'DNS — российская компания, владелец розничной сети, специализирующейся на продаже компьютерной, цифровой и бытовой техники, а также производитель компьютеров, в том числе ноутбуков, планшетов и смартфонов.',
    'exit': 'Завершаю работу',
    'raft_about': 'RAFT — аутсорсинговая компания, занимаемся разработкой ПО для всемирно известных клиентов. У нас есть много интересных проектов и задач, о которых мы расскажем тебе на интервью.'
}

app = Flask(__name__)


@app.route("/respond", methods=["POST"])
def respond():
    # get detected intents
    body = list(request.json['annotations'][0]['intent_catcher'].items())
    body.sort(key=lambda x: x[1]['confidence'])
    detected_intent = body[-1]

    logger.info(f'data (type {type(body)}): {body}')

    return jsonify([{'text': messages[detected_intent[0]], 'confidence': detected_intent[1]['confidence'], 'skill_name': 'sample-skill'}])


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=3555)
