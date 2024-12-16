import tkinter as tk
from tkinter import messagebox

# Load questions
questions = [
    {
        "question": "What is the output of 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": 2  # Index of the correct option
    },
    {
        "question": "Which programming language is used for AI and ML?",
        "options": ["Java", "Python", "C++", "Ruby"],
        "answer": 2
    },
    {
        "question": "What does HTML stand for?",
        "options": ["Hyper Trainer Marking Language", "Hyper Text Markup Language", "Hyperlinks Text Mark Language", "None of the above"],
        "answer": 2
    },
    {
        "question": "Which data structure uses FIFO order?",
        "options": ["Stack", "Queue", "Array", "Linked List"],
        "answer": 2
    },
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": 3
    },
    {
        "question": "What does CPU stand for?",
        "options": ["Central Processing Unit", "Central Programming Unit", "Control Processing Unit", "Control Programming Unit"],
        "answer": 1
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": 2
    },
    {
        "question": "Which is the smallest prime number?",
        "options": ["1", "2", "3", "0"],
        "answer": 2
    },
    {
        "question": "What is the speed of light?",
        "options": ["3 x 10^8 m/s", "5 x 10^8 m/s", "1 x 10^6 m/s", "None of these"],
        "answer": 1
    },
    {
        "question": "Which programming language is used for web development?",
        "options": ["Python", "HTML", "C++", "Java"],
        "answer": 2
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz")
        self.current_question_index = 0
        self.score = 0
        self.timer = 15

        # Create Canvas
        self.canvas = tk.Canvas(root, width=500, height=400)
        self.canvas.pack()

        # Create UI elements on the canvas
        self.question_text = self.canvas.create_text(
            250, 50, text="", font=("Arial", 14), width=400, justify="center"
        )

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Arial", 12), command=lambda idx=i: self.check_answer(idx))
            self.option_buttons.append(button)

        # Place buttons dynamically on the canvas
        self.button_windows = [
            self.canvas.create_window(250, 120 + i * 50, window=self.option_buttons[i], width=400, height=30)
            for i in range(4)
        ]

        self.timer_label = tk.Label(root, text="Time left: 15s", font=("Arial", 12), fg="blue")
        self.canvas.create_window(250, 280, window=self.timer_label)

        self.result_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
        self.canvas.create_window(250, 320, window=self.result_label)

        # Directly start the timer by calling the update_timer method
        self.update_timer()

        # Load the first question
        self.load_question()

    def load_question(self):
        self.timer = 15
        question = questions[self.current_question_index]
        self.canvas.itemconfig(self.question_text, text=question['question'])

        for i, option in enumerate(question['options']):
            self.option_buttons[i].config(text=option, state=tk.NORMAL)

        self.result_label.config(text="")
        self.update_timer()

    def check_answer(self, selected_option):
        question = questions[self.current_question_index]
        correct_index = question['answer'] - 1

        if selected_option == correct_index:
            self.score += self.timer  # Faster answers earn more points

        for button in self.option_buttons:
            button.config(state=tk.DISABLED)

        self.root.after(2000, self.next_question)  # Auto move to next question after 2 seconds

    def next_question(self):
        self.current_question_index += 1

        if self.current_question_index < len(questions):
            self.load_question()
        else:
            messagebox.showinfo("Quiz Over", f"You scored {self.score} points out of {len(questions) * 15}.")
            self.root.quit()

    def update_timer(self):
        if self.timer > 0:
            self.timer -= 1
            self.timer_label.config(text=f"Time left: {self.timer}s")
            self.root.after(1000, self.update_timer)
        else:
            self.next_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
