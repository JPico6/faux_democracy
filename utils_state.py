import scipy.stats as stats


def val_from_normal_dist(
        modifier=1,
        mu=None,
        sigma=None
):

    # generates a value from a normal distribution
    # modifier alters the mean, default to 1 (no modification)

    # range
    a, b = 1, 100
    # mean, sd
    if not mu:
        mu = 50*modifier
    if not sigma:
        sigma = 25

    dist = stats.truncnorm((a - mu) / sigma, (b - mu) / sigma, loc=mu, scale=sigma)

    value = dist.rvs(1)
    return int(value)


def modify_dist_mean(
        val,
        inv=False
):

    # pass in the value to modify
    # in some cases we want to inverse the modifier
    if inv:
        val = 100-val
    modifier = (100 - val) * 0.01 * 2

    return modifier


def check_bounds(
        key,
        val
):

    # ensure values stay in bounds (1-100)
    if key != 'pop':
        if val > 100:
            val = 100
        elif val < 1:
            val = 1
    return int(val)

