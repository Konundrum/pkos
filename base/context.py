from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout

from pkas.data import factory, specify, SelectorProperty
from pkas.ui import load_kv, Interactive, DataView, RecyclerView, Walker
from base.ui import PKButton


load_kv('base', 'context.kv')




@specify
class ContextTab(PKButton):

    defaultmodel = factory.make('DataContext')




class ContextTabRow(RecyclerView, BoxLayout):


    selected = SelectorProperty(allownone=True)


    def __init__(self, **kwargs):
        super().__init__(cls=ContextTab, **kwargs)
        self.walker = Walker()
        self.data = factory.make('DataList')
        self.walker.data = self.data


    def next(self):
        self.selected = self.walker.inc()


    def prev(self):
        self.selected = self.walker.dec()


    def close_tab(self, tab=None):
        if tab:
            i = self.get_child_index(tab)
        elif len(self.data) > 0:
            i = self.walker.index
        else:
            return

        del self.data[i]
        self.selected = self.walker.current



    def shift_up(self):
        c = self.data
        i = self.walker.index
        if i > 0:
            c.swap(i, i-1)
            self.walker.index -= 1


    def shift_down(self):
        c = self.data
        i = self.walker.index
        if i < (len(c) - 1):
            c.swap(i, i+1)
            self.walker.index += 1


    tab_num = 0
    def new_tab(self):
        self.data.insert(self.walker.index + 1,
                factory.make('DataContext', name=str(self.tab_num)))
        self.selected = self.walker.inc()
        self.tab_num += 1



class ContextView(Interactive, RelativeLayout):
    pass

