from os import add_dll_directory
from pprint import pprint as pretty

from METHOD_parse import Parse_2, Parse_3
from METHOD_requests import Request_GET, Request_POST, Request_PUT
from INFORMATION_logger import get_logger
import json
from random import randint
from ESSENTIAL_values import *

# Initialize logger
logger = get_logger('functions')

##########################################################

def func_RETURN_DIFFERENCE_3(List_A,
                             List_B,
                             target):
	
	#This is saying for g_name and g_id which is LIST1 and LIST2 keep the pair in the
	# list if one of them starts with the target
	List_C, List_D = zip(*[(g_name, g_id) for g_name, g_id

	                       in zip(List_A, List_B)

	                       if g_name.startswith(target)

	                       ])

	return List_C, List_D  #group name list, group id list

##########################################################

def func_RETURN_DIFFERENCE_2(List_A,
                             List_B,
                             target):
	
	(List_C, List_D) = zip(*[(name_, id_) for name_, id_

	                         in zip(List_A, List_B)

	                         if name_ not in target

	                         ])

	return List_C, List_D  #user name list, user id list

##########################################################

def func_RETURN_DIFFERENCE_1(List_A,
                             List_B,
                             target):


	(List_C, List_D) = zip(*[(name_, id_) for name_, id_

	                         in zip(List_A, List_B)

	                         if name_ in target

	                         ])



	return List_C, List_D  #user name list, user id list

##########################################################

def func_RETURN_DIFFERENCE_0(List_B,
                             List_A):
	
	List_diff = [

		something for something

		in List_B

		if something not in List_A

	]

	return List_diff

##########################################################

def func_GET_FULLNAME_LIST():
	logger.debug("Extracting full names from CSV data")
	
	List_A = []

	try:
		for group in vendor_groups:  #list of vendor groups in csv
			logger.debug(f"Processing group: {group}")

			List_B = df[df[f"{group_column}"] == group]["FIRST_NAME"].dropna().str.strip().tolist()  #first name list
			List_C = df[df[f"{group_column}"] == group]["LAST_NAME"].dropna().str.strip().tolist()  #last name list

			logger.debug(f"Found {len(List_B)} users in group {group}")

			for first_name, last_name in zip(List_B, List_C):  #looping with first name and last name at same time
				List_A.append(first_name + " " + last_name)  #full name list. combining the names into a usable list (space between them)

		logger.info(f"Successfully extracted {len(List_A)} full names from CSV")
		return List_A  #list of vendor users in csv
		
	except Exception as e:
		logger.error(f"Failed to extract full names from CSV: {str(e)}")
		raise

##########################################################

def func_GET_GROUP_USERID_LIST(List_A,
                               data_token,
                               URL):
	
	List_A = []

	List_B = []

	for group_id in List_A:
		URL = f"{URL}{group_id}"

		data = Request_GET(URL,
		                   data_token)

		List_C, List_D = Parse_2(data, "user_ids", "name")  #GROUP NAME LIST, USER ID LIST

		List_A.append(List_C)  #GROUP NAME LIST

		List_B.extend(List_D)  #USER ID LIST

	return List_A, List_B

##########################################################

def func_GET_GROUP_USERIDList_B(URL,
                                List_D,
                                data_token):
	
	List_A = []

	List_B = []

	for group_id in List_D:  # vendor groups id list in verkada

		URL = f"{URL}{group_id}"

		data = Request_GET(URL, data_token)

		List_C, List_D = Parse_2(data, "user_ids", "name")  # group name list, user id list

		List_A.append(List_C)  # group name list

		List_B.extend(List_D)  # user id list

	return List_A, List_B  # group name list, user id list

##########################################################

def func_SPLIT_NAMELIST(List_C):
	
	List_A = []

	List_B = []

	for names in List_C:  #full name list

		splitter = names.split()  #splitting the fullname into indexes

		List_A.append(splitter[0])  #first name list

		List_B.append(splitter[1])  #last name list

	return List_A, List_B  #first name list, last name list

##########################################################

def func_CREATE_ACCESS_GROUP(List_A,
                             data_token,
                             api_key,
                             URL):
	logger.debug(f"Creating {len(List_A)} access groups")
	
	try:
		for group_name in List_A:
			logger.debug(f"Creating access group: {group_name}")
			PAYLOAD = json.dumps(
				{"name": group_name}
			)

			Request_POST(URL, data_token, api_key, PAYLOAD)
			logger.debug(f"Successfully created access group: {group_name}")
			
		logger.info(f"Successfully created all {len(List_A)} access groups")
		
	except Exception as e:
		logger.error(f"Failed to create access groups: {str(e)}")
		raise

##########################################################

def func_CREATE_VERKADA_USERS(List_A,
                              List_B,
                              URL,
                              email_fake,
                              start,
                              end,
                              emaiL_fake_domain,
                              data_token,
                              api_key):
	logger.debug(f"Creating {len(List_A)} Verkada users")
	
	try:
		for first_name, last_name in zip(List_A, List_B):  #firstname list, last name list
			email = email_fake + f"{randint(start, end)}" + f"{emaiL_fake_domain}"
			logger.debug(f"Creating user: {first_name} {last_name} with email: {email}")

			PAYLOAD = json.dumps(
				{
					"email": email,
					"first_name": first_name,
					"last_name": last_name
				}
			)

			Request_POST(URL, data_token, api_key, PAYLOAD)
			logger.debug(f"Successfully created user: {first_name} {last_name}")
			
		logger.info(f"Successfully created all {len(List_A)} Verkada users")
		
	except Exception as e:
		logger.error(f"Failed to create Verkada users: {str(e)}")
		raise

##########################################################

def func_ADD_ACCESS_USERS_TO_GROUP(List_A,
                                   List_B,
                                   List_C,
                                   List_D,
                                   List_E,
                                   data_token):
	
	for group_name, group_id in zip(List_A, List_B):  #group name list, group id list

		for user_name, user_id in zip(List_C, List_D):  #user full name list, user id list

			URL = f"https://api.verkada.com/access/v1/access_groups/group?group_id={group_id}"

			PAYLOAD = json.dumps(
				{"user_ids": [user_id]}
			)

			Request_POST(URL, data_token, List_E, PAYLOAD)

##########################################################

def func_GET_ACCESS_USERS_WITH_DEACTIVATED_CARDS(URL_A,
                                                 List_D,
                                                 data_token):  #Returning access user with deactivated cards

	List_A = []
	List_B = []

	for user_id_A in List_D:  # user id list

		URL_B = f"{URL_A}{user_id_A}"

		data = Request_GET(URL_B,
		                   data_token)

		List_C, List_E = Parse_3(data,
		                         "cards",
		                         "active",
		                         "user_id",
		                         "card_id")

		if List_C is None or List_E is None: #used to prevent None from being added to the list
			continue

		List_A.append(List_C)  # list users ids with inactive cards
		List_B.append(List_E)  # list card ids that are inactive

	if not List_A: #if list_B returns nothing do this

		pretty("There are no INACTIVE Keycards")


	else: #the else here represents the opposite of the "if not" if something is returned do this
		pretty("The following users have INACTIVE Keycards")
		pretty(List_A)

	return List_A, List_B

##########################################################

def func_ACTIVATE_ACCESS_CARD(URL,
                              data_token,
                              List_A,
                              List_B):
	
	for user_name, user_id in zip(List_A, List_B):  # full name list, user id list

		URL = f"{URL}{user_id}"

		PAYLOAD = json.dumps(
			{"status": "active"}
		)

		Request_PUT(URL,
		            data_token,
		            PAYLOAD)
