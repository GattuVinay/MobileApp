from altair import Color
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from matplotlib.patches import Rectangle
from kivy.uix.popup import Popup
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Load KV files
Builder.load_file('kv/main.kv')

USER_DATABASE = {
    "1": "1",
    "user2": "password2",
}

class HomeScreen(Screen):
    pass

class LessonsScreen(Screen):
    pass

class AutomataPracticeScreen(Screen):
    pass

class QuizScreen(Screen):
    pass

class AutomataScreen(Screen):
    pass

class FormalLanguagesScreen(Screen):
    pass

class GrammarsScreen(Screen):
    pass

class AutomataDetailScreen(Screen):
    pass

class FormalLanguageDetailScreen(Screen):
    pass

class FormalPracticeScreen(Screen):
    pass

class FormalDetailScreen(Screen):
    pass

class GrammarsDetailScreen(Screen):
    pass

class LoginScreen(Screen):
    def validate_user(self):
        user_id = self.ids.user_id.text
        password = self.ids.password.text

        if user_id in USER_DATABASE and USER_DATABASE[user_id] == password:
            self.ids.login_message.text = "Login successful!"
            self.manager.current = 'home'
        else:
            self.ids.login_message.text = "Invalid user ID or password. Please try again."
    
    def change_background_color(self, r, g, b, a):
        with self.canvas.before:
            Color(r, g, b, a)
            Rectangle(pos=self.pos, size=self.size)

class ProfilePopup(Popup):
    def __init__(self, username="user1", profile_image_path="profile_picture.png", **kwargs):
        super().__init__(**kwargs)
        self.title = "User Profile"
        self.size_hint = (0.5, 0.5)  
        self.auto_dismiss = True

        # Main layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Profile Image
        profile_image = Image(source=profile_image_path, size_hint=(None, None))
        layout.add_widget(profile_image)

        # Username Label
        username_label = Label(text=f"Username: {username}", font_size=20, halign='center', valign='middle')
        layout.add_widget(username_label)

        # Close Button
        close_button = Button(text="Close", size_hint_y=None, height=40)
        close_button.bind(on_press=self.dismiss)
        layout.add_widget(close_button)

        # Add layout to the popup
        self.content = layout

class FormalLanguagesApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.category = None
        self.current_question_index = 0
        self.score = 0
        
    def build(self):

        self.current_question_index = 0
        self.score = 0
        self.selected_category =None
        
        # Define a list of questions
        self.questions = {
            "automata": [
                {
                    "question": "Which automaton accepts a context-free language?",
                    "options": ["DFA", "NFA", "PDA", "Turing Machine"],
                    "answer": "C"
                },
                {
                    "question": "What does the transition function in a DFA define?",
                    "options": [
                        "Mapping of states to symbols",
                        "Mapping of symbols to states",
                        "Mapping of state-symbol pairs to states",
                        "Mapping of state pairs to symbols"
                    ],
                    "answer": "C"
                },
            ],
            "grammars": [
                {
                    "question": "Which grammar generates a regular language?",
                    "options": ["Regular Grammar", "Context-Free Grammar", "Context-Sensitive Grammar", "None"],
                    "answer": "A"
                },
                {
                    "question": "Which grammar type is the most restrictive?",
                    "options": ["Type 3", "Type 2", "Type 1", "Type 0"],
                    "answer": "D"
                },
            ],
            "formal_languages": [
                {
                    "question": "Which of these is a formal language?",
                    "options": ["Python", "English", "C++", "All of the above"],
                    "answer": "D"
                },
                {
                    "question": "What is the Chomsky Normal Form used for?",
                    "options": [
                        "Converting a PDA into a DFA",
                        "Simplifying context-free grammars",
                        "Testing regular expressions",
                        "None of the above"
                    ],
                    "answer": "B"
                },
            ],
        }

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(LessonsScreen(name='lessons'))
        sm.add_widget(AutomataPracticeScreen(name='automata_practice'))
        sm.add_widget(QuizScreen(name='quiz'))
        sm.add_widget(AutomataScreen(name='automata'))
        sm.add_widget(FormalLanguagesScreen(name='formal_languages'))
        sm.add_widget(GrammarsScreen(name='grammars'))
        sm.add_widget(AutomataDetailScreen(name='detail'))
        sm.add_widget(FormalDetailScreen(name='formal_detail'))
        sm.add_widget(GrammarsDetailScreen(name='grammar_detail'))
        sm.add_widget(FormalLanguageDetailScreen(name='formal_languages'))
        sm.add_widget(FormalPracticeScreen(name='formallanguage'))
        return sm

    def refresh_screen(self, screen_name):
        """
        Resets the practice state if returning to the automata or practice screens.
        """
        if screen_name == 'automata':
            # Reset practice questions when returning to Automata Lessons
            self.reset_questions()
        elif screen_name == 'automata_practice':
            # Reset when revisiting Practice screen directly
            self.reset_questions()

        # Switch to the target screen
        self.root.current = screen_name

    def show_profile_popup(self):
      profile_popup = ProfilePopup(username="user1", profile_image_path="Profile.png")
      profile_popup.open()
    
    def reset_questions(self):
      
        self.current_question_index = 0
        self.score = 0

        # Reset the Practice Screen elements
        screen = self.root.get_screen('automata_practice')
        screen.ids.question_label.text = "Question will appear here."
        screen.ids.option_a.text = "Option A"
        screen.ids.option_b.text = "Option B"
        screen.ids.option_c.text = "Option C"
        screen.ids.option_d.text = "Option D"
        screen.ids.option_a.disabled = False
        screen.ids.option_b.disabled = False
        screen.ids.option_c.disabled = False
        screen.ids.option_d.disabled = False

        # Display the first question again
        self.display_question()

    def display_question(self):
       
        question_data = self.questions[self.current_question_index]
        screen = self.root.get_screen('automata_practice')
        screen.ids.question_label.text = question_data["question"]
        screen.ids.option_a.text = f"A. {question_data['options'][0]}"
        screen.ids.option_b.text = f"B. {question_data['options'][1]}"
        screen.ids.option_c.text = f"C. {question_data['options'][2]}"
        screen.ids.option_d.text = f"D. {question_data['options'][3]}" 
    
    def on_start(self):
        pass

    def select_category(self, category):
        """Set the selected category and initialize the quiz."""
        self.selected_category = category
        self.current_question_index = 0
        self.score = 0
        self.display_question()

    def display_question(self):
        """Display the current question and its options."""
        screen = self.root.get_screen('automata_practice')
        category_questions = self.questions[self.selected_category]
        question_data = category_questions[self.current_question_index]

        screen.ids.question_label.text = question_data["question"]
        screen.ids.option_a.text = f"A. {question_data['options'][0]}"
        screen.ids.option_b.text = f"B. {question_data['options'][1]}"
        screen.ids.option_c.text = f"C. {question_data['options'][2]}"
        screen.ids.option_d.text = f"D. {question_data['options'][3]}"

    def check_answer(self, selected_option):
        """Validate the selected answer and proceed to the next question."""
        category_questions = self.questions[self.selected_category]
        correct_answer = category_questions[self.current_question_index]["answer"]

        if selected_option == correct_answer:
            self.score += 1
            print("Correct! Your score:", self.score)
        else:
            print("Wrong! The correct answer was:", correct_answer)

        # Move to the next question
        self.current_question_index += 1

        if self.current_question_index < len(category_questions):
            self.display_question()
        else:
            self.show_final_score()

    def show_final_score(self):
     """Display the final score and hide question options."""
     screen = self.root.get_screen('automata_practice')
     final_score_message = f"Quiz complete! Your score: {self.score}/{len(self.questions[self.selected_category])}"

     # Update the score label
     screen.ids.question_label.text  = final_score_message

     # Hide the options
     for option in ['option_a', 'option_b', 'option_c', 'option_d']:
         screen.ids[option].opacity = 0
         screen.ids[option].size_hint_y = None
         screen.ids[option].height = 10

    
    def set_automata_detail(self, title, content):
        """Update AutomataDetailScreen with the topic content."""
        detail_screen = self.root.get_screen('detail')
        detail_screen.ids.title.text = title
        detail_screen.ids.content.text = content
        self.root.current = 'detail'
    

    def set_formal_detail(self, title, content):
        """Update Formal Details screen with the topic content."""
        detail_screen = self.root.get_screen('formal_detail')
        detail_screen.ids.title.text = title
        detail_screen.ids.content.text = content
        self.root.current = 'formal_detail'
        
    def set_gramma_detail(self, title, content):
        """Update Gamma Details screen with the topic content."""
        detail_screen = self.root.get_screen('grammar_detail')
        detail_screen.ids.title.text = title
        detail_screen.ids.content.text = content
        self.root.current = 'grammar_detail'
        

    
if __name__ == "__main__":
    FormalLanguagesApp().run()

