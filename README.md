# Prophet ML Modeling vs. Monte-Carlo Simulation

Comparing traditional finance modeling methods (Monte Carlo via Euler Discretization) with more novel techniques — that being modeling via machine learning — to determine a more viable trading strategy for event contract trading on Kalshi.

## Getting Started

Nearly everything revolving around this project can be run in Jupyter Notebook, meaning that getting started simply involves installing Jupyter and then installing any missing packages that we will need using [pip](https://pip.pypa.io/en/stable/).

```
pip install (package)
```

## Motivation and Beginnings

[Kalshi](https://kalshi.com/) is the fisrt ever CFTC-regulated exchange that allows investors to trade on event contracts, a class of assets that allows investors to invest and trade directly on the outcome of events. In their words, this system is the next evolution of regulated commodities, and expands the world of futures and markets, allowing people to trade on events they are fluent or interested in, without much of the traditional noise of investing.

As with any young market, the possibilities for arbitrage and alpha are endless, and Kalshi's markets, with such rapid turnover, especially within their daily and weekly markets, have the potential to allow for many strategies.

Now to the project itself; the key goal was to compare possible strategies for use on Kalshi's S&P 500 market and garner results about their effectiveness. One pick for this model comparison is Monte-Carlo Simulation, particularly via Euler Discretization, to predict stock pricing. The question became, was Monte-Carlo legitimately viable, or does it face severe pitfalls in accuracy. Next, pitting it against a novel method, machine learning, here with the Prophet API, with possible shortcomigns such as over/under fitting the data.

Initially, base models for the S&P 500 data were formed in `prophet_predictor.ipynb`. Further details and descriptions of very basic Prophet model creation, and also Euler Discretization, are in the file.

## Hyperparameter Tuning and Further Optimization

Obviously, using `m.fit(df)` is just not enough for a proper model, though we wish it was 😔. So, another notebook, `prophet_opt.ipynb` contains all of our optimization processes for the ML model. By the way, further documentation and info on Prophet can be found [here](https://peerj.com/preprints/3190/) for those interested.

Notable changes include, adding regressors, assessing changepoints created by the model, and, of course hyperparameter tuning of many variables; specific code and processes are in the file.

## Final Models



## Kalshi Results

