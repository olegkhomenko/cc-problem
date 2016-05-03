# Coin-changing problem
#
# Problem which is solved in this program is
# a typical Dynamic Programming problem.
# Also can be solved in Recursive way.
#
# Dynamic Programming algorithm complexity: ~ O(Cn).
#
# Non-optimal Recursive algorithm complexity: ~ O(n**2),
# which is not suitable for large 'n'.
#
# NumPy is Required
#
# (c) Oleg Khomenko oleg.khomenko@skolkovotech.ru


class CoinChangingProblemSolver:
    def __init__(self):
        return

    @classmethod
    def initArrayWithNumbers(self, array):
        """Initialize first row and column of array with values = 1"""
        for i in range(array.shape[0]):
            array[i][0] = 1
        for j in range(array.shape[1]):
            array[0][j] = 1
        return array

    # Dynamic Programming
    @classmethod
    def solve_problem_dp(self, N, set_of_coins):
        """
        Solve problem and fill in solution matrix
        (Dynamic Programming)
        """
        array = np.ndarray((len(COINS), N+1), dtype=int)
        array = self.initArrayWithNumbers(array)
        for i in range(array.shape[0] - 1):
            i += 1
            coin = set_of_coins[i]
            for j in range(array.shape[1] - 1):
                j += 1
                if j >= coin:
                    array[i][j] = array[i-1][j] + array[i][j-coin]
                else:
                    array[i][j] = array[i-1][j]
        return array[-1][-1]

    # Recursive
    @classmethod
    def solve_problem_recursive(self, amount, denominations):
        """
        Solve problem and fill in solution matrix
        (Recursive)
        """
        global number_of_variants
        number_of_variants = 0
        arraylist = []
        self.inner_solve_problem_recursive(amount, arraylist, 0, denominations)
        return number_of_variants

    # Inner function for Recursive algorithm
    @classmethod
    def inner_solve_problem_recursive(self, remaining, coins, pos, denominations):
        global number_of_variants
        if remaining == 0:
            # print coins
            number_of_variants = number_of_variants + 1
        else:
            if (remaining >= denominations[pos]):
                coins.append(denominations[pos])
                self.inner_solve_problem_recursive(
                    remaining - denominations[pos],
                    coins,
                    pos,
                    denominations)
                del coins[(len(coins) - 1)]
            if (pos + 1 < len(denominations)):
                self.inner_solve_problem_recursive(
                    remaining,
                    coins,
                    pos + 1,
                    denominations)


if __name__ == "__main__":
    import numpy as np
    import timeit
    COINS = [1, 2, 5, 10]  # Denominations
    Solver = CoinChangingProblemSolver
    print('\nDynamic programming. Timing for 300 RUB:\n')
    print(timeit.timeit(
        "Solver.solve_problem_dp(300, [1, 2, 5, 10])",
        setup="from __main__ import CoinChangingProblemSolver as Solver",
        number=1))
    print('\nRecursive algorithm. Timing for 300 RUB:\n')
    print(timeit.timeit(
        "Solver.solve_problem_recursive(300, [10, 5, 2, 1])",
        setup="from __main__ import CoinChangingProblemSolver as Solver",
        number=1))
    break_flag = False
    while(not break_flag):
        value_to_change = int(input(
            '\nPlease, enter the amount of money you intend to change (larger than 0, less than 30001, -1 to Exit):\n'))
        if (value_to_change > 0 & value_to_change < 30001):
            print(
                "\nThere are %d possible variants to get change"
                % Solver.solve_problem_dp(value_to_change, COINS))
        if (value_to_change == -1):
            break_flag = True
