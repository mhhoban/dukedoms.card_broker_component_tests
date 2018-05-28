@card_broker
Feature: Card Broker

  Scenario: Create New Game
    Given an empty card broker database
    When card broker receives request to create new game with data:
      | game id | player ids |
      | 1337    | 1,3        |
    Then the request is successful
    When card broker receives request for game state for game id "1337"
    Then card broker returns a game state
    When card broker receives request for card state for player
      | game id | player id |
      | 1337    | 1         |
    Then card broker returns a beginning player card state
    When card broker receives request for card state for player
      | game id | player id |
      | 1337    | 3         |
    Then card broker returns a beginning player card state

  Scenario: Player Acquires Card
    Given an empty card broker database
    And a new game with data:
      | game id | player ids |
      | 1337    | 1,3        |
    When card broker receives request for player card acquisition:
      | player id | card id |
      | 1         | 2       |
    Then player has card on top of discard pile
      | player id | card id |
      | 1         | 2       |

  Scenario: Player Draws Card and Discard Card
    Given an empty card broker database
    And a new game with data:
      | game id | player ids |
      | 1337    | 1,3        |
    When card broker receives request for player "3" to draw a card
    Then player "3" successfully draws a card
    When card broker receives request for player discard:
      | player id | card slot |
      | 3         | 1         |
    Then player "3" discards card

  Scenario: Player Discards Hand Then Draws New Hand
    Given an empty card broker database
    And a new game with data:
      | game id | player ids |
      | 1337    | 1,3        |
    When card broker receives request for player "3" to discard hand
    Then player "3" discards hand
    When card broker receives request for player "3" to draw hand
    Then player "3" draws a new hand

  Scenario: Trash Player Card
    Given an empty card broker database
    And a new game with data:
      | game id | player ids |
      | 1337    | 1,3        |
    When card broker receives request for player to trash card:
      | player id | card slot |
      | 1         | 1         |
    Then card broker trashes player card:
      | player id | card slot |
      | 1         | 1         |

  Scenario: Get Card Supply
    Given an empty card broker database
    And a new game with data:
      | game id | player ids |
      | 1337    | 1,3        |
    When card broker receives request for game state for game "1337"
    Then card broker returns the expected game state
