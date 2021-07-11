#!/usr/bin/env python
# coding: utf-8

WAYS = 0
def count_ways(day, number_of_leaves):
    global WAYS
    if day > TOTAL_DAYS:
        # If day visited is more than total days then we are considering extra leaves hence this condition is ignored
        return
    if day == TOTAL_DAYS:
        # If day matches total days then we have found one way to attend college
        WAYS += 1
    elif number_of_leaves == 0:
        # If 0 leaves has been taken previously then we are allowed to take another 0 or 1 or 2 or 3 leaves
        count_ways(day + 1, 0)
        count_ways(day + 1, 1)
        count_ways(day + 2, 2)
        count_ways(day + 3, 3)
    elif number_of_leaves == 1:
        # If 1 leave has been taken on previous day then we are allowed to take more 0 or 1 or 2 leave.
        # We will not consider 3 leaves in this since it will make total leave of 4
        count_ways(day + 1, 0)
        count_ways(day + 1, 1)
        count_ways(day + 2, 2)
    elif number_of_leaves == 2:
        # If 2 leave has been taken on previous day then we are allowed to take more 0 or 1 leave.
        # We will not consider 2 and 3 leaves in this since it will make total leave more than 4
        count_ways(day + 1, 0)
        count_ways(day + 1, 1)
    elif number_of_leaves == 3:
        # If 3 leaves has been taken on previous day then we are not allowed to take any more leave,
        # since it will make total consecutive leave more than 4
        count_ways(day + 1, 0)


TOTAL_DAYS = int(input("Enter total days: "))

# Start college with 0 leaves
count_ways(1, 0)

# Reverse of this will be end the college with 0 leaves or attanding college on end day
num_of_ways_to_attend_college_on_end_day = WAYS


# Start college with 1 leave
count_ways(1, 1)
# Start college with 2 leaves
count_ways(2, 2)
# Start college with 3 leaves
count_ways(3, 3)

total_ways_to_attend_college = WAYS

num_of_ways_to_miss_collge_on_end_day = (
    total_ways_to_attend_college - num_of_ways_to_attend_college_on_end_day
)

print("Total ways to attend college", total_ways_to_attend_college)

print(
    "Probability of missing college on end day: ",
    str(num_of_ways_to_miss_collge_on_end_day)
    + "/"
    + str(total_ways_to_attend_college),
)
