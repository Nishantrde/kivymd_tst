from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel

class MainApp(MDApp):
    def build(self):
        # Optional: ensure your app uses a dark background
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        screen = MDScreen()
        screen.add_widget(
            MDLabel(
                text="Hello, world!",
                halign="center",
                size_hint_y=0.1,
                pos_hint={"center_y": 0.5},
                # ← HERE we switch to “Custom” and set pure white:
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1),
            )
        )
        return screen

if __name__ == "__main__":
    MainApp().run()
