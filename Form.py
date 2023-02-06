# THIS IS FRONT-END CODE ON ANVI
# Go to Client Code, click Add Form, copy-paste this code into it. This calls the sendText() function in chatbotAnvi.py

from ._anvil_designer import Form1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
from datetime import datetime

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.


  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('sendtext', self.message.text, self.userList.text, self.upload.file)

  def message_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    pass

  def upload_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    pass
