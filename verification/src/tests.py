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
            "input": "... --- -- .   - . -..- -",
            "answer": "Some text"
        },
        {
            "input": "..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----",
            "answer":"I was born in 1990" 
        }
    ],
    "Extra": [
        {
            "input": ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..",
            "answer": "Abcdefghijklmnopqrstuvwxyz"
        },
        {
            "input": "----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.   .- .-. .   -.. .. --. .. - ...",
            "answer": "0123456789 are digits"
        },
	{
            "input": "...- ...-- .-. -.--   .---- ----- -. --.   ... - .-. .---- -. --.   .-- .---- - ....   ... ----- -- ...--   -. ..- -- -... ...-- .-. .....",
            "answer": "V3ry 10ng str1ng w1th s0m3 numb3r5"
        }
    ]
}
