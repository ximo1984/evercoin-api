import requests
import json

class Evercoin:
	def __init__(self):
		self.api_url = "https://test.evercoin.com/v1/" # When you are ready for production, make sure you obtain your API key by contacting support@evercoin.com and use the production endpoint which is https://api.evercoin.com 
		self.api_key = "" # WRITE YOUR API KEY HERE

	def __get_request(self, url):
		final_url = self.api_url + url
		headers = self.__headers()
		response = requests.get(final_url, headers=headers)

		return response.json()

	def __post_request(self, url, message):
		final_url = self.api_url + url
		headers = self.__headers()
		serialized_data = json.dumps(message)
		response = requests.post(final_url, headers=headers, data=serialized_data)
		
		return response.json()

	def __headers(self):
		evercoin_headers = {"evercoin-api-key": self.api_key, 'Content-type': 'application/json'}
		return evercoin_headers

	def limit(self, deposit_coin, destination_coin):
		url = "limit/" + deposit_coin + "-" + destination_coin
		response = self.__get_request(url)

		return response

	def validate(self, coin, address):
		url = "validate/" + deposit_coin + "/" + destination_coin
		response = self.__get_request(url)

		return response

	def getCoins(self):
		url = "coins"
		response = self.__get_request(url)

		return response

	def getPrice(self, deposit_coin, destination_coin, deposit_amount, destination_amount=None):
		url = "price"
		message = {"depositCoin": deposit_coin, "destinationCoin": destination_coin}
		
		if destination_amount is None:
			message["depositAmount"] = deposit_amount
		else:
			message["destinationAmount"] = destination_amount

		response = self.__post_request(url, message)

		return response

	def createOrder(self, deposit_coin, refund_address, deposit_amount, destination_coin, destination_address, destination_amount, signature):
		url = "order"
		message = {
			"depositCoin":deposit_coin,
			"refundAddress":refund_address,
			"depositAmount": deposit_amount,
			"destinationCoin": destination_coin,
			"destinationAddress": destination_address,			
			"destinationAmount": destination_amount,
			"signature":signature
		}

		response = self.__post_request(url, message)

		return response

	def getStatusOrder(self, order_id):
		url = "status/" + order_id
		respones = self.__get_request(url)

		return response
