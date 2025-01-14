from ._anvil_designer import manag_proTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class manag_pro(manag_proTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.id = 'A' + str(1000000)  
    self.label_1.text = self.id
    self.data = tables.app_tables.product_details.search()

    a = -1
    self.list_1 = []
 
    for i in self.data:
      a+=1
      self.list_1.append(i['product_id']) 
    if a == -1 :
      self.id = 'A' + str(1000000)
      self.label_1.text = self.id
      
    else:
      self.id = 'A'+ str(int(self.list_1[-1][1:])+1)
      self.label_1.text = self.id
   
  def link_1_copy_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('admin.dashboard.manage_products')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""


    product_name = self.text_box_2.text
    product_discription = self.text_area_1.text
    processing_fee = int(self.text_box_3.text)
    extension_fee = int(self.text_box_4.text)
    discount_coupons = self.radio_button_3.text
    membership_type = self.drop_down_2.selected_value
    print(membership_type)
    interest_type = self.radio_button_1.text
    if interest_type :
      print(self.radio_button_1.text)
    else :
      print(self.radio_button_2.text)
    min_days = int(self.drop_down_3.selected_value)
    print(min_days)
    max_days = int(self.drop_down_4.selected_value)
    print(max_days)
    roi = int(self.text_box_5.text)
    print(roi)

    if product_name == "" or membership_type == "" or processing_fee == "" or extension_fee == "" or interest_type == "" or max_days == "" or min_days == ""  or discount_coupons == "" or roi == "":
      Notification("Fill All Required Details").show()
    else:
     anvil.server.call('product_details', self.id, product_name, processing_fee, extension_fee, membership_type, interest_type, max_days, min_days, roi, discount_coupons)
     product_id = self.label_1.text
     open_form('admin.dashboard.manage_products.add_group',product_id )
 

  def check_box_3_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    product_visibility = self.check_box_3.checked
    if  product_visibility :
      self.label_1.visible = True
      self.text_box_2.visible = True
      self.text_area_1.visible = True
      self.text_box_3.visible = True
      self.text_box_4.visible = True
      self.drop_down_2.visible = True
      self.radio_button_1.visible = True
      self.drop_down_3.visible = True
      self.drop_down_4.visible =True
      self.text_box_5.visible = True
      self.radio_button_3.visible = True
      self.radio_button_4.visible = True
    else:
      self.text_box_2.visible = False
      self.text_area_1.visible = False
      self.text_box_3.visible = False
      self.text_box_4.visible = False
      self.drop_down_2.visible = False
      self.radio_button_1.visible = False
      self.drop_down_3.visible = False
      self.drop_down_4.visible =False
      self.text_box_5.visible = False
      self.radio_button_3.visible = False
      self.radio_button_4.visible = False

    def drop_down_1_change(self, **event_args):
    
     if self.drop_down_1.selected_value == 'Home Loan':
            # Add items to the dropdown dynamically
      items_to_add = ['Home loan balance transfer', 'Top-up-loan', 'Pradhan Mantri AWAS Yojana', 'Joint Home Loans', 'Womens home loan', 'Home Construction loan', 'Plot for purchase', 'Home loan for private employees', 'Home loan for government employees', 'Home loan for bank employees', 'Home loan for advocates' ]
      self.drop_down_5.items = items_to_add
     elif self.drop_down_1.selected_value == 'Personal Loan':
            # Add items to the dropdown dynamically
      items_to_add = ['Credit Card', 'Digital Loans against Mutual Funds', 'Gold Loans']
      self.drop_down_5.items = items_to_add  
     elif self.drop_down_1.selected_value == 'Vehicle Loan':
            # Add items to the dropdown dynamically
      items_to_add = ['Car Loans', 'Two-Wheeler Loans', 'Pre-owned Car Loans']
      self.drop_down_5.items = items_to_add  
     elif self.drop_down_1.selected_value == 'Business Loan':
            # Add items to the dropdown dynamically
      items_to_add = ['Working capital loan', 'Term loan', 'Equipment financing loans', 'Letter of Credit', 'Loan against property', 'Point-of-Sale (POS) Loans', 'Invoice financing loans', 'Business overdraft', 'Business loans under government schemes']
      self.drop_down_5.items = items_to_add  

  
    
   
