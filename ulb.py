# coding=utf8

import os
import json
import yaml
import requests

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
    # get a logger
    logger = easydb_context.get_logger('ulb.pre_update')
    logger.info("pre_update called via ulb plugin")

    url = "http://example.com"  # TODO insert url of invnr service here
    jsonwebtoken = "naaaa"  # TODO insert valid jwt here
    try:
        result = requests.post(url=url, headers={
                               'Authorization': 'Bearer '+jsonwebtoken}, json={"institution": "ABC", "prefix": "cfg"})  # TODO configure prefix
        json_data = result.json()
        if "invnr" in json_data:
            inventarnummer = json_data["invnr"]
        else:
            logger.debug(json.dumps(json_data))
    except requests.exceptions.ConnectionError:
        logger.debug("Exception")

    # get the object data
    data = get_json_value(easydb_info, "data")
    logger.debug("%d Objects" % len(data))

    # check the data, and if there is invalid data, throw an InvalidValueError
    for i in range(len(data)):

        # check if the objecttype is set
        if "_objecttype" not in data[i]:
            continue

        # check if the objecttype is correct
        if data[i]["_objecttype"] != "ztest":
            logger.debug("Ignoring object type %s" % data[i]["_objecttype"])
            continue

        # to avoid confusion with masks and read/write settings in masks, always use the _all_fields mask
        data[i]["_mask"] = "_all_fields"

        # only write invnr if field is empty
        if get_json_value(data[i], "ztest.invnr") is None:
            try:
                data[i]["ztest"]["invnr"] = inventarnummer
            except:
                logger.debug("Problem generating invnr: " + inventarnummer +
                             " at object " + get_json_value(data[i], "ztest._id"))

    # always return if no exception was thrown, so the server and frontend are not blocked
    print json.dumps(data, indent=4)
    return data
