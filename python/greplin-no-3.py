# challenge.greplin.com


def powerset(xs):
    if not xs:
        return [[]]

    y, ys = xs[0], xs[1:]
    yss = powerset(ys)
    yss.extend([[y] + zs for zs in yss])
    return yss


def is_sum_thing(xs):
    if not xs:
        return False

    m = max(xs)
    if sum(xs) - m == m:
        return True


if __name__ == '__main__':
    xss = powerset([1, 2, 3, 4, 6])  # example set
    xss = powerset([3, 4, 9, 14, 15, 19, 28, 37, 47, 50, 54, 56, 59, 61,
                    70, 73, 78, 81, 92, 95, 97, 99])

    candidates = filter(is_sum_thing, xss)

    print candidates
    print len(candidates)
