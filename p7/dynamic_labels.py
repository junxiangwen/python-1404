from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = {"xxx","yyy","zzz"}

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.creat_widgets()
        return self.root

    def creat_widgets(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
