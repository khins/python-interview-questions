# q011_group_anagrams.py

def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Group strings that are anagrams.

    Args:
        strs (list[str]): list of input strings

    Returns:
        list[list[str]]: grouped anagrams
    """
    # 💡 Hint

    # Use a dictionary:

    #  {}
    groups = {}
    for s in strs:
        # Sort the string to get the key
        key = ''.join(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)

    return list(groups.values())


if __name__ == "__main__":
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))