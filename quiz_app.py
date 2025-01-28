import tkinter as tk
from tkinter import messagebox

# Define the quiz questions
questions = [
    {
        "topic": "Loops",
        "question": "What will be the output of this Python code?",
        "code": "for i in range(3):\n    print(i)",
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"],
        "answer": 0  # Index of the correct option in the options list
    },
    {
        "topic": "Strings",
        "question": "What does the len() function return?",
        "code": "len('Python')",
        "options": ["6", "7", "5", "Error"],
        "answer": 0
    },
    {  
        "topic": "Conditionals",
        "question": "What is the output of the following code?",
        "code": "x = 10\ny = 20\nif x > y:\n    print('x is greater')\nelse:\n    print('y is greater')",
        "options": ["x is greater", "y is greater", "Error", "None"],
        "answer": 1
    },
    {
        "topic": "Functions",
        "question": "What will be the output of this Python code?",
        "code": "def add(a, b):\n    return a + b\nresult = add(5, 3)\nprint(result)",
        "options": ["8", "5", "Error", "None"],
        "answer": 0
    },
    {
        "topic": "Dictionaries",
        "question": "What does the following code return?",
        "code": "d = {'a': 1, 'b': 2}\nprint(d.get('c', 3))",
        "options": ["None", "KeyError", "3", "Error"],
        "answer": 2
    },
    {
        "topic": "Error Handling",
        "question": "Which keyword is used to handle exceptions in Python?",
        "code": "",
        "options": ["try", "catch", "except", "finally"],
        "answer": 2
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz Generator")
        self.root.geometry("500x500")

        self.selected_question = None
        self.selected_answer = tk.IntVar()

        # GUI components
        self.create_widgets()

    def create_widgets(self):
         # Title
        self.title_label = tk.Label(
            self.root,
            text="Python Quiz Generator",
            font=("Arial", 20, "bold"),
            bg="blueviolet",
            fg="#edf2f4",
        )
        self.title_label.pack(pady=10)

        # Input Field for Topic
        self.topic_label = tk.Label(self.root, text="Enter Python Topic:", font=("Arial", 12))
        self.topic_label.pack(pady=10)

        self.topic_entry = tk.Entry(self.root, font=("Arial", 12))
        self.topic_entry.pack(pady=5)

        self.generate_button = tk.Button(
            self.root, text="Generate Python Question", command=self.generate_question, font=("Arial", 12)
        )
        self.generate_button.pack(pady=10)

        # Question Display Area
        self.question_frame = tk.Frame(self.root)
        self.question_frame.pack(pady=10)

        self.topic_display = tk.Label(self.question_frame, text="", font=("Arial", 14, "bold"), wraplength=400)
        self.topic_display.pack(pady=5)

        self.question_display = tk.Label(self.question_frame, text="", font=("Arial", 12), wraplength=400)
        self.question_display.pack(pady=5)

        self.code_display = tk.Label(self.question_frame, text="", font=("Courier", 12), wraplength=400, fg="blue")
        self.code_display.pack(pady=5)

        self.options_frame = tk.Frame(self.question_frame)
        self.options_frame.pack(pady=10)

        # Submit Button
        self.submit_button = tk.Button(
            self.root, text="Submit", command=self.check_answer, font=("Arial", 12)
        )
        self.submit_button.pack(pady=10)

        # Feedback Area
        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 12, "italic"))
        self.feedback_label.pack(pady=10)

    def generate_question(self):
        topic = self.topic_entry.get().strip().capitalize()
        if not topic:
            messagebox.showwarning("Warning", "Please enter a topic!")
            return

        # Filter questions by topic
        matching_questions = [q for q in questions if q["topic"] == topic]
        if not matching_questions:
            messagebox.showinfo("No Questions Found", f"No questions available for the topic '{topic}'.")
            return

        # Select the first question (or random if desired)
        self.selected_question = matching_questions[0]
        self.selected_answer.set(-1)  # Reset the selected answer

        # Update the GUI with the question details
        self.topic_display.config(text=f"Topic: {self.selected_question['topic']}")
        self.question_display.config(text=self.selected_question["question"])
        self.code_display.config(text=self.selected_question.get("code", ""))

        # Clear previous options
        for widget in self.options_frame.winfo_children():
            widget.destroy()

        # Display new options
        for i, option in enumerate(self.selected_question["options"]):
            tk.Radiobutton(
                self.options_frame, text=option, variable=self.selected_answer, value=i, font=("Arial", 12)
            ).pack(anchor="w")

        self.feedback_label.config(text="")  # Clear feedback

    def check_answer(self):
        if not self.selected_question:
            messagebox.showwarning("Warning", "Generate a question first!")
            return

        selected_index = self.selected_answer.get()
        if selected_index == -1:
            messagebox.showwarning("Warning", "Please select an answer!")
            return

        correct_index = self.selected_question["answer"]
        if selected_index == correct_index:
            self.feedback_label.config(text="Correct! Well done!", fg="green")
        else:
            self.feedback_label.config(text="Incorrect. Try again.", fg="red")


# Create the app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

