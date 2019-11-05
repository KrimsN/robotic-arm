import argparse
from functools import reduce


def make_parser():
    ret = argparse.ArgumentParser(
        description='Launch the solver with arguments specified')
    ret.add_argument('task', help='task filename')
    ret.add_argument('csv', help='csv stats filename')
    ret.add_argument('seq', help='q sequence filename')
    ret.add_argument('-a', '--alpha',
                     help='pheromone attractiveness modifier',
                     type=float, default=1.0)
    ret.add_argument('-b', '--beta',
                     help='weight attractiveness modifier',
                     type=float, default=1.0)
    ret.add_argument('-g', '--gamma',
                     help='angle attractiveness modifier',
                     type=float, default=0.0)
    ret.add_argument('-p', '--phi',
                     help='base pheromone level',
                     type=float, default=0.1)
    ret.add_argument('-d', '--decay',
                     help='pheromone decay rate',
                     type=float, default=0.01)
    ret.add_argument('-q', '--ant-power',
                     help='amount of pheromone an ant distributes',
                     type=float, default=1.0)
    ret.add_argument('-k', '--ant-num',
                     help='number of ants',
                     type=int, default=1)
    ret.add_argument('-i', '--iters',
                     help='number of algorithm iterations',
                     type=int, default=1)
    return ret


def check_args(args):
    tests = [args.alpha >= 0.0,
             args.beta >= 0.0,
             args.gamma >= 0.0,
             args.phi > 0.0,
             args.decay > 0.0 and args.decay < 1.0,
             args.ant_power > 0.0,
             args.ant_num > 0,
             args.iters > 0, ]

    return reduce(lambda x, y: x and y, tests, True)
