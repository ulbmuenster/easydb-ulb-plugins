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
	# get a logger
	logger = easydb_context.get_logger('ulb.pre_update')
	logger.info("pre_update called via ulb plugin")

	# get the object data
	data = get_json_value(easydb_info, "data")
	logger.debug("%d Objects" % len(data))

	# check the data, and if there is invalid data, throw an InvalidValueError
	for i in range(len(data)):

		# check if the objecttype is set
		if "_objecttype" not in data[i]:
			continue

		# check if the objecttype is correct
		if data[i]["_objecttype"] != "formula":
			formula = data[i]["ztest"]["mineralogische_formeln"]
			# replace variations for Multiplication sign
			formula = formula.replace('*', '·')

			# set map for superstring and substring
			SUB = string.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
			SUP = string.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

			# set variables
			multiplicator = False
			convertedFormula = ''

			for i in range(len(formula)):
				if formula[i] == '·':
					multiplicator = True
				if formula[i].isalpha():
					multiplicator = False
				if formula[i].isdigit and not multiplicator:
					# handle free ions / charge
					if formula[i] == '+':
						convertedFormula = convertedFormula[:-1]
						convertedFormula = convertedFormula + formula[i-1].translate(SUP)
						convertedFormula = convertedFormula + "⁺"
					# handle number of atoms
					else:
						convertedFormula = convertedFormula + formula[i].translate(SUB)
				else:
					convertedFormula = convertedFormula + formula[i]
			else:
				logger.debug(json.dumps(json_data))
		# to avoid confusion with masks and read/write settings in masks, always use the _all_fields mask
		data[i]["_mask"] = "_all_fields"

		# only write formula if field is empty
		if get_json_value(data[i], "ztest.mineralogische_formeln") is None:
			try:
				data[i]["ztest"]["mineralogische_formeln"] = convertedFormula
			except:
				logger.debug("Problem saving formula: " + convertedFormula +
							 " at object " + get_json_value(data[i], "ztest._id"))
	# always return if no exception was thrown, so the server and frontend are not blocked
	print(json.dumps(data, indent=4))
	return data
