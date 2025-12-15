question = [
    "What are the different types of mathematics found in quantitative finance?",
    "What is arbitrage?",
    "What is put-call parity?",
    "What is the Central Limit Theorem and what are its Implications for finance?",
    "How is risk defined in mathematical terms?",
    "What is value at risk and how is it used?",
    "What is Extreme Value Theory?",
    "What is CrashMetrics?",
    "What is a coherent risk measure and what are its properties?",
    "What is Modern Portfolio Theory?",
    "What is the Capital Asset Pricing Model?",
    "What is Arbitrage Pricing Theory?",
    "What is Maximum Likelihood Estimation?",
    "What is cointegration?",
    "What is the Kelly criterion?",
    "Why hedge?",
    "What is marking to market and how does it affect risk management in derivatives trading?",
    "What is the Efficient Markets Hypothesis?",
    "What are the most useful performance measures?",
    "What is a utility function and how is it used?",
    "What is the difference between a quant and an actuary?",
    "What is a Wiener process/Brownian motion and what are its uses in finance?",
    "What is Jensen's Inequality and what is its role in finance?",
    "What is Ito's lemma?",
    "Why does risk-neutral valuation work?",
    "What is Girsanov's theorem, and why is it important in finance?",
    "What are the greeks?",
    "Why do quants like closed-form solutions?",
    "What are the forward and backward equations?",
    "What is the Black-Scholes equation?",
    "Which numerical method should I use and when?",
    "What is Monte Carlo simulation?",
    "What is the finite-difference method?",
    "What is a Poisson process and what are its uses in finance?",
    "What is a jump-diffusion model and how does it affect option values?",
    "What is meant by 'complete' and 'incomplete' markets?",
    "Can I use real probabilities to price derivatives?",
    "What is volatility?",
    "What is the volatility smile?",
    "What is GARCH?",
    "How do I dynamically hedge?",
    "What is serial autocorrelation and does it have a role in derivatives?",
    "What is dispersion trading?",
    "What is bootstrapping using discount factors?",
    "What is the LIBOR market model and its principal applications in finance?",
    "What is meant by the 'value' of a contract?",
    "What is calibration?",
    "What is Option Adjusted Spread?",
    "What is the market price of risk?",
    "Can I reverse engineer a partial differential equation to get at the model and contract?",
    "What is the difference between the equilibrium approach and the no-arbitrage approach to modelling?",
    "How good is the assumption of normal distributions for financial returns?",
    "How robust is the Black-Scholes model?",
    "Why is the lognormal distribution important?",
    "What are copulas and how are they used in quantitative finance?",
    "What is asymptotic analysis and how is it used in financial modelling?",
    "What is a free-boundary problem and what is the optimal-stopping time for an American option?",
    "What are low-discrepancy numbers?",
    "What are the bastard greeks?",
    "What are the stupidest things people have said about risk neutrality?",
    "What is the best-kept secret in quantitative finance?"
]

answers = [
    """
 Short answer
 The fields of mathematics most used in quantitative finance
 are those of probability theory and differential equations.
 And, of course, numerical methods are usually needed for
 producing numbers.
 Example
 The classical model for option pricing can be written as a
 partial differential equation. But the same model also has a
 probabilistic interpretation in terms of expectations.
    """,
    """
     Short answer
 Arbitrage is making a sure profit in excess of the risk-free
 rate of return. In the language of quantitative finance we can
 say that an arbitrage opportunity is a portfolio of zero value
 today which is of positive value in the future with positive
 probability, and of negative value in the future with zero
 probability.
 The assumption that there are no arbitrage opportunities in
 the market is fundamental to classical finance theory. This
 idea is popularly known as 'there's no such thing as a free
 lunch.'
 Example
 An at-the-money European call option with a strike of $100
 and an expiration of six months is worth $8. A European put
 with the same strike and expiration is worth $6. There are
 no dividends on the stock and a six-month zero-coupon bond
 with a principal of $100 is worth $97.
 Buy the call and a bond, sell the put and the stock, which will
 bring in $-8-97+6+100=$1. At expiration this portfolio
 will be worthless regardless of the final price of the stock.
 You will make a profit of $1 with no risk. This is arbitrage. It
 is an example of the violation of put call parity.
    """,
    """
     Short answer
 Put-call parity is a relationship between the prices of a
 European-style call option and a European-style put option,
 as long as they have the same strike and expiration:
 Call price - Put price = Stock price
 -Strike price (present valued from expiration).
 Example Stock price is $98, a European call option struck at
 $100 with an expiration of nine months has a value of $9.07.
 The nine-month, continuously compounded, interest rate is
 4.5%. What is the value of the put option with the same strike
 and expiration?
 By rearranging the above expression we find
 Put price = 9.07-98+100 e-0.045x0.75 = 7.75.
 The put must therefore be worth $7.75.
    """,
    """
     Short answer
 The distribution of the average of a lot of random numbers
 will be normal (also known as Gaussian) even when the indi
vidual numbers are not normally distributed.
 Example
 Play a dice game where you win $10 if you throw a six, but
 lose $1 if you throw anything else. The distribution of your
 profit after one coin toss is clearly not normal, it's bimodal
 and skewed, but if you play the game thousands of times
 your total profit will be approximately normal
    """,
    """
    Short answer
 In layman's terms, risk is the possibility of harm or loss. In
 finance it refers to the possibility of a monetary loss associated with investments.
 Example
 The most common measure of risk is simply standard devia
tion of portfolio returns. The higher this is, the more random
ness in a portfolio, and this is seen as a bad thing.
    """,
    """
     Short answer
 Value at Risk, or VaR for short, is a measure of the amount
 that could be lost from a position, portfolio, desk, bank, etc.
 VaR is generally understood to mean the maximum loss an
 investment could incur at a given confidence level over a
 specified time horizon. There are other risk measures used
 in practice but this is the simplest and most common.
 Example
 An equity derivatives hedge fund estimates that its Value at
 Risk over one day at the 95% confidence level is $500,000.
 This is interpreted as one day out of 20 the fund expects to
 lose more than half a million dollars.
    """,
    """
     Short answer
 Extreme Value Theory (EVT) is the mathematics behind
 extreme events. Some important results have analogies
 with the Central Limit Theorem, but instead of being about
 averages they are about extremes. Of course, whether one
 should even be talking about probabilities when talking about
 crashes is another matter. It's probably safer to look at
 worst-case scenarios.
 Example
 (Taken from McNeil, 1998.) Fit a Frechet distribution to the
 28 annual maxima of the SP500 index returns from 1960 to
 October 16th 1987, the business day before the '87 crash. In
 this dataset the largest fall was 'just' 6.7%. Now calculate the
 probability of various returns. For example, a 50-year return
 level is the level which on average should only be exceeded
 in one year every 50 years. The Frechet distribution gives the
 result as 24%. One business day later the index falls 20.4%.
    """,
    """
    Short answer
 CrashMetrics is a stress-testing methodology for evaluating
 portfolio performance in the event of extreme movements in
 financial markets. Like CAPM it relates moves in individual
 stocks to the moves in one or more indices but only during large moves. It is applicable to portfolios of equities and
 equity derivatives.
 Example
 Your portfolio contains many individual stocks and many
 derivatives of different types. It is perfectly constructed to
 profit from your view on the market and its volatility. But
 what if there is a dramatic fall in the market, perhaps 5%?
 What will the effect be on your P&L? And if the fall is 10%,
 20%...?
    """,
    """
     Short answer
 A risk measure is coherent if it satisfies certain simple,
 mathematical properties. One of these properties, which
 some popular measures do not possess is sub-additivity,
 that adding together two risky portfolios cannot increase the
 measure of risk.
 Example
 Artzner et al. (1997) give a simple example of traditional VaR
 which violates this, and illustrates perfectly the problems of
 measures that are not coherent. Portfolio X consists only of
 a far out-of-the-money put with one day to expiry. Portfolio
 Y consists only of a far out-of-the-money call with one day
 to expiry. Let us suppose that each option has a probability
 of 4% of ending up in the money. For each option individu
ally, at the 95% confidence level the one-day traditional VaR
 is effectively zero. Now put the two portfolios together and
 there is a 92% chance of not losing anything, 100% less two
 lots of 4%. So at the 95% confidence level there will be a sig
nificant VaR. Putting the two portfolios together has in this
 example increased the risk. 'A merger does not create extra
 risk' (Artzner et al. 1997).
    """,
    """
     Short answer
 The Modern Portfolio Theory (MPT) of Harry Markowitz
 (1952) introduced the analysis of portfolios of investments
 by considering the expected return and risk of individual
 assets and, crucially, their interrelationship as measured
 by correlation. Prior to this investors would examine
 investments individually, build up portfolios of favoured
 stocks, and not consider how they related to each other. In
 MPT diversification plays an important role.
 Example
 Should you put all your money in a stock that has low risk
 but also low expected return, or one with high expected
 return but which is far riskier? Or perhaps divide your
 money between the two. Modern Portfolio Theory addresses
 this question and provides a framework for quantifying and
 understanding risk and return.
    """,
    """
    Short answer
 The Capital Asset Pricing Model (CAPM) relates the returns
 on individual assets or entire portfolios to the return on the
 market as a whole. It introduces the concepts of specific risk
 and systematic risk. Specific risk is unique to an individual
 asset, systematic risk is that associated with the market. In
 CAPM investors are compensated for taking systematic risk
 but not for taking specific risk. This is because specific risk
 can be diversified away by holding many different assets.
 Example
 A stock has an expected return of 15% and a volatility of
 20%. But how much of that risk and return are related to
 the market as a whole? The less that can be attributed to
 the behaviour of the market, the better will that stock be for
 diversification purposes.
    """,
    """
     Short answer
 The Arbitrage Pricing Theory (APT) of Stephen Ross (1976)
 represents the returns on individual assets as a linear combination of multiple random factors. These random factors
 can be fundamental factors or statistical. For there to be
 no arbitrage opportunities there must be restrictions on the
 investment processes.
 Example
 Suppose that there are five dominant causes of randomness
 across investments. These five factors might be market as
 a whole, inflation, oil prices, etc. If you are asked to invest
 in six different, well-diversified portfolios then either one of
 these portfolios will have approximately the same risk and
 return as a suitable combination of the other five, or there
 will be an arbitrage opportunity.
    """,
    """
    Short answer
 Maximum Likelihood Estimation (MLE) is a statistical technique for estimating parameters in a probability distribution.
 We choose parameters that maximize the a priori probability
 of the final outcome actually happening.
 Example
 You have three hats containing normally distributed random
 numbers. One hat's numbers have a mean of zero and a standard deviation of 0.1. This is hat A. Another hat's numbers
 have a mean of zero and a standard deviation of 1. This is
 hat B. The final hat's numbers have a mean of zero and a
 standard deviation of 10. This is hat C. You don't know which
 hat is which.
 You pick a number out of one hat. It is -2.6. Which hat do
 you think it came from? MLE can help you answer this question.
    """,
    """
     Short answer
 Two time series are cointegrated if a linear combination has
 constant mean and standard deviation. In other words, the
 two series never stray too far from one another. Cointegra
tion is a useful technique for studying relationships in mul
tivariate time series, and provides a sound methodology for
 modelling both long-run and short-run dynamics in a financial
 system.
 Example
 Suppose you have two stocks S1 and S2 andyoufindthat
 S1 -3 S2 is stationary, so that this combination never strays
 too far from its mean. If one day this 'spread' is particularly
 large then you would have sound statistical reasons for think
ing the spread might shortly reduce, giving you a possible
 source of statistical arbitrage profit. This can be the basis for
 pairs trading
    """,
    """
    Short answer
 The Kelly criterion is a technique for maximizing expected
 growth of assets by optimally investing a fixed fraction of
 your wealth in a series of investments. The idea has long
 been used in the world of gambling.
 Example
 You own a biased coin that will land heads up with probability p> 1
 2. You find someone willing to bet any amount against
 you at evens. They are willing to bet any number of times.
 Clearly you can make a lot of money with this special coin.
 You start with $1,000. How much of this should you bet?
    """,
"""
 Short answer
 'Hedging' in its broadest sense means the reduction of
 risk by exploiting relationships or correlation (or lack of
 correlation) between various risky investments. The purpose
 behind hedging is that it can lead to an improved risk/return.
 In the classical Modern Portfolio Theory framework, for
 example, it is usually possible to construct many portfolios
 having the same expected return but with different variance
 of returns ('risk'). Clearly, if you have two portfolios with
 the same expected return the one with the lower risk is the
 better investment.
 Example
 You buy a call option, it could go up or down in value
 depending on whether the underlying go up or down. So now
 sell some stock short. If you sell the right amount short then
 any rises or falls in the stock position will balance the falls
 or rises in the option, reducing risk.
""",
    """
    Short answer
 Marking to market means valuing an instrument at the price
 at which it is currently trading in the market. If you buy an
 option because you believe it is undervalued then you will
 not see any profit appear immediately, you will have wait
 until the market value moves into line with your own esti
mate. With an option this may not happen until expiration.
 When you hedge options you have to choose whether to
 use a delta based on the implied volatility or your own esti
mate of volatility. If you want to avoid fluctuations in your
 mark-to-market P&L you will hedge using the implied volatil
ity, even though you may believe this volatility to be incor
rect.
 Example
 A stock is trading at $47, but you think it is seriously under
valued. You believe that the value should be $60. You buy
 the stock. How much do you tell people your little 'portfolio'
 is worth? $47 or $60? If you say $47 then you are marking to
 market, if you say $60 you are marking to (your) model. Obvi
ously this is open to serious abuse and so it is usual, and
 often a regulatory requirement, to quote the mark-to-market
 value. If you are right about the stock value then the profit
 will be realized as the stock price rises. Patience, my son.
    """,
    """
     Short answer
 An efficient market is one where it is impossible to beat the
 market because all information about securities is already
 reflected in their prices.
 Example
 Or rather a counter-example, ''I'd be a bum in the street with
 a tin cup if the markets were efficient,'' Warren Buffett.
    """,
    """
     Short answer
 Performance measures are used to quantify the results of a
 trading strategy. They are usually adjusted for risk. The most
 popular is the Sharpe ratio.
 Example
 One stock has an average growth of 10% per annum, another
 is 30% per annum. You'd rather invest in the second, right?
 What if I said that the first had a volatility of only 5%,
 whereas the second was 20%, does that make a difference?
    """,
    """
     Short answer
 A utility function represents the 'worth,' 'happiness' or 'satis
faction' associated with goods, services, events, outcomes,
 levels of wealth, etc. It can be used to rank outcomes, to
 aggregate 'happiness' across individuals and to value games
 of chance.
 Example
 You own a valuable work of art; you are going to put it up
 for auction. You don't know how much you will make but
 the auctioneer has estimated the chances of achieving cer
tain amounts. Someone then offers you a guaranteed amount
 provided you withdraw the painting from the auction. Should
 you take the offer or take your chances? Utility theory can
 help you make that decision.
    """,
    """
     Short answer
 The answer is 'Lots.' They can both learn a lot from each
 other.
 Example
 Actuaries work more than quants with historical data and
 that data tends to be more stable. Think of mortality statis
tics. Quants often project forward using information con
tained in a snapshot of option prices.
    """,
    """
     Short answer
 The Wiener process or Brownian motion is a stochastic pro
cess with stationary independent normally distributed incre
ments and which also has continuous sample paths. It is the
 most common stochastic building block for random walks in
 f
 inance.
 Example
 Pollen in water, smoke in a room, pollution in a river, are all
 examples of Brownian motion. And this is the common model
 for stock prices as well.
    """,
    """
    Short answer
 Jensen's Inequality states1 that if f(*) is a convex function
 and x is a random variable then
 E[f(x)] ≥ f (E[x]).
 This justifies why non-linear instruments, options, have inher
ent value.
 Example
 You roll a die, square the number of spots you get, you win
 that many dollars. For this exercise f(x) isx2 a convex func
tion. So E[f(x)] is 1 +4+9+16+25+36 = 91 divided by 6,
 so 15 1/6. But E[x] is31/2sof (E[x]) is 12 1/4.
    """,
    """
     Short answer
 Ito
 o's lemma is a theorem in stochastic calculus. It tells you
 that if you have a random walk, in y, say, and a function of
 that randomly walking variable, call it f(y,t), then you can
 easily write an expression for the random walk in f. A func
tion of a random variable is itself random in general.
 Example
 The obvious example concerns the random walk
 dS =µSdt+σSdX
 commonly used to model an equity price or exchange rate, S.
 What is the stochastic differential equation for the logarithm
 of S, lnS?
 The answer is
 d(lnS) = µ- 1
 2σ2 dt+σ dX.
    """,
    """
     Short answer
 Risk-neutral valuation means that you can value options in
 terms of their expected payoffs, discounted from expiration
 to the present, assuming that they grow on average at the
 risk-free rate.
 Option value = Expected present value of payoff
 (under a risk-neutral random walk).
 Therefore the real rate at which the underlying grows on
 average doesn't affect the value. Of course, the volatility,
 related to the standard deviation of the underlying's return,
 does matter. In practice, it's usually much, much harder to
 estimate this average growth than the volatility, so we are
 rather spoiled in derivatives, that we only need to estimate
 the relatively stable parameter, volatility.2 The reason that
 this is true is that by hedging an option with the underly
ing we remove any exposure to the direction of the stock,
 whether it goes up or down ceases to matter. By eliminating
 risk in this way we also remove any dependence on the value
 of risk. End result is that we may as well imagine we are in
 a world in which no one values risk at all, and all tradeable
 assets grow at the risk-free rate on average.
 For any derivative product, as long as we can hedge it
 dynamically and perfectly (supposing we can as in the case
 of known, deterministic volatility and no defaults) the hedged
 portfolio loses its randomness and behaves like a bond.
  Example
 A stock whose value is currently $44.75 is growing on aver
age by 15% per annum. Its volatility is 22%. The interest rate
 is 4%. You want to value a call option with a strike of $45,
 expiring in two months' time. What can you do?
 First of all, the 15% average growth is totally irrelevant. The
 stock's growth and therefore its real direction does not affect
 the value of derivatives. What you can do is simulate many,
 many future paths of a stock with an average growth of 4%
 per annum, since that is the risk-free interest rate, and a 22%
 volatility, to find out where it may be in two months' time.
 Then calculate the call payoff for each of these paths. Present
 value each of these back to today, and calculate the aver
age over all paths. That's your option value. (For this simple
 example of the call option there is a formula for its value,
 so you don't need to do all these simulations. And in that
 formula you'll see an r for the risk-free interest rate, and no
 mention of the real drift rate.)
    """,
    """
     Short answer
 Girsanov's theorem is the formal concept underlying the
 change of measure from the real world to the risk-neutral
 world. We can change from a Brownian motion with one drift
 to a Brownian motion with another.
 Example
 The classical example is to start with
 dS =µSdt+σSdWt
 with W being Brownian motion under one measure (the
 real-world measure) and converting it to
 dS =rS dt +σSd ˜ Wt
 under a different, the risk-neutral, measure.
    """,
    """
     Short answer
 The 'greeks' are the sensitivities of derivatives prices
 to underlyings, variables and parameters. They can be
 calculated by differentiating option values with respect to
 variables and/or parameters, either analytically, if you have a
 closed-form formula, or numerically.
 Example
 Delta, 
= ∂V
 ∂S , is the sensitivity of an option price to the
 stock price. Gamma, Ŵ = ∂2V
 ∂S2 
, is the second derivative of the
 option price to the underlying stock, it is the sensitivity of
 the delta to the stock price. These two examples are called
 greek because they are members of the Greek alphabet. Some
 sensitivities, such as vega = ∂V
 ∂σ , are still called 'greek' even
 though they aren't in the Greek alphabet.
    """,
    """
     Short answer
 Because they are fast to compute and easy to understand.
 Example
 The Black-Scholes formulæ are simple and closed form and
 often used despite people knowing that they have limitations,
 and despite being used for products for which they were not
 originally intended.
    """,
"""
 Short answer
 Forward and backward equations usually refer to the
 differential equations governing the transition probability
 density function for a stochastic process. They are diffusion
 equations and must therefore be solved in the appropriate
 direction in time, hence the names.
 Example
 An exchange rate is currently 1.88. What is the probability
 that it will be over 2 by this time next year? If you have a
 stochastic differential equation model for this exchange rate
 then this question can be answered using the equations for
 the transition probability density function.
""",
    """
    Short answer
 The Black-Scholes equation is a differential equation for the
 value of an option as a function of the underlying asset and
 time.
 Example
 The basic equation is
 ∂V
 ∂t + 1
 2σ2S2∂2V
 ∂S2 
+rS∂V
 ∂S -rV =0,
 where V(S,t) is the option value as a function of asset price
 S and time t.
 There have been many extensions to this model, some people
 call them 'improvements.' But these extensions are all trivial
 compared with the breakthrough in modelling that was the
 original equation.
    """,
    """
    Short answer
 The three main numerical methods in common use are Monte
 Carlo, finite difference and numerical quadrature. (I'm includ
ing the binomial method as just a simplistic version of finite
 differences.) Monte Carlo is great for complex path depen
dency and high dimensionality, and for problems which can
not easily be written in differential equation form. Finite dif
ference is best for low dimensions and contracts with deci
sion features such as early exercise, ones which have a differ
ential equation formulation. Numerical quadrature is for when
 you can write the option value as a multiple integral.
 Example
 You want to price a fixed-income contract using the BGM
 model. Which numerical method should you use? BGM is
 geared up for solution by simulation, so you would use a
 Monte Carlo simulation.
 You want to price an option which is paid for in instalments,
 and you can stop paying and lose the option at any time if
 you think it's not worth keeping up the payments. This may
 be one for finite-difference methods since it has a decision
 feature.
 You want to price a European, non-path-dependent contract
 on a basket of equities. This may be recast as a multiple inte
gral and so you would use a quadrature method.
    """,
    """
     Short answer
 Monte Carlo simulations are a way of solving probabilistic
 problems by numerically 'imagining' many possible scenar
ios or games so as to calculate statistical properties such as
 expectations, variances or probabilities of certain outcomes.
 In finance we use such simulations to represent the future
 behaviour of equities, exchange rates, interest rates, etc., so
 as to either study the possible future performance of a port
folio or to price derivatives.
 Example
 We hold a complex portfolio of investments, we would like
 to know the probability of losing money over the next year
 since our bonus depends on our making a profit. We can
 estimate this probability by simulating how the individual
 components in our portfolio might evolve over the next year.
 This requires us to have a model for the random behaviour
 of each of the assets, including the relationship or correlation
 between them, if any.
 Some problems which are completely deterministic can also
 be solved numerically by running simulations, most famously
 f
 inding a value for π.
    """,
    """
     Short answer
 The finite-difference method is a way of approximating dif
ferential equations, in continuous variables, into difference
 equations, in discrete variables, so that they may be solved
 numerically. It is a method particularly useful when the prob
lem has a small number of dimensions, that is, independent
 variables.
 Example
 Many financial problems can be cast as partial differential
 equations. Usually these cannot be solved analytically and so
 they must be solved numerically.
    """,
    """
    Short answer
 The Poisson process is a model for a discontinuous random
 variable. Time is continuous, but the variable is discrete. The
 variable can represent a 'jump' in a quantity or the occur
rence of an 'event.'
 Example
 The Poisson process is used to model radioactive decay. In
 f
 inance it can be used to model default or bankruptcy, or to
 model jumps in stock prices.
    """,
    """
     Short answer
 Jump-diffusion models combine the continuous Brownian
 motion seen in Black-Scholes models (the diffusion) with
 prices that are allowed to jump discontinuously. The tim
ing of the jump is usually random, and this is represented
 by a Poisson process. The size of the jump can also be ran
dom. As you increase the frequency of the jumps (all other
 parameters remaining the same), the values of calls and puts
 increase. The prices of binaries, and other options, can go
 either up or down.
 Example
 A stock follows a lognormal random walk. Every month you
 roll a dice. If you roll a one then the stock price jumps dis
continuously. The size of this jump is decided by a random
 number you draw from a hat. (This is not a great example
 because the Poisson process is a continuous process, not a
 monthly event.)
    """,
    """
    Short answer
 A complete market is one in which a derivative product can
 be artificially made from more basic instruments, such as
 cash and the underlying asset. This usually involves dynam
ically rebalancing a portfolio of the simpler instruments,
 according to some formula or algorithm, to replicate the
 more complicated product, the derivative. Obviously, an
 incomplete market is one in which you can't replicate the
 option with simpler instruments.
 Example
 The classic example is replicating an equity option, a call,
 say, by continuously buying or selling the equity so that you
 always hold the amount
 =e-D(T-t)N(d1),
 in the stock, where
 N(x) = 1
 √
 2π
 and
 x
 -∞
 e-1
 2φ2dφ
 d1 = ln(S/E)+(r -D+ 1
 2σ2)(T -t)
 σ√T -t
    """,
    """
     Short answer
 Yes. But you may need to move away from classical quantita
tive finance.
 Example
 Some modern derivatives models use ideas from utility the
ory to price derivatives. Such models may find a use in pric
ing derivatives that cannot be dynamically hedged.
    """,
    """
     Short answer
 Volatility is annualized standard deviation of returns. Or is it?
 Because that is a statistical measure, necessarily backward
 looking, and because volatility seems to vary, and we want to
 know what it will be in the future, and because people have
 different views on what volatility will be in the future, things
 are not that simple.
 Example
 Actual volatility is the σ that goes into the Black-Scholes
 partial differential equation. Implied volatility is the number
 in the Black-Scholes formula that makes a theoretical price
 match a market price.
    """,
    """
     Short answer
 Volatility smile is the phrase used to describe how the
 implied volatilities of options vary with their strikes. A smile
 means that out-of-the-money puts and out-of-the-money
 calls both have higher implied volatilities than at-the-money
 options. Other shapes are possible as well. A slope in the
 curve is called a skew. So a negative skew would be a
 download-sloping graph of implied volatility versus strike.
    """,
    """
     Short answer
 GARCH stands for Generalized Auto Regressive Conditional
 Heteroscedasticity. This is an econometric model used for
 modelling and forecasting time-dependent variance, and
 hence volatility, of stock price returns. It represents current
 variance in terms of past variance(s).
 Example
 The simplest member of the GARCH family is GARCH(1,1) in
 which the variance, vn, of stock returns at time step n is mod
elled by
 vn = (1-α-β)w0+βvn-1 +αvn-1B2
 n-1,
 where w0 is the long-term variance, α and β are positive
 parameters, with α +β<1, and Bn are independent Brownian
 motions, that is, random numbers drawn from a normal
 distribution. The latest variance, vn, can therefore be thought
 of as a weighted average of the most recent variance, the
 latest square of returns, and the long-term average.
    """,
    """
    Short answer
 Dynamic hedging, or delta hedging, means the continuous
 buying or selling of the underlying asset according to some
 formula or algorithm so that risk is eliminated from an option
 position. The key point in this is what formula do you use,
 and, given that in practice you can't hedge continuously, how
 should you hedge discretely? First, get your delta correct,
 and this means use the correct formula and estimates for
 parameters, such as volatility. Second, decide when to hedge
 based on the conflicting desires of wanting to hedge as often
 as possible to reduce risk, but as little as possible to reduce
 any costs associated with hedging.
 Example
 The implied volatility of a call option is 20% but you think
 that is cheap and volatility is nearer 40%. Do you put 20% or
 40% into the delta calculation? The stock then moves, should
 you rebalance, incurring some inevitable transactions costs,
 or wait a bit longer while taking the risks of being unhedged?
    """,
    """
     Short answer
 Serial autocorrelation (SAC) is a temporal correlation between
 a time series and itself, meaning that a move in, say, a stock
 price one day is not independent of the stock move on a
 previous day. Usually in quantitative finance we assume that
 there is no such memory, that's what Markov means. We can
 measure, and model, such serial autocorrelation with differ
ent 'lags.' We can look at the SAC with a one-day lag, this
 would be the correlation between moves one day and the day
 before, or with a two-day lag, that would be the correlation
 between moves and moves two days previously, etc.
 Example
 Figure 2.12 shows the 252-day rolling SAC, with a lag of one
 day, for the Dow Jones Industrial index. It is clear from this
 that there has been a longstanding trend since the late 1970s
 going from extremely positive SAC to the current extremely
 negative SAC. (I imagine that many people instinctively felt
 this!)
    """,
    """
     Short answer
 Dispersion trading is a strategy involving the selling of
 options on an index against buying a basket of options on
 individual stocks. Such a strategy is a play on the behaviour
 of correlations during normal markets and during large
 market moves. If the individual assets returns are widely
 dispersed then there may be little movement in the index,
 but a large movement in the individual assets. This would
 result in a large payoff on the individual asset options but
 little to payback on the short index option.
 Example
 You have bought straddles on constituents of the SP500
 index, and you have sold a straddle on the index itself. On
 most days you don't make much of a profit or loss on this
 position, gains/losses on the equities balance losses/gains on
 the index. But one day half of your equities rise dramatically,
 and one half fall, with there being little resulting move in the
 index. On this day you make money on the equity options
 from the gammas, and also make money on the short index
 option because of time decay. That was a day on which the
 individual stocks were nicely dispersed.
    """,
    """
     Short answer
 Bootstrapping means building up a forward interest-rate
 curve that is consistent with the market prices of common
 f
 ixed-income instruments such as bonds and swaps. The
 resulting curve can then be used to value other instruments,
 such as bonds that are not traded.
 Example
 You know the market prices of bonds with one, two three,
 f
 ive years to maturity. You are asked to value a four-year
 bond. How can you use the traded prices so that your
 four-year bond price is consistent?
    """,
"""
 Short answer
 The LIBOR Market Model (LMM), also known as the BGM or
 BGM/J model, is a model for the stochastic evolution of for
ward interest rates. Its main strength over other interest rate
 models is that it describes the evolution of forward rates that
 exist, at market-traded maturities, as opposed to theoretical
 constructs such as the spot interest rate.
 Example
 In the LMM the variables are a set of forward rates for
 traded, simple fixed-income instruments. The parameters are
 volatilities of these and correlations between them. From no
 arbitrage we can find the risk-neutral drift rates for these
 variables. The model is then used to price other instruments.
""",
    """
     Short answer
 Value usually means the theoretical cost of building up a new
 contract from simpler products, such as replicating an option
 by dynamically buying and selling stock.
 Example
 Wheels cost $10 each. A soapbox is $20. How much is a
 go-cart? The value is $60.
    """,
    """
     Short Answer
 Calibration means choosing parameters in your model so
 that the theoretical prices for exchange-traded contracts out
put from your model match exactly, or as closely as possi
ble, the market prices at an instant in time. In a sense it is
 the opposite of fitting parameters to historical time series. If
 you match prices exactly then you are eliminating arbitrage
 opportunities, and this is why it is popular.
 Example
 You have your favourite interest rate model, but you don't
 know how to decide what the parameters in the model
 should be. You realize that the bonds, swaps and swaptions
 markets are very liquid, and presumably very efficient. So
 you choose your parameters in the model so that your
 model's theoretical output for these simple instruments is
 the same as their market prices.
    """,
    """
     Short answer
 The Option Adjusted Spread (OAS) is the constant spread
 addedtoaforwardorayieldcurvetomatchthemarket
 price of some complex instrument and the present value of
 all its cash flows.
 Example
 Analyses using Option Adjusted Spreads are common in
 Mortgage-Backed Securities (MBS).
    """,
    """
     Short answer
 The market price of risk is the return in excess of the
 risk-free rate that the market wants as compensation for
 taking risk.
 Example
 Historically a stock has grown by an average of 20% per
 annum when the risk-free rate of interest was 5%. The
 volatility over this period was 30%. Therefore, for each unit
 of risk this stock returns on average an extra 0.5 return
 above the risk-free rate. This is the market price of risk.
    """,
    """
     Short answer
 Very often you can. You just need to understand what all the
 terms in a financial partial differential equation represent, all
 those ∂ this
 ∂ that terms and their coefficients. And the final condi
tion for the PDE defines the contract's payoff.
 Example
 In a typical equation you will see a V, representing 'value.'
 What is the coefficient in front of it? If it's r + p where r is a
 risk-free interest rate then the p probably represents a risk of
 default, so you are dealing with some contract that has the
 possibility of default
    """,
    """
     Short answer
 Equilibrium models balance supply and demand, they
 require knowledge of investor preferences and probabilities.
 No-arbitrage models price one instrument by relating it to the
 prices of other instruments.
 Example
 The Vasicek interest rate model can be calibrated to histori
cal data. It can therefore be thought of as a representation of
 an equilibrium model. But it will rarely match traded prices.
 Perhaps it would therefore be a good trading model. The
 BGM model matches market prices each day and therefore
 suggests that there are never any profitable trading opportu
nities
    """,
    """
     Short answer
 The answer has to be 'it depends.' It depends on the
 timescale over which returns are measured. For stocks
 over very short timescales, intraday to several days, the
 distributions are not normal, they have fatter tails and higher
 peaks than normal. Over longer periods they start to look
 more normal, but then over years or decades they look
 lognormal.
 It also depends on what is meant by 'good.' They are very
 good in the sense that they are simple distributions to work
 with, and also, thanks to the Central Limit Theorem,sensible
 distributions to work with since there are sound reasons why
 they might appear. They are also good in that basic stochas
tic calculus and Ito's lemma assume normal distributions and
 those concepts are bricks and mortar to the quant.
 Example
 In Figure 2.14 is the probability density function for the daily
 returns on the S&P index since 1980, scaled to have zero
 mean and standard deviation of 1, and also the standardized
 normal distribution. The empirical peak is higher than the
 normal distribution and the tails are both fatter.
 On 19 October 1987 the SP500 fell 20.5%. What is the proba
bility of a 20% one-day fall in the SP500? Since we are working
 with over 20 years of daily data, we could argue that empiri
cally there will be a 20% one-day fall in the SPX index every
 20 years or so. To get a theoretical estimate, based on nor
mal distributions, we must first estimate the daily standard
 deviation for SPX returns. Over that period it was 0.0106,
 equivalent to an average volatility of 16.9%. What is the prob
ability of a 20% or more fall when the standard deviation is
 0.0106? This is a staggeringly small 1.8 * 10-79. That is just
 once every 2*1076 years. Empirical answer: Once every 20
 years. Theoretical answer: Once every 2 * 1076 years. That's
 how bad the normal-distribution assumption is in the tails.
    """,
    """
     Short answer
 Very robust. You can drop quite a few of the assumptions
 underpinning Black-Scholes and it won't fall over.
 Example
 Transaction costs? Simply adjust volatility. Time-dependent
 volatility? Use root-mean-square-average volatility instead.
 Interest rate derivatives? Black '76 explains how to use the
 Black-Scholes formulæ in situations where it wasn't originally
 intended.
    """,
    """
     Short answer
 The lognormal distribution is often used as a model for the
 distribution of equity or commodity prices, exchange rates
 and indices. The normal distribution is often used to model
 returns.
 Example
 The stochastic differential equation commonly used to repre
sent stocks,
 dS =µSdt+σSdX
 results in a lognormal distribution for S,providedµ and σ
 are not dependent on stock price.
    """,
    """
    Short answer
 Copulas are used to model joint distribution of multiple
 underlyings. They permit a rich 'correlation' structure
 between underlyings. They are used for pricing, for risk
 management, for pairs trading, etc., and are especially
 popular in credit derivatives.
 Example
 You have a basket of stocks which, during normal days,
 exhibit little relationship with each other. We might say that
 they are uncorrelated. But on days when the market moves
 dramatically they all move together. Such behaviour can be
 modelled by copulas
    """,
    """
    Short answer
 Asymptotic analysis is about exploiting a large or small
 parameter in a problem to find simple(r) equations or even
 solutions. You may have a complicated integral that is much
 nicer if you approximate it. Or a partial differential equation
 that can be solved if you can throw away some of the less
 important terms. Sometimes these are called approximate
 solutions. But the word 'approximate' does not carry the
 same technical requirements as 'asymptotic.'
 Example
 The SABR model is a famous model for a forward rate and
 its volatility that exploits low volatility of volatility in order
 for closed-form solutions for option prices to be found. With
out that parameter being small we would have to solve the
 problem numerically.
    """,
    """
    Short answer
 A boundary-value problem is typically a differential equation
 with specified solution on some domain. A free-boundary
 problem is one for which that boundary is also to be found
 as part of the solution. When to exercise an American option
 is an example of a free-boundary problem, the boundary rep
resenting the time and place at which to exercise. This is also
 called an optimal-stopping problem, the 'stopping' here refer
ring to exercise.
 Example
 Allow a box of ice cubes to melt. As they do there will appear
 a boundary between the water and the ice, the free boundary.
 As the ice continues to melt so the amount of water increases
 and the amount of ice decreases.
    """,
    """
    Short answer
 Low-discrepancy sequences are sequences of numbers that
 cover a space without clustering and without gaps, in such a
 way that adding another number to the sequence also avoids
 clustering and gaps. They give the appearance of randomness
 yet are deterministic. They are used for numerically esti
mating integrals, often in high dimensions. The best-known
 sequences are due to Faure, Halton, Hammersley, Niederreiter
 and Sobol'.
 Example
 You have an option that pays off the maximum of 20
 exchange rates on a specified date. You know all the
 volatilities and correlations. How can you find the value of
 this contract? If we assume that each exchange rate follows
 a lognormal random walk, then this problem can be solved
 as a 20-dimensional integral. Such a high-dimensional integral
 must be evaluated by numerical quadrature, and an efficient
 way to do this is to use low-discrepancy sequences.
    """,
    """
     Short answer
 The greeks are sensitivities of values, such as option prices,
 to other financial quantities, such as price. Bastard means
 'illegitimate,' here in the sense that sometimes such a con
cept is not mathematically justified and can give misleading
 information.
 Example
 Suppose you value a barrier option assuming constant volatil
ity, σ, of 20% but are then worried whether that volatility is
 correct. You might measure ∂V
 ∂σ so that you know how sen
sitive the option's value is to volatility and whether or not
 it matters that you have used 20%. Because you are assum
ing volatility to be constant and then are effectively varying
 that constant you are measuring a strange sort of hybrid sen
sitivity which is not the true sensitivity. This could be very
 dangerous
    """,
    """
    Short answer
 Where do I start? Probably the stupidest and most dangerous
 thing is to implicitly (or sometimes even explicitly) assume
 that one can use ideas and results from risk neutrality in situ
ations where it is not valid.
 Example
 Naming no names, I have seen the following written in
 research papers: 'Using risk-neutral pricing we replace µ with
 the risk-free rate r.' Naughty! As explained below you can
 only do this under certain very restrictive assumptions.
    """,
    """
    Short answer
 That inventors/discoverers/creators of models usually don't
 use them. They often use simpler models instead.
    """
]
