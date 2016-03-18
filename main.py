from kivy.config import Config
Config.set('kivy', 'exit_on_escape', 0)

from pkas.app import PKApp
from base.root import PKOSRoot



class PKOS(PKApp):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
  


  def build(self):
    return PKOSRoot()
    
    
    
  def build_config(self, config):
    config.setdefaults('keybinds', {
      'left': '["a", "left"]',
      'right': '["d", "right"]',
      'up': '["w", "up"]',
      'down': '["s", "down"]',
      'toggle_overlay': '["q"]',
      'select': '["e"]',
      'delve': '["space", "enter"]',
      'ascend': '["shift + space", "shift + enter"]',
      'toggle_menu' : '["escape"]',
    })



if __name__ == '__main__':
  app = PKOS()
  app.run()
  