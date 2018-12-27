## xkcd word counter

Ever wondered how many words "exoplanet", "blag" or "kachunk" are used in xkcd comics? You came to the right place! This handy (but slow) tool lets you list all words and their number of uses. (Answer to the first question is 5, 3 and 14 respectively, in comics 1-2090)

## How to run

run with:

python ./explist.py

It lists the words from comics from `first` to `last`  (inclusive). These are variables, there's no fancy CLI. You may want to adjust these values as time passes or if you want only part of comics to be listed.

## Prerequisites

This script runs on python 3. It needs python compiled with openSSL as it uses `http.client.HTTPSConnection`.
