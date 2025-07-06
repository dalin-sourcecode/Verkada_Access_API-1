###############################################

import argparse
from METHOD_requests import Request_Token_POST
from ESSENTIAL_values import *
from METHOD_func import func_GET_FULLNAME_LIST
from METHOD_controller import VERKADA_API
from INFORMATION_logger import get_logger
import pprint

# Initialize logger
logger = get_logger('main')

###############################################

def main():
	parser = argparse.ArgumentParser(description='VERKADA API Operations')
	parser.add_argument('action', choices=[
		'list-groups',
		'list-users', 
		'deactivated-cards',
		'reactivate-cards',
		'compare-groups',
		'compare-users',
		'create-groups',
		'create-users',
		'add-users-to-groups'
	], help='Action to perform')
	
	args = parser.parse_args()
	
	logger.info(f"Starting VERKADA API operation: {args.action}")
	
	try:
		# Initialize API connection
		logger.debug("Requesting authentication token")
		data_token = Request_Token_POST(url, api_key)
		logger.info("Successfully obtained authentication token")
		
		logger.debug("Loading vendor users from CSV")
		vendor_users_full_names = func_GET_FULLNAME_LIST()
		logger.info(f"Loaded {len(vendor_users_full_names)} vendor users from CSV")
	
		logger.debug("Initializing VERKADA API controller")
		class_0 = VERKADA_API(
			token_url,
			api_key,
			vendor_groups,
			vendor_users_full_names,
			email_fake,
			emaiL_fake_domain,
			email_random_number_start,
			email_random_number_end,
			df,
			group_column,
			data_token
		)
		logger.info("VERKADA API controller initialized successfully")
		
		# Execute the requested action
		logger.debug(f"Executing action: {args.action}")
		if args.action == 'list-groups':
			INSTANCE_GET_ACCESS_GROUPS_list(class_0)
		elif args.action == 'list-users':
			INSTANCE_get_the_users(class_0)
		elif args.action == 'deactivated-cards':
			INSTANCE_get_deactivated_cards(class_0)
		elif args.action == 'reactivate-cards':
			INSTANCE_reactivate_cards(class_0)
		elif args.action == 'compare-groups':
			INSTANCE_compare_the_groups(class_0)
		elif args.action == 'compare-users':
			INSTANCE_compare_the_users(class_0)
		elif args.action == 'create-groups':
			INSTANCE_groups_create(class_0)
		elif args.action == 'create-users':
			INSTANCE_users_create(class_0)
		elif args.action == 'add-users-to-groups':
			INSTANCE_users_add_vendors_to_group(class_0)
		
		logger.info(f"Successfully completed operation: {args.action}")
		
	except Exception as e:
		logger.error(f"Error during operation '{args.action}': {str(e)}", exc_info=True)
		raise

##########################################################################

def INSTANCE_GET_ACCESS_GROUPS_list(class_0):
	logger.info("Retrieving all access groups from Verkada")
	LIST_1, _ = class_0.obj_GET_ACCESS_GROUPS_ALL()#group names list
	logger.info(f"Found {len(LIST_1)} access groups")
	pprint.pprint(LIST_1)

def INSTANCE_get_the_users(class_0):
	logger.info("Retrieving all users from Verkada")
	print("CURRENT USERS IN VERKADA:")
	UG, _, _ = class_0.obj_GET_ACCESS_USERS()
	logger.info(f"Found {len(UG)} users")
	pprint.pprint(UG)

def INSTANCE_get_deactivated_cards(class_0):
	logger.info("Retrieving users with deactivated cards")
	class_0.obj_GET_ACCESS_USERS_WITH_DEACTIVATED_CARDS()

def INSTANCE_reactivate_cards(class_0):
	logger.info("Reactivating access cards")
	class_0.obj_ACTIVATE_ACCESS_CARD()

def INSTANCE_compare_the_groups(class_0):
	logger.info("Comparing groups between CSV and Verkada")
	class_0.COMPARE_ACCESS_GROUPS_printout()

def INSTANCE_groups_create(class_0):
	logger.info("Creating missing access groups")
	class_0.obj_CREATE_ACCESS_GROUP()

def INSTANCE_compare_the_users(class_0):
	logger.info("Comparing users between CSV and Verkada")
	class_0.COMPARE_ACCESS_USERS_printout()

def INSTANCE_users_create(class_0):
	logger.info("Creating missing users")
	class_0.obj_CREATE_VERKADA_USERS()

def INSTANCE_users_add_vendors_to_group(class_0):
	logger.info("Adding users to access groups")
	class_0.obj_ADD_ACCESS_USERS_TO_GROUP()

##########################################################################

if __name__ == "__main__":
	main() 