import pandas
import os

# SECURITY: Use environment variable for API key in production
# Set VERKADA_API_KEY environment variable or replace with your actual key
api_key = os.getenv("VERKADA_API_KEY", "YOUR_API_KEY_HERE")

token_url = "https://api.verkada.com/token"

email_fake = "no-email"

email_random_number_start = 0

email_random_number_end = 900

emaiL_fake_domain = "@vendor.com"

group_column = "VENDOR_GROUP"

df = pandas.read_csv("Vendor Employee List.csv", low_memory=False)#dataframe of the vendor employee list

vendor_groups = df[f"{group_column}"].drop_duplicates().dropna().str.strip().tolist()
#['VAC | VENDOR | JANITORIAL', 'VAC | VENDOR | PTM | ABRAM', 'VAC | VENDOR | PTM | NCR', 'VAC | VENDOR | ATM | NCR', 'VAC | VENDOR | ATM | BRINKS']

url = "https://api.verkada.com/token" 