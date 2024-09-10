from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(padding=4)
        btn = Button(text='Click Me', size_hint=(None, None), size=(400, 100)) 
        colors = [
            (1, 0, 0, 1),  
            (0, 1, 0, 1),  
            (0, 0, 1, 1),  
            (1, 1, 0, 1),  
            (1, 0, 1, 1),  
            (0, 1, 1, 1),  
            (1, 1, 1, 1)   
        ]
        self.current_color_index = 0

        def on_click(instance):
            instance.background_color = colors[self.current_color_index]
            self.current_color_index = (self.current_color_index + 1) % len(colors)

        btn.bind(on_press=on_click)
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    MyApp().run()
