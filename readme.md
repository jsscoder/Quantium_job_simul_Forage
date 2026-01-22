# Quantium – Data Analytics Virtual Experience (Forage)

This repository contains my completed work for the **Quantium Data Analytics Virtual Experience Program on Forage**. The project simulates a real-world analytics workflow for **Soul Foods**, focusing on understanding the impact of a product price change using data generation, visualisation, testing, and continuous integration concepts.

---

## Overview

**Business Question:**

> *Were sales higher before or after the Pink Morsel price increase on 15 January 2021?*

To answer this, I:

* Generated and analysed sales data
* Built an interactive Dash dashboard
* Added region-level filtering
* Implemented automated tests
* Prepared the project for CI-style execution

---

## Task Breakdown

### Task 1 – Data Generation

* Generated daily sales data for the product **Pink Morsels**
* Covered January 2021
* Included multiple regions (north, east, south, west)
* Structured data for downstream analysis and visualisation

**Outcome:** A clean, reproducible dataset suitable for analysis.

---

### Task 2 – Exploratory Analysis

* Sorted sales data chronologically
* Compared trends before and after **15 January 2021**
* Identified a noticeable increase in sales following the price change

**Outcome:** Initial evidence suggesting higher post-price-increase sales.

---

### Task 3 – Dash Visualiser

* Built an interactive **Dash** application
* Added:

  * Clear title/header
  * Line chart of daily sales
  * Proper axis labels
  * Visual marker for the price increase date

**Outcome:** A visual answer to the business question.

---

### Task 4 – Region Filtering & Styling

* Added radio buttons to filter sales by region:

  * north
  * east
  * south
  * west
  * all
* Applied custom CSS styling for improved usability and presentation

**Outcome:** Stakeholders can explore region-specific trends interactively.

---

### Task 5 – Automated Testing

* Created a Dash test suite using **pytest** and **dash[testing]**
* Implemented tests to verify:

  * Presence of the dashboard header
  * Presence of the sales visualisation
  * Presence of the region selector

**Outcome:** Confidence that the app renders correctly and remains stable.

---

### Task 6 – Continuous Integration Readiness

* Implemented a bash script to automate test execution
* Script:

  * Runs tests inside a `uv`-managed environment
  * Correctly propagates pass/fail exit codes
* Enables easy integration with CI systems

**Outcome:** Tests can be executed automatically on every commit.

---

## Technologies Used

* Python
* Dash
* Plotly
* Pandas
* Pytest
* uv
* Bash

---

## Key Insight

Sales of Pink Morsels were **higher after the price increase on 15 January 2021**, and this trend was consistent across multiple regions. This suggests that the price increase did not negatively impact demand and may have coincided with increased overall sales.

---

## How to Run Locally

```bash
uv sync
python index.py
```

To run tests:

```bash
./run_tests.sh
```

---

## Final Notes

This project demonstrates an end-to-end analytics workflow: from data generation to insight communication, supported by automated testing and CI-friendly practices.

---

**Completed as part of the Quantium Data Analytics Virtual Experience on Forage.**
