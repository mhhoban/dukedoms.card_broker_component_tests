#!/bin/bash

./oas_setup.sh
SERVICE=card_broker_component_tests
docker build --build-arg service=$SERVICE \
--tag "mhhoban/dukedoms-card-broker-tests:latest" .
