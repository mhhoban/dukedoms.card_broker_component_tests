@card_broker
Feature: Card Broker
Background: New Game
  Given an empty card broker database
  and a new game with data:
    | game id | player ids |
    | 1337    | 1,3        |

  Scenario: Create New Game
    When card broker receives request for game state for game id "1337"
    Then card broker returns expected game state:
      | card id | supply | finite |
    When card broker receives request for card state for player "1"
    Then card broker returns player card state:
      | deck size | hand size | discard size |
      | 5         | 5         | 0            |
    When card broker receives request for card state for player "3"
    Then card broker returns player card state:
      | deck size | hand size | discard size |
      | 5         | 5         | 0            |

  Scenario: Player Acquires Card
    When card broker receives request for player card acquisition:
      | game id | player id | card id |
      | 1337    | 1         | 4       |
    Then player has card on top of "discard" pile:
      | player id | card id |
      | 1         | 4       |
    And game deck has size:
      | game id| card id | deck size    |
      | 1337   | 4       | 7            |

  Scenario: Player Draws Card
    When card broker receives request for player "3" to draw a card
    Then player "3" successfully draws a card

  @wip
  Scenario: Player Discards Card
    When card broker receives request for player discard:
      | player id | card slot |
      | 3         | 1         |
    Then player "3" discards card

  @wip
  Scenario: Player Discards Hand Then Draws New Hand
    When card broker receives request for player "3" to discard hand
    Then player "3" discards hand
    When card broker receives request for player "3" to draw hand
    Then player "3" draws a new hand

  @wip
  Scenario: Trash Player Card
    When card broker receives request for player to trash card:
      | player id | card slot |
      | 1         | 1         |
    Then card broker trashes player card:
      | player id | card slot |
      | 1         | 1         |

  @wip
  Scenario: Get Card Supply
    Given an empty card broker database
    When card broker receives request for game state for game "1337"
    Then card broker returns the expected game state
