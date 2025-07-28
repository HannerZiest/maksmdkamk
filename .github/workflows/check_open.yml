name: Check Math 2B Open Sections

on:
  schedule:
    - cron: '*/10 * * * *'  # runs every 10 minutes
  workflow_dispatch:  # allows manual runs from GitHub UI

jobs:
  check_open:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install requests beautifulsoup4

    - name: Run the bot script
      env:
        DISCORD_WEBHOOK_URL: ${{ secrets.DISCORD_WEBHOOK_URL }}
      run: |
        python check_math_open.py
