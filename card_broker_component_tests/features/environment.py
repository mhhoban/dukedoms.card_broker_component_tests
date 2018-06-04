from addict import Dict
from bravado.client import SwaggerClient
from bravado.swagger_model import load_file

def get_env_urls(env):
    urls = Dict()

    urls.container.card_broker = 'http://card-broker:8080'
    urls.container.card_broker_db = (
        'postgresql+psycopg2://postgres:daleria@dukedoms-rdbs:5432/card_broker'
    )

    urls.local.card_broker = 'http://127.0.0.1:5006'
    urls.local.card_broker_db = (
        'postgresql+psycopg2://postgres:daleria@127.0.0.1:5432/card_broker'
    )

    return urls.local if env == 'local' else urls.container

def before_scenario(context, step):

    config = {
        'also_return_response': True,
        'validate_responses': True,
        'validate_requests': True,
        'validate_swagger_spec': True,
        'use_models': True,
        'formats': []
    }

    context.urls = get_env_urls(context.config.userdata.get('env'))



    context.clients = Dict()
    context.clients.card_broker = SwaggerClient.from_spec(
        load_file(
            'specs/dukedoms_card_broker_api.yaml',
        ),
        origin_url=context.urls.card_broker,
        config=config
    )
