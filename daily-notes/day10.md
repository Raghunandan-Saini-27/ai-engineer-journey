# Day 10

## C++
- Sliding window problems
- Fixed and variable window

## Backend
Built AI service:
- ML prediction API
- Stored predictions in SQLite DB
- Created endpoints:
  POST /predict
  GET /predictions

## DevOps
- Dockerized full AI service

## Automation
- Filtered jobs and stored in DB

## Key Learnings
- Combining ML + API + DB creates real systems
- Docker helps deploy full application
- Data persistence is important

## Problems Faced

Just some db related issues like the prediction data was not getting saved as sqlite doesnt exactly know about numpy elements so had to convert that first.