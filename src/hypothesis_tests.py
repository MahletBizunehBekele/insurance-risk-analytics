from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency


def run_ttest(group_a, group_b):

    group_a = group_a.dropna()
    group_b = group_b.dropna()

    stat, p_value = ttest_ind(
        group_a,
        group_b,
        nan_policy="omit"
    )

    return {
        "test": "Independent t-test",
        "p_value": p_value
    }


def run_chi2(contingency_table):

    stat, p_value, dof, expected = chi2_contingency(
        contingency_table
    )

    return {
        "test": "Chi-squared",
        "p_value": p_value
    }