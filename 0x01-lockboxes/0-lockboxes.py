#!/usr/bin/python3
"""Module that defines canUnlockAll function to check lockboxes."""


def canUnlockAll(boxes):
    """Determines if all boxes can be opened."""
    n = len(boxes)
    unlocked = set([0])  # Start with the first box unlocked
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key < n and key not in unlocked:
            unlocked.add(key)
            keys.update(boxes[key])

    return len(unlocked) == n
