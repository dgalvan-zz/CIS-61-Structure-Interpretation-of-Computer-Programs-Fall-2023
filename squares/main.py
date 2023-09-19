# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def merge_interval_i(intervals):
    i = 0
    j = 0
    if (intervals[i][j + 1]) >= (intervals[i + 1][j]):
        return [[intervals[i][j], intervals[i + 1][j + 1]]]
    else:
        return intervals


interval = [[1, 2], [3, 4]]
return_value = merge_interval_i(interval)
print(return_value)
