# CI with GitHub Actions — Demo

This repository contains two GitHub Actions workflows demonstrating:
- **Continuous Integration** with unit tests on a **Python version matrix**
- A **scheduled (cron)** workflow that runs daily at **00:00 UTC**


## Repository Structure

ci-github-actions-demo/
├─ main.py
├─ test_main.py
└─ .github/
└─ workflows/
├─ ci.yml # runs on push/PR; matrix tests
└─ scheduled.yml # runs daily at 00:00 UTC (and on manual dispatch)






