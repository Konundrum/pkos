from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from pkas.ui import Interactive, load_kv, Walker


load_kv('base', 'menu.kv')


class MenuDialog(BoxLayout, Interactive):

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.walker = Walker(widgets=self.children)


  def on_up(self, controller):
    controller.focus = self.walker.forward()


  def on_down(self, controller):
    controller.focus = self.walker.backward()


  def on_active(self, controller):
    controller.focus = self.walker.widget


  def on_inactive(self, controller):
    controller.focus = None

    