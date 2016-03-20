from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout

from pkas.data import factory, specify
from pkas.ui import load_kv, Interactive, DataView
from pkas.utils import Walker, SelectorProperty
from base.ui import PKButton


load_kv('base', 'context.kv')




@specify
class ContextTab(PKButton):
  pass
    



class ContextTabRow(DataView, BoxLayout):

  selected = SelectorProperty()


  def __init__(self, **kwargs):
    super().__init__(cls=ContextTab, **kwargs)
    self.data = factory.make('DataList')
    self.walker = Walker(list=self.data)


  def next(self):
    context = self.walker.inc()
    self.selected = context
    return context


  def prev(self):
    context = self.walker.dec()
    self.selected = context
    return context


  def close_tab(self):
    if len(self.data) > 0:
      del self.data[self.walker.index]
      context = self.walker.current
      self.selected = context
      return context
    return self.walker.current


  def shift_down(self):
    c = self.data
    i = self.walker.index
    if i < (len(c) - 1):
      c.swap(i, i+1)
      self.walker.index += 1


  def shift_up(self):
    c = self.data
    i = self.walker.index
    if i > 0:
      c.swap(i, i-1)
      self.walker.index -= 1


  tab_num = 0
  def new_tab(self):
    context = factory.make('DataContext', name=str(self.tab_num))
    self.tab_num += 1
    i = self.walker.index
    self.data.insert(i + 1, context)
    self.selected = context
    self.walker.current = context
    return context



class ContextView(Interactive, RelativeLayout):
  pass  

