from behave import given, then, when
from hamcrest import assert_that, equal_to

@when('card broker receives request for card state for player "{player_id:d}"')
def request_player_card_state(context, player_id):
    """
    requests current player card state from card broker
    """
    player_state, result = context.clients.card_broker.gameInfo.get_player_state(
        playerId=player_id
    ).result()

    context.player_state = None
    assert_that(result.status_code, equal_to(200))
    context.player_state = player_state

@then('card broker returns player card state')
def assert_player_card_state(context):
    """
    asserts that player hand/deck/discard numbers check out
    """
    assert_that(len(context.player_state.deck), equal_to(context.table.rows[0]['deck size'])
    assert_that(len(context.player_state.hand), equal_to(context.table.rows[0]['hand size'])
    assert_that(len(context.player_state.discard), equal_to(context.table.rows[0]['discard size'])
