# Day 11

## Project (AI Job Intelligence Platform)

### Architecture
- Created modular structure:
  - scraper/
  - database/
  - api/
  - data/

### Database
- Created jobs table
- Fields:
  - id
  - title
  - company
  - location
  - link
- Implemented:
  - create_jobs_table()
  - insert_job()
  - get_all_jobs()

### Scraper
- Scraped job data from website
- Extracted:
  - title
  - company
  - location
  - apply link
- Stored data directly into database

### API
- Built FastAPI endpoints:
  - GET /jobs → returns all jobs
  - GET /jobs/python → filtered jobs

## DSA
- Learned deque (double-ended queue)
- Operations:
  - push_front
  - push_back
  - pop_front
  - pop_back

## Key Learnings
- Importance of modular architecture
- Separation of concerns (scraper, DB, API)
- Real-world data pipeline structure

## Problems Faced

Some data conversion problems.And package clashes so setup Python Environment.