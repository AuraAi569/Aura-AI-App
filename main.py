from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from google import genai

API_KEY = "AQ.Ab8RN6J0WgpppvB_J5F0IDxKSnICOAoUPGCo2wNc4he9SW7E5g"
client = genai.Client(api_key=API_KEY)

class AuraApp(App):
    def build(self):
        self.title = 'Aura AI'
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.scroll = ScrollView(size_hint=(1, 0.85))
        self.chat_history = Label(
            text="[b]Aura AI:[/b] Assalam-o-Alaikum! Main aap ka smart assistant hoon.\n\n",
            size_hint_y=None,
            markup=True,
            halign='left',
            valign='top'
        )
        self.chat_history.bind(texture_size=self.chat_history.setter('size'))
        self.scroll.add_widget(self.chat_history)
        layout.add_widget(self.scroll)
        
        input_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.15), spacing=5)
        self.text_input = TextInput(hint_text="Aap ka sawal...", multiline=False)
        send_btn = Button(text="Send", size_hint=(0.25, 1))
        send_btn.bind(on_press=self.send_message)
        
        input_layout.add_widget(self.text_input)
        input_layout.add_widget(send_btn)
        layout.add_widget(input_layout)
        
        return layout

    def send_message(self, instance):
        user_text = self.text_input.text.strip()
        if not user_text:
            return
            
        self.chat_history.text += f"[b]Aap:[/b] {user_text}\n"
        self.text_input.text = ""
        
        try:
            response = client.models.generate_content(
                model='gemini-3.8-flash',
                contents=user_text,
                config={'system_instruction': "You are Aura AI, a helpful AI assistant. Reply in Roman Urdu naturally."}
            )
            self.chat_history.text += f"[b]Aura AI:[/b] {response.text}\n\n"
        except Exception as e:
            self.chat_history.text += f"[b]Aura AI:[/b] Error: {e}\n\n"

if __name__ == '__main__':
    AuraApp().run()
