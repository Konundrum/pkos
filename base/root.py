from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

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
      controller.region = self.ids.view
    else:
      self.add_widget(self.menu)
      controller.region = self.menu


  def on_tab(self, controller):
    self.ids.tabs.next()


  def on_untab(self, controller):
    self.ids.tabs.prev()


  def on_close_tab(self, controller):
    self.ids.tabs.close_tab()


  def on_new_tab(self, controller):
    self.ids.tabs.new_tab()
    

  def on_shift_up(self, controller):
    self.ids.tabs.shift_up() 

  def on_shift_down(self, controller):
    self.ids.tabs.shift_down()
    
