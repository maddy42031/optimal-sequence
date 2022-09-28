# I'm Ma👽dy.

# Optimal Sequence Problem.

# Below table is example question.

#   +------------------------------------------------+
#   |  MACHINE   |  1  |  2  |  3  |  4  |  5  |  6  |
#   |------------------------------------------------+
#   |  MACHINE1  |  5  |  7  |  2  |  6  |  3  |  4  |
#   |------------------------------------------------+
#   |  MACHINE2  | 2  |  5  |  4  |  9  |  1  |   3  |
#   +------------------------------------------------+


#  To find the optimal sequence for the above example.
#  The output :
#   +-----------------------------------------------+
#   |   3   |   4   |   2   |   6   |   1   |   5   |
#   +-----------------------------------------------+


machine = {    # Quetion of this program
    1: [5, 2],
    2: [7, 5],
    3: [2, 4],
    4: [6, 9],
    5: [3, 1],
    6: [4, 3]
}


def check_2_Arr(ma, mb):
    a = [ma, mb]
    b = [c for i in a for c in i]  # parameter (arr) comes 2d array
    v = min(b)

    for i in b:
        if i == v:
            continue
        g = [i, v] if [i, v] in a else [v, i]
        if g in a:
            return [a[a.index(g)], a[a.index(g)-1]]


def arrange_os(arr):
    arranged = []
    arr[1].reverse()
    for i in arr[0]:
        arranged.append(i)
    for i in arr[1]:
        arranged.append(i)
    print(arranged)


def optimal_sequence():
    optimal_sequence = [machine[item] for item in machine.keys()]
    sm, gr = [], []
    a = [item for item in optimal_sequence]
    while len(a) != 0:
        if len(a) == 1:
            minimum_in_arr = a[0].index(min(a[0]))
            m_i = optimal_sequence.index(a[0])+1
            if minimum_in_arr == 0:
                sm.append(m_i)
            else:
                gr.append(m_i)
            break
        else:
            min_A = min(a)
            a.remove(min_A)
            min_B = min(a)
            a.remove(min_B)

            mini = check_2_Arr(min_A, min_B)
            minimum_in_arr = mini[0].index(min(mini[0]))
            m_i = optimal_sequence.index(mini[0])+1
            if minimum_in_arr == 0:
                sm.append(m_i)
            else:
                gr.append(m_i)
            a.append(mini[1])

    return [sm, gr]


if __name__ == "__main__":
    catch = optimal_sequence()
    arrange_os(catch)

# Happy Hacking #
