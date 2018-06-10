from behave import given, then, when
from hamcrest import assert_that, equal_to, has_item

from player_operations import request_player_card_state
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

@when('card broker receives request for player "{player_id}" to draw a card')
def draw_card_request(context, player_id):
    """
    send request for player to draw a card from deck
    """
    player_id = int(player_id)
    request_player_card_state(context, player_id)
    context.pre_draw_hand_len = len(context.player_state.hand)
    context.pre_draw_deck_size = len(context.player_state.deck)
    _, result= context.clients.card_broker.cardOperations.draw_player_card(
        playerId=int(player_id)
    ).result()
    assert_that(result.status_code, equal_to(200))

@then('player "{player_id}" successfully draws a card')
def assert_card_drawn(context, player_id):
    """
    update player state, check that hand has grown by one
    """
    request_player_card_state(context, int(player_id))
    assert_that(len(context.player_state.hand), equal_to(context.pre_draw_hand_len + 1))
    assert_that(len(context.player_state.deck), equal_to(context.pre_draw_deck_size - 1))

@when('card broker receives request for player discard')
def send_player_discard_request(context):
    """
    sends request for player to discard card
    """
    player_id = int(context.table.rows[0]['player id'])
    card_slot = int(context.table.rows[0]['card slot'])

    request_player_card_state(context, int(player_id))
    context.pre_discard_hand_len = len(context.player_state.hand)
    context.pre_discard_discard_len = len(context.player_state.discard)
    _, result= context.clients.card_broker.cardOperations.discard_player_card(
        discardCardRequest={
            'playerId': player_id,
            'cardSlotId': int(card_slot)
        }
    ).result()
    assert_that(result.status_code, equal_to(200))

@then('player "{player_id}" discards card')
def assert_player_discard(context, player_id):
    """
    asserts that discard card action did occur
    """
    request_player_card_state(context, int(player_id))
    assert_that(len(context.player_state.hand), equal_to(context.pre_discard_hand_len - 1))
    assert_that(len(context.player_state.discard), equal_to(context.pre_discard_discard_len + 1))

@when('card broker receives request to curse players with data')
def request_player_curse(context):
    """
    sends request to card broker to distribute curse cards
    """
    _, result = context.clients.card_broker.cardOperations.curse_players(
        cursePlayersRequest= {
            'gameId':int(context.table.rows[0]['game id']),
            'cursingPlayerId':int(context.table.rows[0]['player id'])
        }
    ).result()

    assert_that(result.status_code, equal_to(200))

@then('players have curse cards in discard')
def assert_players_have_curses(context):
    """
    asserts that given list of players have curses at top of discard pile
    """
    player_ids = context.table.rows[0]['player ids'].split(',')
    CURSE_ID = 666
    for id in player_ids:
        request_player_card_state(context, int(id))
        assert_that(context.player_state.discard[-1], equal_to(CURSE_ID))
