from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout

from pkas import *

from src.ui import PKButton
load_kv('src', 'base.kv')



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



    def on_tab(self, controller): self.tabs.walk_down()
    def on_untab(self, controller): self.tabs.walk_up()

    def on_tabs_right(self, controller):
        self.tabs.scroll_down()
        self.tabs.walker.dec()
    def on_tabs_left(self, controller):
        self.tabs.scroll_up()
        self.tabs.walker.inc()

    def on_close_tab(self, controller): self.tabs.close_tab()
    def on_new_tab(self, controller): self.tabs.new_tab()

    def on_shift_up(self, controller): self.tabs.shift_up()
    def on_shift_down(self, controller): self.tabs.shift_down()

    def on_save(self, controller): controller.file.save()





@specify
class ContextTab(PKButton):

    model = DataProperty(factory.make('FileContext'))




class ContextTabRow(DequeReducerView, BoxLayout):

    selected = SelectorProperty()

    def __init__(self, **kwargs):
        super().__init__(cls=ContextTab,
                         data=factory.make('DataList'),
                         displayed_total=4,
                         **kwargs)

        self.walker = Walker(data=self.displayed)
        self.walker_uid = self.walker.fbind('current',
            lambda p, c: setattr(self, 'selected', c))



    def close_tab(self, tab=None):
        if tab:
            index = self.get_child_index(tab)
        elif len(self.data) > 0:
            index = self.displayed_index + self.walker.index
        else: return

        del self.data[index]
        if self.walker.current is None: self.scroll_up()
        self.walker.update()


    def shift_up(self):
        data = self.data
        index = self.displayed_index + self.walker.index

        if index > 0:
            data.swap(index, index - 1)
            if self.walker.index == 0: self.scroll_up()
            self.walker.dec()


    def shift_down(self):
        data = self.data
        index = self.displayed_index + self.walker.index

        if index < (len(data) - 1):
            data.swap(index, index + 1)
            if self.walker.index == self.displayed_total - 1:
                self.scroll_down()
            self.walker.inc()


    tab_num = 0
    def new_tab(self):
        if self.walker.index == self.displayed_total - 1:
            self.scroll_down()

        model = factory.make('FileContext',
                             name=str(self.tab_num),
                             filename='my_file.pkm',
                             data=dict(a=factory.make('DataModel')))

        self.data.insert(self.displayed_index + self.walker.index + 1, model)
        self.walker.current = model
        self.tab_num += 1


    def walk_down(self):
        if self.walker.index == self.displayed_total - 1:
            self.scroll_down()
        self.walker.inc()

    def walk_up(self):
        if self.walker.index == 0:
            self.scroll_up()
        self.walker.dec()




class ContextView(Interactive, RelativeLayout):
    pass





class MenuDialog(BoxLayout, Interactive):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.walker = Walker(data=self.children)

    def on_active(self, controller):
        controller.focus = self.walker.current
        self._walker_uid = self.walker.fbind(
            'current', lambda p,v: setattr(controller, 'focus', v))
        self.walker.update()

    def on_inactive(self, controller):
        self.walker.unbind_uid('focus', self._walker_uid)
        controller.focus = None

    def on_up(self, controller): self.walker.inc()
    def on_down(self, controller): self.walker.dec()



