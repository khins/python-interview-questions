# Q011 - Group Anagrams

## Key Idea

Group words using a normalized key.

---

## Approaches

### 1. Sorting Key

* key = sorted string
* simple and readable

### 2. Character Count Key

* fixed-size array of 26 letters
* faster, avoids sorting

---

## Complexity

* Time: O(n * k)
* Space: O(n)

---

## Pattern

Use hash map with transformed key

---

## Takeaway

When grouping:

* define a canonical representation
* use it as dictionary key

🧩 The Code
🧠 Key Concept (Important)
We convert each word into a "canonical form" (sorted string)
and use that as a grouping key.
groups = {} -- Create a “groups” dictionary

    Think of this like a set of labeled buckets:

    {
    "aet": ["eat", "tea", "ate"],
    "ant": ["tan", "nat"]
    }
    key = sorted version of a word
    value = list of words that match that pattern
-- 👉 All anagrams produce the same key
for s in strs:  -- Loop through each word
    key = ''.join(sorted(s)) -- Create the key (this is the magic)
    if key not in groups: -- Check if the key exists
        groups[key] = []
    groups[key].append(s)  --Add the word to the group

return list(groups.values())  --Return the result

🧠 Interview-Level Explanation

“I group strings by sorting each one to create a normalized key. All anagrams share the same sorted representation, so I use that as a dictionary key and collect words into lists.”