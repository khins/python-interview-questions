🧠 What This Teaches
Control flow matters (ordering bugs are common)
Writing flexible code > hardcoding

Interviewers often push:

“What if rules change?”


def fizzbuzz(n: int) -> list[str]:
    result = []

    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    return result

🔍 Key Concepts
range(1, n + 1) → inclusive loop
% (modulo) → checks divisibility
i % 15 == 0 → means divisible by both 3 and 5
⚠️ Critical Detail

Order matters:

If you check 3 or 5 first → you never reach 15
That’s why 15 must come first

🧠 How to Explain in Interview

“I iterate from 1 to n, check divisibility using modulo, and prioritize the combined case first to avoid logical conflicts.”

✅ Approach 2: Cleaner Concatenation
def fizzbuzz_clean(n: int) -> list[str]:
    result = []

    for i in range(1, n + 1):
        output = ""

        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"

        result.append(output if output else str(i))

    return result

🔍 Key Concepts
No elif → all conditions evaluated
Build string dynamically
"Fizz" + "Buzz" happens naturally
💡 Why This Is Better
No need for special 15 check
More extensible
Cleaner mental model

🧠 How to Explain in Interview

“Instead of handling edge cases separately, I build the result string incrementally. If no conditions match, I fall back to the number.”

🔥 Approach 3: Dynamic Rules (Best Version)
def fizzbuzz_advanced(n: int, rules: dict[int, str]) -> list[str]:
    result = []

    for i in range(1, n + 1):
        output = ""

        for divisor, word in rules.items():
            if i % divisor == 0:
                output += word

        result.append(output if output else str(i))

    return result

🔍 Key Concepts

Uses a dictionary:

{3: "Fizz", 5: "Buzz"}
Iterates through rules dynamically
No hardcoding at all

🧠 How to Explain in Interview

“I abstracted the divisibility rules into a dictionary so the function is reusable and scalable. This removes hardcoding and makes it adaptable to new requirements.”