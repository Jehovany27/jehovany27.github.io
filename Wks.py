import tkinter as tk
from tkinter import messagebox

class WorldKnowledgeShareGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("World Knowledge Share")
        self.root.geometry("400x300")

        # Title label
        self.title_label = tk.Label(root, text="World Knowledge Share", font=("Helvetica", 20))
        self.title_label.pack(pady=20)

        # Logged-in user label
        self.logged_in_user_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.logged_in_user_label.pack(pady=10)

        # View Knowledge button
        self.view_knowledge_button = tk.Button(root, text="View Knowledge", command=self.view_knowledge)
        self.view_knowledge_button.pack()

        # Contribute Knowledge button
        self.contribute_knowledge_button = tk.Button(root, text="Contribute Knowledge", command=self.contribute_knowledge)
        self.contribute_knowledge_button.pack()

        # Placeholder for knowledge shares (you can replace this with actual data)
        self.knowledge_shares = [
            "Article 1: How to Learn Python",
            "Article 2: Introduction to Web Development",
            # Add more knowledge shares here
        ]

    def login(self):
        # In a real application, you'd validate the credentials against a database.
        # For simplicity, we'll assume any input is valid.
        username = input("Enter your username: ")
        self.logged_in_user_label.config(text=f"Logged in as: {username}")

    def view_knowledge(self):
        # Display existing knowledge shares
        knowledge_text = "\n".join(self.knowledge_shares)
        messagebox.showinfo("View Knowledge", knowledge_text)

    def contribute_knowledge(self):
        if self.logged_in_user_label.cget("text"):
            # Implement logic to allow users to contribute knowledge (e.g., write an article)
            new_knowledge = input("Enter your knowledge share: ")
            self.knowledge_shares.append(new_knowledge)
            messagebox.showinfo("Contribute Knowledge", "Thank you for sharing your knowledge!")
        else:
            messagebox.showwarning("Not Logged In", "Please log in first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WorldKnowledgeShareGUI(root)
    root.mainloop()
