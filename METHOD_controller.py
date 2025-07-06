#######################################

import pprint
from METHOD_requests import Request_GET
from METHOD_parse import Parse
from METHOD_func import (
	func_GET_GROUP_USERID_LIST, func_RETURN_DIFFERENCE_0, func_SPLIT_NAMELIST,
	func_CREATE_ACCESS_GROUP, func_CREATE_VERKADA_USERS, func_RETURN_DIFFERENCE_1,
	func_RETURN_DIFFERENCE_2, func_ADD_ACCESS_USERS_TO_GROUP, func_RETURN_DIFFERENCE_3,
	func_GET_GROUP_USERIDList_B, func_GET_ACCESS_USERS_WITH_DEACTIVATED_CARDS,
	func_ACTIVATE_ACCESS_CARD
)
from INFORMATION_logger import get_logger

# Initialize logger
logger = get_logger('controller')


#######################################

class VERKADA_API:

	def __init__(self,
	             token_url,
	             api_key,

	             vendor_groups_in_csv,  #list of vendor groups in csv
	             vendor_users_full_names_in_csv,  #list of vendor users in csv

	             email_fake,
	             emaiL_fake_domain,
	             email_random_number_start,
	             email_random_number_end,

	             df,

	             group_column,

	             data_token
	             ):

		logger.debug("Initializing VERKADA_API controller")
		
		self.token_url = token_url
		self.api_key = api_key

		self.vendor_groups_in_csv = vendor_groups_in_csv
		self.vendor_users_full_names_in_csv = vendor_users_full_names_in_csv

		self.email_fake = email_fake
		self.emaiL_fake_domain = emaiL_fake_domain
		self.start = email_random_number_start
		self.end = email_random_number_end

		self.df = df

		self.group_column = group_column

		self.data_token = data_token
		
		logger.info(f"VERKADA_API controller initialized with {len(vendor_groups_in_csv)} groups and {len(vendor_users_full_names_in_csv)} users")

	##########################################################################

	def obj_GET_ACCESS_GROUPS_ALL(self):
		#returning a list of the Group names and Group IDs
		logger.debug("Retrieving all access groups from Verkada")

		URL = "https://api.verkada.com/access/v1/access_groups"

		try:
			DATA = Request_GET(URL, self.data_token)
			List_A, List_B = Parse(DATA, "access_groups", "name", "group_id")  #group name list, group id list
			
			logger.info(f"Successfully retrieved {len(List_A)} access groups")
			return List_A, List_B  #group name list, group id list
			
		except Exception as e:
			logger.error(f"Failed to retrieve access groups: {str(e)}")
			raise

	def obj_GET_ACCESS_GROUPS_MEMBERS(self, LIST_0):  #group id list

		URL = "https://api.verkada.com/access/v1/access_groups/group?group_id="

		List_A, List_B = func_GET_GROUP_USERID_LIST(LIST_0, self.data_token, URL)  #group name list, user id list

		List_C = set(List_B)  #using set to drop the duplicates

		List_D = list(List_C)  #using list to reset the set to a list

		return List_A, List_D  #group name list, user id list without duplicates

	##########################################################################

	def obj_GET_ACCESS_USERS(self):  #Returning the user's full name and User ID
		logger.debug("Retrieving all access users from Verkada")

		URL = "https://api.verkada.com/access/v1/access_users"

		try:
			DATA = Request_GET(URL, self.data_token)
			List_A, List_B = Parse(DATA, "access_members", "full_name", "user_id")  #full name list, user id list
			
			logger.info(f"Successfully retrieved {len(List_A)} access users")
			return List_A, List_B, DATA  #full name list, user id list
			
		except Exception as e:
			logger.error(f"Failed to retrieve access users: {str(e)}")
			raise

	##########################################################################

	def COMPARE_ACCESS_GROUPS_printout(self):
		#OUT OF THE GROUPS THAT YOU ARE TRYING TO ADD, WHICH ARE NOT IN VERKADA
		logger.debug("Comparing access groups between CSV and Verkada")
		
		try:
			missing_groups = self.obj_COMPARE_ACCESS_GROUPS_VS_CSV()
			
			if not missing_groups:  #if nothing is returned
				logger.info("All vendor groups are identical between CSV and Verkada")
				print("ALL VENDOR GROUPS ARE IDENTICAL")
			else:
				logger.info(f"Found {len(missing_groups)} groups in CSV that are not in Verkada")
				print("THESE GROUPS ARE NOT IN VERKADA")
				pprint.pprint(missing_groups)
				
		except Exception as e:
			logger.error(f"Failed to compare access groups: {str(e)}")
			raise

	##########################################################################

	def obj_COMPARE_ACCESS_GROUPS_VS_CSV(self):
		logger.debug("Comparing groups in CSV vs groups in Verkada")

		try:
			List_A, _ = self.obj_GET_ACCESS_GROUPS_ALL()  #list of groups that are in verkada
			logger.debug(f"Groups in Verkada: {List_A}")

			List_B = self.vendor_groups_in_csv  #list of groups in the CSV
			logger.debug(f"Groups in CSV: {List_B}")

			List_C = func_RETURN_DIFFERENCE_0(List_B, List_A)  #list of groups in csv that are not in verkada
			logger.debug(f"Missing groups: {List_C}")

			return List_C  #list of groups in csv that are not in verkada
			
		except Exception as e:
			logger.error(f"Failed to compare groups: {str(e)}")
			raise

	##########################################################################

	def obj_COMPARE_ACCESS_USERS_VS_CSV(self):

		_, _, DATA = self.obj_GET_ACCESS_USERS()

		List_A, List_B = Parse(DATA, "access_members", "full_name", "user_id")  #full name list, user id list

		List_B = func_RETURN_DIFFERENCE_0(self.vendor_users_full_names_in_csv,
		                                  List_A)  #list of users in csv but not in verkada

		List_C, List_D = func_SPLIT_NAMELIST(List_B)  #firstname list, lastname list

		return List_C, List_D  #firstname list, lastname list

	##########################################################################

	def COMPARE_ACCESS_USERS_printout(self):
		logger.debug("Comparing access users between CSV and Verkada")
		
		try:
			missing_users = self.obj_COMPARE_ACCESS_USERS_VS_CSV()
			
			if missing_users == ([], []):
				logger.info("All vendor users are identical between CSV and Verkada")
				print("ALL VENDOR USERS ARE IDENTICAL")
			else:
				logger.info(f"Found {len(missing_users[0])} users in CSV that are not in Verkada")
				print("THESE USERS ARE NOT IN VERKADA")
				pprint.pprint(missing_users)
				
		except Exception as e:
			logger.error(f"Failed to compare access users: {str(e)}")
			raise

	##########################################################################

	def obj_CREATE_ACCESS_GROUP(self):
		logger.debug("Creating missing access groups")

		try:
			List_A = self.obj_COMPARE_ACCESS_GROUPS_VS_CSV()  #list of groups in csv that are not in verkada
			
			if not List_A:
				logger.info("No groups to create - all groups already exist")
				return

			URL = "https://api.verkada.com/access/v1/access_groups/group"
			logger.info(f"Creating {len(List_A)} access groups")

			func_CREATE_ACCESS_GROUP(List_A, self.data_token, self.api_key, URL)
			logger.info("Successfully created all missing access groups")
			
		except Exception as e:
			logger.error(f"Failed to create access groups: {str(e)}")
			raise

	##########################################################################

	def obj_CREATE_VERKADA_USERS(self):
		logger.debug("Creating missing Verkada users")

		try:
			List_A, List_B = self.obj_COMPARE_ACCESS_USERS_VS_CSV()  #firstname list, lastname list = users in csv that are not in verkada
			
			if not List_A or not List_B:
				logger.info("No users to create - all users already exist")
				return

			URL = "https://api.verkada.com/core/v1/user"
			logger.info(f"Creating {len(List_A)} Verkada users")

			func_CREATE_VERKADA_USERS(List_A,
			                          List_B,
			                          URL,
			                          self.email_fake,
			                          self.start,
			                          self.end,
			                          self.emaiL_fake_domain,
			                          self.data_token,
			                          self.api_key)

			logger.info("Successfully created all missing Verkada users")
			
		except Exception as e:
			logger.error(f"Failed to create Verkada users: {str(e)}")
			raise

	##########################################################################

	def obj_ADD_ACCESS_USERS_TO_GROUP(self):

		List_A, List_B, _ = self.obj_GET_ACCESS_USERS()  #full name list, user id list

		List_C, List_D = func_RETURN_DIFFERENCE_1(List_A, #full name list, user id list of names in verkada that match csv
		                                          List_B,
		                                          self.vendor_users_full_names_in_csv)

		##################################################################

		List_E, List_F = self.obj_GET_ACCESS_GROUPS_ALL()  #group name list, group id list

		List_G, List_H = func_RETURN_DIFFERENCE_1(List_E, #group name list, group id list in verkada that match csv
		                                          List_F,
		                                          self.vendor_groups_in_csv)

		##################################################################

		_, List_i = self.obj_GET_ACCESS_GROUPS_MEMBERS(
			List_H)  #group names list, user ids (these users are currently in groups)

		List_J, List_K = func_RETURN_DIFFERENCE_2(List_C, #user full name list, user id list (these users are not in groups yet)
		                                          List_D,
		                                          List_i)

		##################################################################

		func_ADD_ACCESS_USERS_TO_GROUP(List_G,
		                               List_H,
		                               List_J,
		                               List_K,
		                               List_F,
		                               self.data_token)

	##########################################################################

	def obj_GET_ACCESS_GROUP_MEMBERS(self):  #returning list of vendor groups in verkada

		List_A, List_B = self.obj_GET_ACCESS_GROUPS_ALL()  # group name list, group id list = all groups not just vendors

		List_C = "VAC | VENDOR"  #target prefix for the vendor name, this is what it will start with

		List_D, List_E = func_RETURN_DIFFERENCE_3(List_A, #vendor group name list, vendor group id list, target prefix
		                                          List_B,
		                                          List_C)

		return List_E  #vendor group id list

	##########################################################################

	def obj_GET_ACCESS_GROUP_MEMBERS_USER_IDS(self):  #returning verkada groups and user ids in the groups

		#FINDING THE USER ID'S FOR THE USERS IN THE FILTERED GROUPS

		List_A = self.obj_GET_ACCESS_GROUP_MEMBERS()  #vendor group id list

		URL = f"https://api.verkada.com/access/v1/access_groups/group?group_id="

		List_B, List_C = func_GET_GROUP_USERIDList_B(URL, #group name list, user ids in the groups list
		                                             List_A,
		                                             self.data_token)

		return List_B, List_C  #group name list, user ids in the groups list

	##########################################################################

	def obj_GET_ACCESS_USERS_WITH_DEACTIVATED_CARDS(self):

		List_A, List_B, _ = self.obj_GET_ACCESS_USERS()  #full name list, user id list

		List_C, List_D = func_RETURN_DIFFERENCE_1(List_A, #full name list, user id list of names in verkada that match csv
		                                          List_B,
		                                          self.vendor_users_full_names_in_csv)

		URL = f"https://api.verkada.com/access/v1/access_users/user?user_id="

		List_A, List_B = func_GET_ACCESS_USERS_WITH_DEACTIVATED_CARDS(URL,
		                                                              List_D,
		                                                              self.data_token)

		return List_A, List_B

	##########################################################################

	def obj_ACTIVATE_ACCESS_CARD(self):

		List_A, List_B = self.obj_GET_ACCESS_USERS_WITH_DEACTIVATED_CARDS()

		URL = f"https://api.verkada.com/access/v1/credentials/card/activate?user_id="

		func_ACTIVATE_ACCESS_CARD(URL,
		                          self.data_token,
		                          List_A,
		                          List_B)

##########################################################################
