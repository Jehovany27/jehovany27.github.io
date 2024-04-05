class WorldKnowledgeShare:
    def __init__(self):
        self.logged_in_user = None

    def display_title(self):
        print("=== World Knowledge Share ===")

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # In a real application, you'd validate the credentials against a database.
        # For simplicity, we'll assume any input is valid.
        self.logged_in_user = username
        print(f"Welcome, {username}!")

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. View Knowledge")
            print("2. Contribute Knowledge")
            print("3. Logout")
            choice = input("Enter your choice (1/2/3): ")

            if choice == "1":
                self.view_knowledge()
            elif choice == "2":
                self.contribute_knowledge()
            elif choice == "3":
                self.logout()
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")

    def view_knowledge(self):
        print("\nViewing Knowledge:")
        # Implement logic to display existing knowledge (e.g., articles, posts, etc.)

    def contribute_knowledge(self):
        if self.logged_in_user:
            print("\nContribute Knowledge:")
            # Implement logic to allow users to contribute knowledge (e.g., write an article)

    def logout(self):
        self.logged_in_user = None
        print("Logged out. Thank you for using World Knowledge Share!")

if __name__ == "__main__":
    wks = WorldKnowledgeShare()
    wks.display_title()
    wks.login()
    wks.main_menu()
