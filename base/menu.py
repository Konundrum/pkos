from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from pkas.ui import Interactive, load_kv, Selector


load_kv('base', 'menu.kv')


class MenuDialog(BoxLayout, Interactive):

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.selector = Selector(self.children)


  def on_up(self, controller):
    controller.focus = self.selector.increment()


  def on_down(self, controller):
    controller.focus = self.selector.decrement()


  def on_active(self, controller):
    controller.focus = self.selector.selected


  def on_inactive(self, controller):
    controller.focus = None

    