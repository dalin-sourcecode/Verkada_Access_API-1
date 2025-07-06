############################

import requests
from INFORMATION_logger import get_logger

# Initialize logger
logger = get_logger('requests')

###############################################################################

def Request_GET(url, token):
	logger.debug(f"Making GET request to: {url}")
	
	payload = {

	}

	headers = {
		'accept': 'application/json',
		'x-verkada-auth': f"{token}"
	}

	try:
		response = requests.request("GET", url, headers=headers, data=payload)
		response.raise_for_status()  # Raise exception for bad status codes
		
		data = response.json()
		logger.debug(f"GET request successful, status code: {response.status_code}")
		return data
		
	except requests.exceptions.RequestException as e:
		logger.error(f"GET request failed: {str(e)}")
		raise

	except ValueError as e:
		logger.error(f"Failed to parse JSON response: {str(e)}")
		raise

###############################################################################

def Request_POST(url, token, api_key, payload):
	logger.debug(f"Making POST request to: {url}")
	
	headers = {
		'x-api-key': f'{api_key}',
		'accept': 'application/json',
		'x-verkada-auth': f"{token}",
		'Content-Type': 'application/json'
	}

	try:
		response = requests.request("POST", url, headers=headers, data=payload)
		response.raise_for_status()  # Raise exception for bad status codes
		
		data = response.json()
		logger.debug(f"POST request successful, status code: {response.status_code}")
		return data
		
	except requests.exceptions.RequestException as e:
		logger.error(f"POST request failed: {str(e)}")
		raise

	except ValueError as e:
		logger.error(f"Failed to parse JSON response: {str(e)}")
		raise

###############################################################################

def Request_Token_POST(url, API_KEY):
	logger.debug(f"Requesting authentication token from: {url}")
	
	payload = {

	}

	headers = {
		'x-api-key': API_KEY,
		'Accept': 'application/json'
	}

	try:
		response = requests.request("POST", url, headers=headers, data=payload)
		response.raise_for_status()  # Raise exception for bad status codes
		
		data = response.json()
		
		if "token" not in data:
			logger.error("Token not found in response")
			raise ValueError("Token not found in response")
		
		data_token = data["token"]
		logger.debug("Authentication token obtained successfully")
		return data_token
		
	except requests.exceptions.RequestException as e:
		logger.error(f"Token request failed: {str(e)}")
		raise

	except ValueError as e:
		logger.error(f"Failed to parse token response: {str(e)}")
		raise

###############################################################################

def Request_PUT(url, token, payload):
	logger.debug(f"Making PUT request to: {url}")
	
	headers = {
		'accept': 'application/json',
		'x-verkada-auth': f"{token}",
	}

	try:
		response = requests.request("PUT", url, headers=headers, data=payload)
		response.raise_for_status()  # Raise exception for bad status codes
		
		logger.debug(f"PUT request successful, status code: {response.status_code}")
		return response.status_code
		
	except requests.exceptions.RequestException as e:
		logger.error(f"PUT request failed: {str(e)}")
		raise

###############################################################################
