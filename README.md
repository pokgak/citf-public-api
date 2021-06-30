# README

## Steps

1. parse csv from citf-public repo
2. transform csv to better format
3. save inside a db
4. serve data from API

## API Usecase

- show daily trends of vaccination

## API

Refer `/docs` for OpenAPI specs.

To start the server, run:

```
uvicorn main:app --reload
```

- GET /daily
    - query params
        - from: date
        - until: date
        - type: "first", "second", "total"
- GET /cumulative
    - query params
        - from: date
        - until: date
        - type: "first", "second", "total"
