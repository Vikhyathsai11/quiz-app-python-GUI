import tkinter as tk
from tkinter import *
class QuizApp(tk.Tk):
    def __init__(self, questions):
        super().__init__()
        self.title("Quiz App")
        self.questions = questions
        self.current_question = 0
        self.score = 0


        self.question_label = tk.Label(self, text="", width=50)
        self.question_label.pack(pady=10)

        self.radio_var = tk.IntVar()
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self, text="", variable=self.radio_var, value=i)
            self.radio_buttons.append(rb)
            rb.pack()

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=10)

        self.score_label = tk.Label(self, text="Score: 0")
        self.score_label.pack()

        self.next_question()

    def next_question(self):
        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question]["question"])
            for i, rb in enumerate(self.radio_buttons):
                rb.config(text=self.questions[self.current_question]["choices"][i])
                # self.current_question=change(i)
            self.radio_var.set(-1)
        else:
            # self.Pack.delete('all')
            self.question_label.config(text="Quiz Completed!")
            self.submit_button.config(state=tk.DISABLED)

    def submit_answer(self):
        selected_choice = self.radio_var.get()
        if selected_choice == self.questions[self.current_question]["answer"]:
            self.score += 1
        self.current_question += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.next_question()

#writing questions edo
questions = [
    {
        "question": "What is the capital of India?",
        "choices": ["Chennai", "Delhi", "Mumbai", "Hyderabad"],
        "answer": 1
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Mars", "Jupiter", "Venus", "Mercury"],
        "answer": 0
    },
    {
        "question": "What is the largest ocean in the world?",
        "choices": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": 3
    }
]


quiz_app = QuizApp(questions)
quiz_app.mainloop()
