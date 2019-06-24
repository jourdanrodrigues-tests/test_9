#!/usr/bin/env bash

docker exec -it mozio_test_db psql -U postgres -c 'drop database test_mozio_test_db'
