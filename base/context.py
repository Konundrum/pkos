from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout

from pkas import *
from base.ui import PKButton


load_kv('base', 'context.kv')




@specify
class ContextTab(PKButton):
    model = DataProperty(factory.make('FileContext'))



class ContextTabRow(ListView, BoxLayout):

    selected = SelectorProperty(allownone=True)


    def __init__(self, **kwargs):
        super().__init__(cls=ContextTab, **kwargs)
        self.data = factory.make('DataList')
        self.walker = Walker(data=self.data)
        # print('tabrow Ctor:', self._data_uids)


    def next(self):
        self.selected = self.walker.inc()

    def prev(self):
        self.selected = self.walker.dec()


    def close_tab(self, tab=None):
        print('closing tab', self.data.data, '\n', self.displayed.data)
        if tab:
            i = self.get_child_index(tab)
        elif len(self.data) > 0:
            i = self.walker.index
        else:
            return

        del self.data[i]
        self.selected = self.walker.current
        print('closed tab', self.data.data, '\n', self.displayed.data)


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
        print('opening tab', self.data.data, '\n', self.displayed.data)
        self.data.insert(self.walker.index + 1,
                factory.make('FileContext',
                             name=str(self.tab_num),
                             filename='my_file.pkm',
                             data=dict(a=factory.make('DataModel'))))
        self.selected = self.walker.inc()
        self.tab_num += 1
        print('opened tab', self.data.data, '\n', self.displayed.data)



class ContextView(Interactive, RelativeLayout):
    pass

