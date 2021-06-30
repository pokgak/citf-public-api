# README

## Steps

1. parse csv from citf-public repo
2. transform csv to better format
3. save inside a db
4. serve data from API

## API Usecase

- show daily trends of vaccination

## API

- GET /daily
    - query params
        - from: date
        - until: date
        - type: FIRST, SECOND, ALL
        
- GET /cumulative
    - query params
        - from: date
        - until: date
        - type: FIRST, SECOND, ALL
