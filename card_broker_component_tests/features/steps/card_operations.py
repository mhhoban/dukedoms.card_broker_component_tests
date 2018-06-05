from behave import given, then, when
from hamcrest import assert_that, equal_to, has_item

@when('card broker receives request for player card acquisition')
def acquire_card_request(context):
    """
    send request for a player card acquisition to Card Broker
    """
    game_id = int(context.table.rows[0]['game id'])
    player_id = int(context.table.rows[0]['player id'])
    card_id = int(context.table.rows[0]['card id'])

    _, result = context.clients.card_broker.cardOperations.acquire_card(
        acquireCardRequest={
                'playerId': player_id,
                'gameId': game_id,
                'cardId': card_id
        }
    ).result()

    assert_that(result.status_code, equal_to(200))
