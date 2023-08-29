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
            "input": ["hello world", "world", "TypeScript"],
            "answer": "hello TypeScript"
        },
        {
            "input": ["hello world world", "world", "TypeScript"],
            "answer": "hello TypeScript TypeScript"
        },
        {
            "input": ["TypeScript is fun", "fun", "awesome"],
            "answer": "TypeScript is awesome"
        },
        {
            "input": ["aaa", "a", "b"],
            "answer": "bbb"
        },
        {
            "input": ["replace all the all", "all", "some"],
            "answer": "replace some the some"
        },
        {
            "input": ["nothing to replace", "something", "nothing"],
            "answer": "nothing to replace"
        },
        {
            "input": ["same same same", "same", "same"],
            "answer": "same same same"
        },
        {
            "input": ["123 123", "123", "321"],
            "answer": "321 321"
        },
        {
            "input": ["OpenAI", "AI", "Source"],
            "answer": "OpenSource"
        },
        {
            "input": ["", "anything", "nothing"],
            "answer": ""
        },
    ],
    "Extra": [
        {
            "input": ["The quick brown fox quick fox quick", "quick", "slow"],
            "answer": "The slow brown fox slow fox slow"
        },
    ]
}
