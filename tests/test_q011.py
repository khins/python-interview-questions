from questions.q011_group_anagrams import group_anagrams


def test_basic():
    result = group_anagrams(["eat","tea","tan","ate","nat","bat"])
    sorted_result = [sorted(group) for group in result]
    expected = [["ate","eat","tea"], ["nat","tan"], ["bat"]]
    assert sorted(sorted_result) == sorted(expected)


def test_single():
    assert group_anagrams(["a"]) == [["a"]]


def test_empty():
    assert group_anagrams([]) == []