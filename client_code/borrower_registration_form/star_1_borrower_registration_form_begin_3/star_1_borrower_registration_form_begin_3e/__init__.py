from ._anvil_designer import star_1_borrower_registration_form_begin_3eTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_begin_3e(star_1_borrower_registration_form_begin_3eTemplate):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    user_data=app_tables.user_profile.get(customer_id=user_id)
    if user_data:
      self.text_box_1.text=user_data['company_address']
      self.text_box_2.text=user_data['company_landmark']
      self.text_box_3.text=user_data['business_no']
      user_data.update()
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    comp_address = self.text_box_1.text
    landmark = self.text_box_2.text
    business_phone_number = self.text_box_3.text
    user_id = self.userId
    if not comp_address or not landmark or not business_phone_number:
      Notification("please fill the required fields").show()
    else:
      anvil.server.call('add_lendor_individual_form_2',business_phone_number, landmark,comp_address,user_id)
      open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3f',user_id=user_id)


  def button_1_click(self, **event_args):
    open_form('borrower_registration_form.star_1_borrower_registration_form_begin_3.star_1_borrower_registration_form_begin_3d',user_id=self.userId)

  def button_3_click(self, **event_args):
    open_form("bank_users.user_form")
