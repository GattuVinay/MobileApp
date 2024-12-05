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

class QuizScreen(Screen):
    pass

class ScoreScreen(Screen):
    pass

class GrammarPracticeScreen(Screen):
    def display_question(self, category):
        # Ensure the category is valid
        if category not in self.questions:
            return

        # Get the current question based on index
        question_data = self.questions[category][self.current_question_index]
        
        # Update the question label text
        self.ids.question_label.text = question_data["question"]
        
        # Update the option button texts
        self.ids.option_a.text = question_data["options"][0]
        self.ids.option_b.text = question_data["options"][1]
        self.ids.option_c.text = question_data["options"][2]
        self.ids.option_d.text = question_data["options"][3]

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

class FormalLanguagesApp(App,Screen):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.category = None
    #     self.current_question_index = 0
    #     self.score = 0
        
    def build(self):
        self.current_question_index = 0
        self.score = 0
        self.selected_category = None
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

        self.selected_category = None
        self.current_question_index = 0
        self.score = 0
        
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
        sm.add_widget(FormalPracticeScreen(name='formalpraticescreen'))
        sm.add_widget(GrammarPracticeScreen(name='grammarpratice'))
        sm.add_widget(QuizScreen(name='quiz'))
        sm.add_widget(ScoreScreen(name='score'))
        # sm.get_screen('automata').load_question()
        return sm
    
    def on_start(self):
        pass

    def load_question(self):
      """
      Load the current question based on the selected category and question index.
      """
      category_questions = self.questions[self.selected_category]
      
      if self.current_question_index < len(category_questions):
          # Get the current question
          question_data = category_questions[self.current_question_index]
          
          # Update the question label and options dynamically
          automata_screen = self.root.get_screen('automata')
          
          # Ensure we are updating the ids correctly
          automata_screen.ids.question_label.text = question_data["question"]
          automata_screen.ids.option_a.text = f"A. {question_data['options'][0]}"
          automata_screen.ids.option_b.text = f"B. {question_data['options'][1]}"
          automata_screen.ids.option_c.text = f"C. {question_data['options'][2]}"
          automata_screen.ids.option_d.text = f"D. {question_data['options'][3]}"
          
      else:
          # If there are no more questions, navigate to the score screen
          self.root.current = 'score'
          self.root.get_screen('score').ids.score_label.text = f"Your Final Score: {self.score}"



    def update_question(self):
        # Get the current question set and question
        category_questions = self.questions[self.selected_category]
        question_data = category_questions[self.current_question_index]
        
        # Update the UI
        screen = self.root
        screen.ids.question_label.text = question_data["question"]
        screen.ids.option_a.text = question_data["options"][0]
        screen.ids.option_b.text = question_data["options"][1]
        screen.ids.option_c.text = question_data["options"][2]
        screen.ids.option_d.text = question_data["options"][3]

    # def refresh_screen(self, screen_name):
    #     """Reset the screen based on the selected category."""
    #     if screen_name == 'automata':
    #         self.selected_category = 'automata'
    #         self.reset_questions(screen_name)
    #         self.root.current = screen_name
    #     elif screen_name == 'grammars':
    #         self.selected_category = 'grammars'
    #         self.reset_questions(screen_name)
    #         self.root.current = screen_name
    #     elif screen_name == 'formal_languages':
    #         self.selected_category = 'formal_languages'
    #         self.reset_questions(screen_name)
    #         self.root.current = screen_name


    def refresh_screen(self, category):
        """
        Refresh the screen by resetting the score and question index.
        """
        self.selected_category = category
        self.current_question_index = 0
        self.score = 0
        self.load_question()    
        
        # # Reset any other states if necessary
        # self.reset_questions(screen_name)

        # # Switch to the selected screen
        # self.root.current = screen_name

    def show_profile_popup(self):
      profile_popup = ProfilePopup(username="user1", profile_image_path="Profile.png")
      profile_popup.open()
    
    def reset_questions(self,screen_name):
        """Reset the question index and score, and display the first question."""
        self.current_question_index = 0
        self.score = 0
        self.display_question(screen_name)
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
        self.display_question(screen_name)

    # def display_question(self,):
       
    #     question_data = self.questions[self.current_question_index]
    #     screen = self.root.get_screen('automata_practice')
    #     screen.ids.question_label.text = question_data["question"]
    #     screen.ids.option_a.text = f"A. {question_data['options'][0]}"
    #     screen.ids.option_b.text = f"B. {question_data['options'][1]}"
    #     screen.ids.option_c.text = f"C. {question_data['options'][2]}"
    #     screen.ids.option_d.text = f"D. {question_data['options'][3]}" 
    

    def select_category(self, category):
        """
        Set the selected category and load the first question.
        """
        self.selected_category = category
        self.current_question_index = 0
        self.score = 0
        self.load_question()
        self.root.current = 'quiz'

    def load_question(self):
        """
        Load the current question based on the selected category and question index.
        """
        category_questions = self.questions[self.selected_category]
        if self.current_question_index < len(category_questions):
            question_data = category_questions[self.current_question_index]
            quiz_screen = self.root.get_screen('quiz')
            quiz_screen.ids.question_label.text = question_data["question"]
            quiz_screen.ids.option_a.text = f"A. {question_data['options'][0]}"
            quiz_screen.ids.option_b.text = f"B. {question_data['options'][1]}"
            quiz_screen.ids.option_c.text = f"C. {question_data['options'][2]}"
            quiz_screen.ids.option_d.text = f"D. {question_data['options'][3]}"
        else:
            # All questions attempted, go to the score screen
            self.root.current = 'score'
            self.root.get_screen('score').ids.score_label.text = f"Your Final Score: {self.score}"


    def display_question(self,screen_name):
        """Display the current question and options."""
        # Get the appropriate questions based on selected category
        question_data = self.questions[self.selected_category][self.current_question_index]
        screen = screen_name
        if screen =='automata_practice' :
         screen = self.root.get_screen('automata_practice') 
         screen.ids.question_label.text = question_data["question"]
         screen.ids.option_a.text = f"A. {question_data['options'][0]}"
         screen.ids.option_b.text = f"B. {question_data['options'][1]}" 
         screen.ids.option_c.text = f"C. {question_data['options'][2]}"
         screen.ids.option_d.text = f"D. {question_data['options'][3]}"
        elif screen =='formal_languages' :
            screen = self.root.get_screen('formal_languages')
        elif screen == 'grammars':
            screen = self.root.get_screen('grammars')

        screen.ids.question_label.text = question_data["question"]
        screen.ids.option_a.text = f"A. {question_data['options'][0]}"
        screen.ids.option_b.text = f"B. {question_data['options'][1]}"
        screen.ids.option_c.text = f"C. {question_data['options'][2]}"
        screen.ids.option_d.text = f"D. {question_data['options'][3]}"
    

    def display_question(self,screen_name):
        """Display the current question and its options."""
        if (screen_name == 'automata_practice' ) :
          question_data = self.questions[self.selected_category][self.current_question_index]
          screen = self.root.get_screen('automata_practice')
          screen.ids.question_label.text = question_data["question"]
          screen.ids.option_a.text = f"A. {question_data['options'][0]}"
          screen.ids.option_b.text = f"B. {question_data['options'][1]}"
          screen.ids.option_c.text = f"C. {question_data['options'][2]}"
          screen.ids.option_d.text = f"D. {question_data['options'][3]}"
        elif (screen_name == 'grammarpratice') :
          question_data = self.questions[self.selected_category][self.current_question_index]
          screen = self.root.get_screen('grammarpratice')
          screen.ids.question_label.text = question_data["question"]
          screen.ids.option_a.text = f"A. {question_data['options'][0]}"
          screen.ids.option_b.text = f"B. {question_data['options'][1]}"
          screen.ids.option_c.text = f"C. {question_data['options'][2]}"
          screen.ids.option_d.text = f"D. {question_data['options'][3]}"
        elif (screen_name == 'formalpraticescreen') :
          question_data = self.questions[self.selected_category][self.current_question_index]
          screen = self.root.get_screen('formalpraticescreen')
          screen.ids.question_label.text = question_data["question"]
          screen.ids.option_a.text = f"A. {question_data['options'][0]}"
          screen.ids.option_b.text = f"B. {question_data['options'][1]}"
          screen.ids.option_c.text = f"C. {question_data['options'][2]}"
          screen.ids.option_d.text = f"D. {question_data['options'][3]}"


    # def display_question(self, screen_name):
    #   """Display the current question and its options dynamically."""
    #   try:
    #       # Ensure the selected category is set
    #       print(f"Selected Category: {self.selected_category}")
          
    #       # Fetch the question data for the selected category and index
    #       question_data = self.questions[self.selected_category][self.current_question_index]
    #       print(f"Current Question Data: {question_data}")
  
    #       # Get the correct screen based on screen_name
    #       screen = self.root.get_screen(screen_name)
          
    #       # Set the question text and options dynamically
    #       screen.ids.question_label.text = question_data["question"]
    #       screen.ids.option_a.text = f"A. {question_data['options'][0]}"
    #       screen.ids.option_b.text = f"B. {question_data['options'][1]}"
    #       screen.ids.option_c.text = f"C. {question_data['options'][2]}"
    #       screen.ids.option_d.text = f"D. {question_data['options'][3]}"
      
    #   except Exception as e:
    #       print(f"Error displaying question on screen {screen_name}: {e}")

    def check_answer(self, selected_option):
        """
        Check the selected answer and move to the next question.
        """
        category_questions = self.questions[self.selected_category]
        correct_answer = category_questions[self.current_question_index]["answer"]
        if selected_option == correct_answer:
            self.score += 1
        self.current_question_index += 1
        self.load_question()

    def show_score(self):
        # Display the final score
        screen = self.root
        screen.ids.question_label.text = f"You scored {self.score}/{len(self.questions[self.selected_category])}!"
        screen.ids.option_a.text = ""
        screen.ids.option_b.text = ""
        screen.ids.option_c.text = ""
        screen.ids.option_d.text = ""

    
    def set_automata_detail(self, chapter_heading, paragraph_heading, content):
     try:
         # Get the detail screen
         detail_screen = self.root.get_screen('detail')
         
         # Set the text for heading, paragraph, and content
         detail_screen.ids.heading_label.text = chapter_heading
         detail_screen.ids.paragraph_heading.text = paragraph_heading
         detail_screen.ids.content_label.text = content
 
         # Navigate to the detail screen
         self.root.current = 'detail'
     except KeyError as e:
         print(f"Error: ID not found in KV file - {e}")
     except AttributeError as e:
         print(f"Error: Attribute issue - {e}")
    

    def set_formal_detail(self, chapter_heading,paragraph_heading, content):
        """Update Formal Details screen with the topic content."""
        try:
            detail_screen =self.root.get_screen('formal_detail')
            detail_screen.ids.heading_label.text = chapter_heading
            detail_screen.ids.paragraph_heading.text = paragraph_heading
            detail_screen.ids.content_label.text = content
            self.root.current = 'formal_detail'
        except KeyError as e:
            print(f"Error: ID not found in KV file - {e}")
        except AttributeError as e:
            print(f"Error: Attribute issue - {e}")
        
    def set_gramma_detail(self, chapter_heading,paragraph_heading, content):
        """Update Gamma Details screen with the topic content."""
        try:
            detail_screen = self.root.get_screen('grammar_detail')
            detail_screen.ids.heading_label.text = chapter_heading
            detail_screen.ids.paragraph_heading.text = paragraph_heading
            detail_screen.ids.content_label.text = content
            self.root.current ='grammar_detail'
        except KeyError as e:
            print(f"Error: ID not found in KV file - {e}")
        except AttributeError as e:
            print(f"Error: Attribute issue - {e}")

    def reset_quiz(self):
        """
        Reset the quiz by clearing the current question index and score.
        """
        self.current_question_index = 0
        self.score = 0
        self.selected_category = None
        

    
if __name__ == "__main__":
    FormalLanguagesApp().run()

