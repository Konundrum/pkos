from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from pkas.ui import Interactive, load_kv, Walker


load_kv('base', 'menu.kv')


class MenuDialog(BoxLayout, Interactive):

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.walker = Walker(self.children)


  def on_up(self, controller):
    controller.focus = self.walker.increment()


  def on_down(self, controller):
    controller.focus = self.walker.decrement()


  def on_active(self, controller):
    controller.focus = self.walker.position


  def on_inactive(self, controller):
    controller.focus = None

    