#!/bin/bash

#fetch card broker API Spec

curl https://raw.githubusercontent.com/mhhoban/dukedoms.card_service_api/master/dukedoms_card_broker_api.yaml -O
mv dukedoms_card_broker_api.yaml card_broker_component_tests/specs/dukedoms_card_broker_api.yaml
