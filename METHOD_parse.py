##########################################################
from idlelib.autocomplete_w import LISTUPDATE_SEQUENCE
from INFORMATION_logger import get_logger

# Initialize logger
logger = get_logger('parser')

def Parse(data,
          key_main,
          key_name,
          key_id):

	logger.debug(f"Parsing data with keys: main={key_main}, name={key_name}, id={key_id}")

	try:
		List_A = []
		List_B = []

		for number in range(len(data[key_main])):
			name = data[key_main][number][key_name].strip()#name
			id_ = data[key_main][number][key_id].strip()#id

			List_A.append(name)
			List_B.append(id_)

		logger.debug(f"Successfully parsed {len(List_A)} items")
		return List_A, List_B
		
	except KeyError as e:
		logger.error(f"Missing key in data: {str(e)}")
		raise

	except Exception as e:
		logger.error(f"Failed to parse data: {str(e)}")
		raise

##########################################################

def Parse_2(data,
            key_main,
            key_name):

	logger.debug(f"Parsing data with keys: main={key_main}, name={key_name}")

	try:
		List_A = []
		List_B = []

		for number in range(len(data[key_main])):
			user_name = data[key_name].strip()#user name 
			user_id = data[key_main]#user id

			List_A.append(user_name)
			List_B.extend(user_id)

		List_C = set(List_B)#drop the duplicates
		List_D = list(List_C)#convert back to list

		logger.debug(f"Successfully parsed {len(List_A)} items, {len(List_D)} unique IDs")
		return List_A, List_D#user name list, user id list
		
	except KeyError as e:
		logger.error(f"Missing key in data: {str(e)}")
		raise

	except Exception as e:
		logger.error(f"Failed to parse data: {str(e)}")
		raise

def Parse_3(data,
            key_main_cards,
            key_active,
            key_user_id,
            key_card_id):

	logger.debug(f"Parsing card data with keys: main_cards={key_main_cards}, active={key_active}, user_id={key_user_id}, card_id={key_card_id}")

	try:
		user_id_A = None #assingning the None value because you cannot return nothing
		card_id_A = None #assingning the None value because you cannot return nothing

		for number in range(len(data[key_main_cards])): #Essential for offsetting the range

			if data[key_main_cards] and data[key_main_cards][0][key_active] == False: #if data["cards"] exists and data["cards"][0]["active"] equals False

				user_id_A = data[key_user_id] #user ids with a card that is NOT active
				card_id_A = data[key_main_cards][0][key_card_id] #ids of INACTIVE cards

		logger.debug(f"Parsed card data - user_id: {user_id_A}, card_id: {card_id_A}")
		return user_id_A, card_id_A
		
	except KeyError as e:
		logger.error(f"Missing key in card data: {str(e)}")
		raise

	except Exception as e:
		logger.error(f"Failed to parse card data: {str(e)}")
		raise



