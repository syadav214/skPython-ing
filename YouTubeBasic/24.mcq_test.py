from simple_mcq_question import Question

question_prompts = [
    "What color are apples?\n(a) Red\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'c'),
    Question(question_prompts[2], 'b')
]


def run_test(questions):
    score = 0
    for q in questions:
        annswer = input(q.prompt)
        if annswer == q.answer:
            score += 1
    print("You got "+str(score)+"/"+str(len(questions)))


run_test(questions)
