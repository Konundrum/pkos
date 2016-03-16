from kivy.properties import DictProperty
from kivy.uix.floatlayout import FloatLayout
from pkas.uix import Interactive, load_kv
from base.menu import MenuDialog
import base.context

load_kv('base', 'root.kv')



class PKOSRoot(Interactive, FloatLayout):
  context = DictProperty()
  contexts = DictProperty()


  # def __init__(self, **kwargs):
  #   super().__init__(**kwargs)


  def on_active(self, app):
    self.menu = MenuDialog()



  def on_toggle_menu(self, app):
    if self.menu in self.children:
      self.remove_widget(self.menu)
      app.controller.region = self.ids.context_view
    else:
      self.add_widget(self.menu)
      app.controller.region = self.menu
