from kivy.uix.floatlayout import FloatLayout
from pkas.ui import Interactive, load_kv
from base.menu import MenuDialog
import base.context

load_kv('base', 'root.kv')



class PKOSRoot(Interactive, FloatLayout):


  def on_active(self, controller):
    self.menu = MenuDialog()



  def on_toggle_menu(self, controller):
    if self.menu in self.children:
      self.remove_widget(self.menu)
      controller.region = self.ids.context_view
    else:
      self.add_widget(self.menu)
      controller.region = self.menu
