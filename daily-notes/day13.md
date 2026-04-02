# Day 13

## Project

* Fixed API pagination logic (page & limit handling)
* Corrected database query to return full job data instead of only titles
* Improved database function to support both paginated and full fetch
* Optimized search logic by preparing for SQL-based filtering (instead of Python filtering)

## DSA

* Studied Sliding Window concept (core pattern)
* Solved:

  * Maximum Sum Subarray of Size K
  * First Negative Number in Every Window

## Automation

* Strengthened understanding of scraping structure:

  * Identifying parent containers
  * Extracting nested elements (title, company, location)

## Key Learnings

* Pagination is essential for scalable APIs
* Avoid fetching unnecessary data from database
* Sliding window avoids recomputation → improves efficiency
* Always understand structure before scraping

## Problems Faced

* Confusion in applying sliding window transitions (i, j movement)
* Needed better clarity on when to shrink window
