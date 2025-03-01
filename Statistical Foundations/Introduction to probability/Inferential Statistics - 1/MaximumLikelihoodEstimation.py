"""
<h2><u>Statistical Foundations</u></h2>

# Module 5: Inferential Statistics-1
<h2> Demo 2: Maximum Likelihood Estimation </h2>

"""

#Import the required library
import pandas as pd
import numpy as np

### Let’s say our sample is 3, what is the probability that it comes from a distribution of μ = 3 and σ = 1?

from scipy.stats import norm
print(norm.pdf(3,3,1))

### What if it came from a distribution with μ = 7 and σ = 2?

print(norm.pdf(3,7,2))

### The probability that samples 2 and 6 are drawn from a distribution with μ = 4 and σ = 1?

print(norm.pdf(2, 4, 1)*norm.pdf(6, 4, 1))
