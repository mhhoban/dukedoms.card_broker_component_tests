from behave import given, then, when
from hamcrest import assert_that, equal_to, has_item

@when('card broker receives request to create new game with data')
def create_new_game(context):
    """
    Send request for card broker to create new game with data provided
    """
    game_id = context.table.rows[0]['game id']
    player_ids = [int(id) for id in context.table.rows[0]['player ids'].split(',')]

    _, result = context.clients.card_broker.newGame.new_game(
        newGameRequest={
            'gameId': game_id,
            'players': player_ids
        }
    ).result()

    context.result = result.status_code

@when('card broker receives request for game state for game id "{game_id:d}"')
def request_game_state(context):
    """
    Send request for game state
    """
    game_state, result = context.clients.card_broker.gameInfo.get_game_cards(
        gameId=game_id
    ).result()

    assert_that(result.status_code, equal_to(200))
    context.game_state = game_state

@then('card broker returns expected game state')
def assert_game_state(context):
    """
    Asserts that game state object returned contains expected contents
    """
    for row in context.table:
        content = {
            'cardId': row['card id'],
            'supply': row['supply'],
            'finite': row['finite']
        }

        assert_that(context.game_state, has_item(content))


@then('the request returns 200')
def assert_ok_response(context):
    """
    verify a 200 was returned by request
    """
    assert_that(context.result, equal_to(200))
