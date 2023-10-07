"""
Project

    When two blocks of the same "type" are adjacent to each other, the entire contiguous block disappears (pops off). If this occurs, this can allow previously separated blocks to be in contact with each other, setting off a chain reaction. This will continue until each block is surrounded by a different block.

Examples

    ["A", "B", "C", "C", "B", "D", "A"]
    # The two adjacent Cs pop off

    ["A", "B", "B", "D", "A"]
    # Two adjacent Bs pop off

    ["A", "D", "A"]
    # No more blocks can be popped off

    ------------------------------------------
    
    ["A", "B", "A", "A", "A", "B", "B"]
    # The three adjacent As will pop off
    # (before the two adjacent Bs)

    ["A", "B", "B", "B"]
    # 3 adjacent Bs pop off

    ["A"]
    # Final result

    ------------------------------------------

    final_result(["B", "B", "A", "C", "A", "A", "C"]) ➞ ["A"]

    final_result(["B", "B", "C", "C", "A", "A", "A"]) ➞ []

    final_result(["C", "A", "C"]) ➞ ["C", "A", "C"]

Notes

    - If the first round has multiple poppable blocks, pop starting from the left.

    LINK: https://edabit.com/challenge/v3iQ4XiW385SrkWKo

Thoughts

    - 2 or more blocks adjacent will pop all connected blocks (see example 2)
    - I could iterate through the list comparing the block on the right.
        - if the block to the right is equal to current block. A pop occurs
            - need to check immediate right of the two popping blocks; due to linearlly iterating from left to right, I should never have a block on the left that is equal.
        - after a pop I need to compare current block with previous block, in case the pop made it such that new adjacent blocks are now equal
            - might be easier to decrement index (if possible) and do the same check as before

"""

def final_result(lst):
    i = 0
    popBlocks = 2
    while(i < len(lst) - 1):
        if(lst[i] == lst[i + 1]): # if current block equal to block on the right
            j = i + 2
            try: # check immediate right, may be out of bounds
                while(lst[i] == lst[j]):
                    popBlocks += 1
                    j += 1
            except: # ignore index out of bounds
                None
            for n in range(popBlocks): # remove all equal adjacent blocks
                lst.pop(i)
            popBlocks = 2

            # after a successful pop the current block could potentially be equal to previous block. I will decrement index (if possible) to double check
            if(i != 0):
                i -= 1
        else:
            i += 1
    return(lst)


# complete and tested Aug. 7, 2023. See test_poppingBlocks.py for test cases.