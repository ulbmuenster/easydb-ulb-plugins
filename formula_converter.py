# coding=utf8

import os
import json
import yaml
import requests

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import string

from datetime import datetime, date
import calendar
import locale
from dateutil.relativedelta import relativedelta

from time import sleep
from threading import Thread

from context import EasydbException
from context import InvalidValueError
from context import get_json_value




# called from easydb
def easydb_server_start(easydb_context):
	# called when server starts (just once)
	logger = easydb_context.get_logger('ulb')
	logger.debug('registering ulb plugin')

	# api callbacks that extend the api
	easydb_context.register_callback(
		'db_pre_update', {'callback': 'pre_update'})


# method for the 'db_pre_update' callback
def pre_update(easydb_context, easydb_info):
	convertedFormula = ''
	#datamodel/"Datenmodell"
	datamodel = "fb14_basis_dm_1"
	# get a logger
	logger = easydb_context.get_logger('ulb.pre_update')
	logger.info("pre_update called via formula_converter plugin")

	# get the object data
	data = get_json_value(easydb_info, "data")
	logger.debug("%d Objects" % len(data))

	# check the data, and if there is invalid data, throw an InvalidValueError
	for i in range(len(data)):
		# check if datamodel is in data
		if datamodel not in data[i]:
			continue
		# check if formel is in mineralogie
		if "formel" not in data[i][datamodel]:
			continue

		formula = data[i][datamodel]["formel"]
		url = "https://easydbwebservice/convert"
		result = requests.post(url=url, json={"formula": formula})
		json_data = result.json()
		if "convertedFormula" in json_data:
			convertedFormula = json_data["convertedFormula"]
		else:
			logger.debug(json.dumps(json_data))
		# to avoid confusion with masks and read/write settings in masks, always use the _all_fields mask
		data[i]["_mask"] = "_all_fields"
		try:
			data[i][datamodel]["formel"] = convertedFormula
		except:
			logger.debug("Problem saving formula: " + convertedFormula)
	# always return if no exception was thrown, so the server and frontend are not blocked
	print(json.dumps(data, indent=4))
	return data
