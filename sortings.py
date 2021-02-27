from typing import Sequence


class Sorter:
    def __init__(self):
        pass

    @staticmethod
    def sort_selection(l: Sequence, reverse: bool = False):  # False means ascending
        """
        Selection sorting: O(n^2)
        """
        l_new = l.copy()
        out = []

        if reverse:
            while l_new:
                out.append(l_new.pop(l_new.index(max(l_new))))
        else:
            while l_new:
                out.append(l_new.pop(l_new.index(min(l_new))))

        return out

    @staticmethod
    def sort_quick(l: Sequence):
        """
        Quick sort: O(nlogn)
        """
        if len(l) < 2:
            return l
        else:
            picked = l.pop(-1)

            left = []
            right = []

            for i in l:
                if i <= picked:
                    left.append(i)
                else:
                    right.append(i)
            return Sorter.sort_quick(left) + [picked] + Sorter.sort_quick(right)

    @staticmethod
    def sort_merge(l: Sequence):
        """
        Merge sorting: O(nlogn)
        """
        if len(l) < 2:
            return l
        elif len(l) == 2:
            return [l[0], l[1]] if l[0] < l[1] else [l[1], l[0]]
        else:
            left = Sorter.sort_merge(l[: len(l) // 2])
            right = Sorter.sort_merge(l[len(l) // 2 :])

            local_list = left + right

            if min(right) > max(left):
                return left + right
            elif min(left) > max(right):
                return right + left
            else:
                for i in range(len(local_list)):
                    min_value = local_list[i]
                    index_min = i

                    for j in range(i + 1, len(local_list)):
                        if local_list[j] < min_value:
                            min_value = local_list[j]
                            index_min = j

                    if i != index_min:
                        local_list[i], local_list[index_min] = (
                            local_list[index_min],
                            local_list[i],
                        )
                return local_list


if __name__ == "__main__":

    s = Sorter()
    print(s.sort_quick([12, 566, 234, 3, 8]))
