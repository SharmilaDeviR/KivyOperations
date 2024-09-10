from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label


class ToggleButtonApp(App):
    def build(self):
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.label = Label(text='Toggle is OFF', font_size=24)
        
        self.toggle_button = ToggleButton(text='OFF', state='normal', size_hint=(None, None), size=(400, 100))
        
       
        self.toggle_button.bind(on_release=self.on_toggle)
        
        layout.add_widget(self.toggle_button)
        layout.add_widget(self.label)
        
        return layout

    def on_toggle(self, instance):
 
        if instance.state == 'down':
            instance.text = 'ON'
            self.label.text = 'Toggle is ON'
        else:
            instance.text = 'OFF'
            self.label.text = 'Toggle is OFF'


if __name__ == '__main__':
    ToggleButtonApp().run()
