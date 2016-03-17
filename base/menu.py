from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.label import Label

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from pkas.uix import Interactive, load_kv, Selector


class PKButton(Interactive, ButtonBehavior, Label):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)


  def on_delve(self, app):
    self.dispatch('on_press')


load_kv('base', 'menu.kv')


class MenuDialog(BoxLayout, Interactive):

  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.selector = Selector(self.children)


  def on_up(self, app):
    app.controller.focus = self.selector.increment()


  def on_down(self, app):
    app.controller.focus = self.selector.decrement()


  def on_active(self, app):
    app.controller.focus = self.selector.selected


  def on_inactive(self, app):
    app.controller.focus = None

    