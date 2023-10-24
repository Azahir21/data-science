import math
from typing import Literal


class Bernoulli:
    """A Bernoulli random variable (also called a **boolean** or **indicator**
    random variable) can take on two values, 1 and 0. It takes on a 1 if an 
    experiment with probability _p_ resulted in success and a 0 otherwise.

    Some example uses include a coin flip, a random binary digit, whether a 
    disk drive crashed, and whether someone likes a Netflix movie. 

    Bernoulli distribution is parameterized by only one variables:
     - _p_: probability of success of a single event

    Ref: https://chrispiech.github.io/probabilityForComputerScientists/en/part2/bernoulli/
    """

    def __init__(self, p: float):
        """_p_ is the probability that random variable **X** is equal to 1.
        """
        assert 0 < p < 1, "`p` must be in [0, 1]"
        self.p = p

        self.support  = set([0, 1])
        self.mean = p
        self.variance = self.p * (1 - self.p)

    def pmf(self, x: int) -> float:
        """Probability mass function of Bernoulli distribution implemented
        in smooth definition.

        Effectively, it converts to discrete cases of X={0, 1} since X can only
         take these two values.
         - P(X=1) = _p_
         - P(X=0) = 1 - _p_
        """
        return (self.p ** x) * (1 - self.p) ** (1 - x)

    def proba(self, x: Literal[0, 1]) -> float:
        """Returns the probability of random variable **X** being equal to _x_,
          i.e. P(X=x)
        """
        if x not in self.support:
            raise ValueError(f"Bernoulli distribution can only take values in {self.support}")

        return self.pmf(x)


class Binomial:
    """A binomial distribution is the sum of independent and identically 
    distributed **Bernoulli** random variables.

    The binomial distribution is a probability distribution that describes the
    number of successes (_k_) in a fixed number of independent trials (_n_), 
    each with the same probability of success (_p_). 

    Example scenarios:
     - # heads in _n_ coint flips
     - # of 1's in randomly generated length _n_ bit string
     - # of disk drives crashed in 1000 computer cluster, assuming disks crash 
     independently

    Binomial distribution is parameterized by two variables:
     - _p_: probability of success of a single trial
     - _n_: number of trials

    Ref: 
     - https://chrispiech.github.io/probabilityForComputerScientists/en/part2/binomial/
     - Visualize: https://shiny.rit.albany.edu/stat/binomial/
    """

    def __init__(self, p: float, n: int):
        assert 0 < p < 1, "`p` must be in [0, 1]"
        self.p = p

        assert (n % 1 == 0) & (n > 0), "`n` must be a natural number, i.e. {1, 2, 3, ...}"
        self.num_trials = n

        self.support = list(range(1, self.num_trials + 1))

        self.mean = self.num_trials * self.p
        self.variance = self.num_trials * self.p * (1 - self.p)  # https://proofwiki.org/wiki/Variance_of_Binomial_Distribution

    def pmf(self, x: int) -> float:
        return (
            math.comb(self.num_trials, x) 
            * (self.p ** x) 
            * ((1 - self.p) ** (self.num_trials - x))
            )

    def proba(self, x: int) -> float:
        """Returns probability of _x_ successes in _n_ trials."""
        if x not in self.support:
            raise ValueError(f"Invalid input, number of successes can only be "
                             f"less than or equal to {self.num_trials}")
        return self.pmf(x)


if __name__ == "__main__":
    # d = Bernoulli(p=0.75)
    # print(d.proba(1))
    # print(d.proba(0))
    # print(d.proba(0.5))

    d = Binomial(0.6, 5)
    print(d.proba(2))

