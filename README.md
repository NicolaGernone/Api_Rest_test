# Crypto Terminal

## Data
All necessary data is in `data/archive`.

## Create an interactive tool to answer the following questions
1) What coins are available in our dataset?
2) What was the Close price of X coin at date yyyy-mm-dd (eg: BTC in 2020-01-02)
3) Given a start date and end date, what are the best possible buy and sell times to maximise profit?

You can use any language and GUI (command line interface, streamlit, etc.).

## Bonus
These are not necessary for evaluation, but the candidate can use them to showcase his/her skills.
- Load the data into SQLite
- Create a REST API backend to serve the data to the tool
- Create a dashboard with useful metrics and graphs

## Usage

The commands are listed in the [Makefile](/Makefile).

To run the server use `make first`, it will create the docker env running the build the migrations and loading the csv files in the Database.

After this time you can use `make up` instead.

To consult easly the Data use `make user` to create a superuser and with it enter in the admin pannel. `localhost:5050/admin`

With the server up you will be able to make the call to the Api specifide in the yaml file [Api_Crypto_Coin](/NicolaGernone-Api_cryptoCoins-0.1-resolved.yaml).