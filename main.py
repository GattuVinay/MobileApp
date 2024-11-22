from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# Load KV files
Builder.load_file('kv/main.kv')

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
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(LessonsScreen(name='lessons'))
        sm.add_widget(AutomataPracticeScreen(name='automata_practice'))
        sm.add_widget(QuizScreen(name='quiz'))
        sm.add_widget(AutomataScreen(name='automata'))
        sm.add_widget(FormalLanguagesScreen(name='formal_languages'))
        sm.add_widget(GrammarsScreen(name='grammars'))
        sm.add_widget(AutomataDetailScreen(name='detail'))
        sm.add_widget(FormalDetailScreen(name='formal_detail'))
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
        """Display the final score and disable question options."""
        screen = self.root.get_screen('automata_practice')
        final_score_message = f"Quiz complete! Your score: {self.score}/{len(self.questions[self.selected_category])}"
        screen.ids.question_label.text = final_score_message

        # Disable the options
        for option in ['option_a', 'option_b', 'option_c', 'option_d']:
            screen.ids[option].disabled = True
    
    def set_automata_detail(self, title, content):
        """Update AutomataDetailScreen with the topic content."""
        detail_screen = self.root.get_screen('detail')
        detail_screen.ids.title.text = title
        detail_screen.ids.content.text = content
        self.root.current = 'detail'
    
    # def set_formalLanguage_detail(self, title, content):
    #     """Update Formal Language with the topic content."""
    #     detail_screen = self.root.get_screen('detail')
    #     detail_screen.ids.title.text = title
    #     detail_screen.ids.content.text = content
    #     self.root.current = 'detail'
    
if __name__ == "__main__":
    FormalLanguagesApp().run()

