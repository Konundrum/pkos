from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from pkas.uix import Interactive, PKButton, load_kv

load_kv('base', 'context.kv')



# TODO: Adapter Pattern for ContextTabs
#  (using factory / recycler)


class ContextTab(PKButton):
  pass
  # def __init__(self, **kwargs):
  #   super().__init__(**kwargs)
    



class ContextTabRow(BoxLayout):
  pass  
  # def __init__(self, **kwargs):
  #   super().__init__(**kwargs)




class ContextView(Interactive, RelativeLayout):
  pass  
  # def __init__(self, **kwargs):
  #   super().__init__(**kwargs)
