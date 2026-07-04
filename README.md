# Live-Currency-converter

A Python currency converter that uses the Frankfurter API for live exchange-rate data and can be extended to support over 160 active currencies.  - No API key required.

## Features

- Converts between selected currencies
- Uses current exchange-rate data from the Frankfurter API
- Accepts input like `100GBP` or `100 GBP`
- Prompts for the currency separately if only the amount is entered
- Easy to expand with more supported currencies

## Requirements

- Python 3.x
requests library

## Installation

bash
git clone https://github.com/Kiam-Guest/Live-Currency-Converter.git
cd Live-Currency-Converter
pip install requests


## Usage

Run the script:

bash
python "Currency conversion.py"

Example:

text
Enter amount (e.g. 100 or 100GBP): 100GBP
To (GBP/USD/EUR/CAD/AUD): AUD
100.0 GBP = 192.49 AUD
Rate: 1.9249
Date: 2026-07-03


## Supported currencies

By default, the script is configured for:

- GBP
- USD
- EUR
- CAD
- AUD

This list can be expanded by editing the `ALLOWED` set in the script.
You should also update the user exception messages as best practise but this is not a strict requirement.

## API source

This project uses the [Frankfurter API](https://frankfurter.dev/) for exchange-rate data.

## License

MIT
