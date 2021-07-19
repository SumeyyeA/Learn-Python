from Question import Question
question_prompts=[
    "What calor are apple?\na)Red\nb)Orange\nc)Yellow\n\n",
    "What calor are banana?\na)Red\nb)Orange\nc)Yellow\n\n",
    "What calor are orange?\na)Red\nb)Orange\nc)Yellow\n\n"
]
questions=[
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"b")
]
def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score+=1
    print("You got"+str(score)+"/"+str(len(questions))+"Correct")
print(run_test(questions))
