from ._anvil_designer import manag_prodTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class manag_prod(manag_prodTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.manage_products.manage_producs1')

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.manage_products.view_product')

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.manage_products.view_categories')

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard')

 
