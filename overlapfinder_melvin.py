from datetime import datetime as dt
from intervaltree import Interval, IntervalTree
#import test_inputs

# one interval
tc_0 = [Interval(1, 3, "aaron")]

# no overlap
tc_1 = [Interval(1, 2, "aaron"), Interval(3, 4, "ben"), Interval(5, 6, "charlotte")]

# separate overlaps
tc_2 = [Interval(1, 3, "aaron"), Interval(2, 4, "ben"),  Interval(3, 5, "charlotte")]

# shared overlap
tc_3 = [Interval(1, 3, "aaron"), Interval(2, 4, "ben"), Interval(2, 5, "charlotte")]

# 4 intervals
tc_4 = [Interval(1, 3, "aaron"), Interval(2, 4, "ben"),
        Interval(3, 5, "charlotte"), Interval(1, 6, "dan")]



# Input: An list of Intervals
# Output: A dictionary (key: overlap, value: set of user_ids which share the overlap)
def find_all_common_intervals(interval_list):
    overlap_dict = dict()
    interval_tree = IntervalTree(interval_list)
    for interval in interval_tree.items(): # create a copy of the tree to iterate over
        other_intervals_that_overlap = find_other_intervals_which_overlap(interval_tree, interval)
        for other_interval in other_intervals_that_overlap:
            add_overlap_to_dict(interval, other_interval, overlap_dict)
    return overlap_dict


# Input: An IntervalTree and an Interval in the IntervalTree
# Output: A set containing all other Intervals in the IntervalTree that intersect with the given
#  Interval
def find_other_intervals_which_overlap(tree, interval):
    tree.remove(interval)
    result = tree.search(interval.begin, interval.end) # returns a set
    return result

# Input: Two intervals and a dictionary (key: tuple)
# Output: None
def add_overlap_to_dict(interval_a, interval_b, dict):
    overlap = find_overlap(interval_a.begin, interval_a.end, interval_b.begin, interval_b.end)
    # if it is already recorded that other existing intervals already overlap over this exact
    # period, add intervals a and b to the set of existing intervals
    if overlap in dict:
        existing_intervals_that_overlap = dict[overlap]
        existing_intervals_that_overlap |= {interval_a.data, interval_b.data}
        dict[overlap] = existing_intervals_that_overlap
    else:
        dict[overlap] = {interval_a.data, interval_b.data}


# Pre-condition: all arguments are integers, a and b are comparable
def find_overlap(a1, a2, b1, b2):
    a_begin = min(a1, a2)
    a_end = max(a1, a2)
    b_begin = min(b1, b2)
    b_end = max(b1, b2)

    if b_end < a_begin or a_end < b_begin:
        return None
    common_begin = max(a_begin, b_begin)
    common_end = min(a_end, b_end)
    return common_begin, common_end


def print_common_intervals(tup_set_dict):
    print("available common datetime intervals:\n")
    # tup is the tuple representing the common interval, userid_set is set of the user data
    for tup, userid_set in tup_set_dict.items():
        print(tup[0].strftime('%Y-%b-%d %H%M') + " - " + tup[1].strftime('%Y-%b-%d %H%M') + ": ")
        print("\tuserids: " + str(userid_set))
    print()