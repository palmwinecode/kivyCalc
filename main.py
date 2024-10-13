from kivy.app import App # type: ignore
from kivy.uix.boxlayout import BoxLayout # type: ignore
from kivy.uix.button import Button # type: ignore
from kivy.uix.textinput import TextInput # type: ignore

class CalculatorApp(App):

    def build(self):
        # Set app icon
        self.icon = "calculator.png"

        # Create instance variables
        # List of operators
        self.operators = ["/", "*", "+", "-"]
        
        # Track if last entry was an operator 
        self.last_was_operator = None

        # Track last entry
        self.last_button = None

        # Define main layout
        main_layout = BoxLayout(orientation="vertical")

        # Display screen
        self.display_screen = TextInput(background_color="black", foreground_color="white",
                                        multiline=False, halign="right", font_size=55, readonly=True)

        # Add display screen to main layout
        main_layout.add_widget(self.display_screen)

        # List of buttons
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"],
        ]

        # Add buttona to layout
        for row in buttons:
            # Create horizontal layout
            h_layout = BoxLayout(orientation="horizontal")
            for label in row:
                # Create button
                button = Button(
                    text=label, font_size=30, background_color="grey",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                  ) 
                # Add callback for each button
                button.bind(on_press=self.on_button_press)

                # Add button to horizontal layout
                h_layout.add_widget(button)
            
            # Add row to main layout
            main_layout.add_widget(h_layout)

        # Equal button
        equal_button = Button(
                    text="=", font_size=30, background_color="grey",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                  ) 
        
        # Add callback for equal button
        equal_button.bind(on_press=self.on_equal)

        # Add equal button to main layout
        main_layout.add_widget(equal_button)

        return main_layout

    # Button press callback function
    def on_button_press(self, instance):
        # Get current input
        current = self.display_screen.text

        # Get the text of the pressed button
        button = instance.text

        # Clear screen?
        if button == "C":
            # Clear screen
            self.display_screen.text = ""
        # Is there an entry? Is user trying to type two operator back to back?
        elif current and (
                self.last_was_operator and button in self.operators):
                return
        # Is user trying to start with an operator other than "-"?
        elif current == "" and button in ["/",  "*", "+"]:
            return

        else:
            # Add new entry
            new_text = current + button

            # Display entry
            self.display_screen.text = new_text

        # Reset check variables
        self.last_button = button
        self.last_was_operator = self.last_button in self.operators

    # Equal callback function
    def on_equal(self, instance):
        # Get current input
        current = self.display_screen.text

        # Is expression incomplete?
        if self.last_button in self.operators:
            return

        # Available input?
        if current:
            # Get solution(pending leading zero issue)
            solution = str(eval(self.display_screen.text))

            # Display solution
            self.display_screen.text = solution
    
if __name__ == "__main__":
    # Run App
    CalculatorApp().run()