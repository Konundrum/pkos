from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout

from pkas.data import factory, specify
from pkas.ui import load_kv, Interactive, DataView

from base.ui import PKButton


load_kv('base', 'context.kv')




@specify
class ContextTab(PKButton):
  pass
    



class ContextTabRow(DataView, BoxLayout):

  data_widget = ContextTab


  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    
    make = factory.make
    l = make('DataList')
    for i in range(10):
      l.append(make('DataContext', name=str(i)))

    self.data_list = l




class ContextView(Interactive, RelativeLayout):
  pass  

