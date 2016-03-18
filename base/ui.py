from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.label import Label

from pkas.ui import Interactive, DataWidget




class PKButton(Interactive, DataWidget, ButtonBehavior, Label):
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)


  def on_delve(self, controller):
    self.dispatch('on_press')

