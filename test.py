from scipy.stats import chisquare
import numpy as np

# Example observed frequencies
observed_values = [10, 5, 7, 2, 2]
total_obs = np.sum(observed_values)
expected_proportions = np.ones_like(observed_values) / len(observed_values)
exp = expected_proportions * total_obs
# Performing the chi-square test
chi2_stat, p_value = chisquare(f_obs=observed_values, f_exp=exp)

# Displaying the results
print("Chi-square Statistic:", chi2_stat)
print("P-value:", p_value)
