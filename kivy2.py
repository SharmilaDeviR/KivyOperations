from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class SliderApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.label = Label(text='Slider Value: 0', font_size='20sp')
        self.slider = Slider(min=0, max=100, value=0)
        self.slider.bind(value=self.on_value_change)
        
        layout.add_widget(self.label)
        layout.add_widget(self.slider)
        
        return layout

    def on_value_change(self, instance, value):
        self.label.text = f'Slider Value: {int(value)}'

if __name__ == '__main__':
    SliderApp().run()
