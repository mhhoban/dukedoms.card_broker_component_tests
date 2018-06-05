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
    assert_that(len(context.player_state.deck), equal_to(int(context.table.rows[0]['deck size'])))
    assert_that(len(context.player_state.hand), equal_to(int(context.table.rows[0]['hand size'])))
    assert_that(
        len(context.player_state.discard), equal_to(int(context.table.rows[0]['discard size']))
    )

@then('player has card on top of "{list}" pile')
def assert_top_card(context, list):
    """
    asserts a given card is atop a given player's given card list
    """
    player_id = int(context.table.rows[0]['player id'])
    card_id = int(context.table.rows[0]['card id'])

    request_player_card_state(context, player_id)

    assert_that(context.player_state[list][-1], equal_to(card_id))
