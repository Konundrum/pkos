from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

from pkas import Interactive, load_kv
from base.menu import MenuDialog
import base.context


load_kv('base', 'root.kv')



class PKOSRoot(Interactive, FloatLayout):

    def on_active(self, controller):
        self.menu = MenuDialog()
        self.tabs = self.ids.tabs
        self.bound_uid = self.tabs.fbind('selected',
            lambda p,f: setattr(controller, 'file', f))


    def on_inactive(self, controller):
        self.tabs.unbind_uid('selected', self.bound_uid)


    def on_toggle_menu(self, controller):
        if self.menu in self.children:
            self.remove_widget(self.menu)
            controller.region = self.ids.view
        else:
            self.add_widget(self.menu)
            controller.region = self.menu


    def on_tab(self, controller):
        self.tabs.next()

    def on_untab(self, controller):
        self.tabs.prev()

    def on_close_tab(self, controller):
        self.tabs.close_tab()


    def on_new_tab(self, controller):
        self.tabs.new_tab()


    def on_shift_up(self, controller):
        self.tabs.shift_up()

    def on_shift_down(self, controller):
        self.tabs.shift_down()

    def on_save(self, controller):
        controller.file.save()
