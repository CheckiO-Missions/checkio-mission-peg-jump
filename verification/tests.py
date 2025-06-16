"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[
    "--.o.--",
    "--o.o--",
    "....o..",
    "....o..",
    "o.o.o..",
    "--o.o--",
    "--o.o--"]],
            "answer": 2,
        },
        {
            "input": [[
    "--ooo--",
    "--oo.--",
    "ooo.ooo",
    "oo...oo",
    "ooo.ooo",
    "--o.o--",
    "--ooo--"]],
            "answer": 11,
        },
        {
            "input": [[
    "--ooo--",
    "--oo.--",
    "oo.o.oo",
    "o..o..o",
    "oo.o.oo",
    "--oo.--",
    "--ooo--"]],
            "answer": 8,
        },
        {
            "input": [[
    "--ooo--",
    "--o.o--",
    "oo.oooo",
    "o..o..o",
    "oooo.oo",
    "--o.o--",
    "--ooo--"]],
            "answer": 10,
        },
        {
            "input": [[
    "--ooo--",
    "--o.o--",
    "o.ooo.o",
    ".o.o.o.",
    "o.ooo.o",
    "--oo.--",
    "--ooo--"]],
            "answer": 9,
        },
    ],
    "Extra": [
        {
            "input": [[
    "--ooo--",
    "--.oo--",
    ".ooooo.",
    "oo...oo",
    ".ooooo.",
    "--oo.--",
    "--ooo--"]],
            "answer": 12,
        },
        {
            "input": [[
    "--ooo--",
    "--o.o--",
    "o.o.o.o",
    ".o...o.",
    "o.o.o.o",
    "--o.o--",
    "--ooo--"]],
            "answer": 4,
        },
        {
            "input": [[
    "--ooo--",
    "--oo.--",
    "ooo.ooo",
    "o..o..o",
    "ooo.ooo",
    "--.oo--",
    "--ooo--"]],
            "answer": 10,
        },
        {
            "input": [[
    "--ooo--",
    "--ooo--",
    "o.ooo.o",
    ".o...o.",
    "o.ooo.o",
    "--ooo--",
    "--ooo--"]],
            "answer": 10,
        },
        {
            "input": [[
    "--ooo--",
    "--.oo--",
    "oo.oo.o",
    "o..o..o",
    "o.oo.oo",
    "--oo.--",
    "--ooo--"]],
            "answer": 10,
        },
        {
            "input": [[
    "--ooo--",
    "--o.o--",
    "o.o.ooo",
    "..o.o..",
    "ooo.o.o",
    "--o.o--",
    "--ooo--"]],
            "answer": 2,
        },
        {
            "input": [[
    "--ooo--",
    "--.oo--",
    ".ooooo.",
    ".o...o.",
    ".ooooo.",
    "--oo.--",
    "--ooo--"]],
            "answer": 10,
        },
        {
            "input": [[
    "--ooo--",
    "--ooo--",
    "ooooooo",
    "o.....o",
    "ooooooo",
    "--ooo--",
    "--ooo--"]],
            "answer": 6,
        },
        {
            "input": [[
    "--ooo--",
    "--ooo--",
    "ooo.ooo",
    "..o.o..",
    "ooo.ooo",
    "--ooo--",
    "--ooo--"]],
            "answer": 6,
        },
        {
            "input": [[
    "--ooo--",
    "--oo.--",
    "oo.oo.o",
    "o..o..o",
    "o.oo.oo",
    "--o.o--",
    "--ooo--"]],
            "answer": 11,
        },
        {
            "input": [[
    "--ooo--",
    "--.oo--",
    "o.ooooo",
    ".o...o.",
    "ooooo.o",
    "--oo.--",
    "--ooo--"]],
            "answer": 10,
        },
    ]
}
