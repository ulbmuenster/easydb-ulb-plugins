# coding=utf8
import json
import logging

from context import get_json_value


def easydb_server_start(easydb_context):
    easydb_context.register_callback('db_pre_update', {'callback': 'convert'})

    logging.basicConfig(filename="/var/tmp/formula_converter.log", level=logging.DEBUG)
    logging.info("Loaded formula converter.")


def convert(easydb_context, easydb_info):
    try:
        # datamodel/"Datenmodell"
        datamodel = "fb14_basis_dm_1"

        # get a logger
        logger = easydb_context.get_logger('ulb.convert')
        logger.info("db_pre_update called via formula_converter plugin.")

        # get the object data
        data = get_json_value(easydb_info, "data")
        logger.debug("%d Objects" % len(data))

        # check the data, and if there is invalid data, throw an InvalidValueError
        for i in range(len(data)):

            # check if datamodel is in data
            if datamodel not in data[i]:
                continue

            # check if formel is in datamodel
            if "formel" not in data[i][datamodel]:
                continue

            formula = data[i][datamodel]["formel"]
            # url = "https://easydbwebservice.uni-muenster.de/convert"
            # result = requests.post(url=url, json={"formula": formula})
            # json_data = result.json()

            # replace variations for Multiplication sign
            formula = formula.replace('*', '·')

            # set map for superstring and substring
            sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
            sup = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

            # set variables
            multiplication = False

            # In this we save the converted string.
            converted_formula = ''

            for character in range(len(formula)):
                if formula[character] == '·':
                    multiplication = True
                if formula[character].isalpha():
                    multiplication = False
                if formula[character].isdigit and not multiplication:
                    # handle free ions / charge
                    if formula[character] == '+':
                        converted_formula = converted_formula[:-1]
                        converted_formula = converted_formula + formula[character - 1].translate(sup)
                        converted_formula = converted_formula + "⁺"
                    # handle number of atoms
                    else:
                        converted_formula = converted_formula + formula[character].translate(sub)
                else:
                    converted_formula = converted_formula + formula[character]
            # to avoid confusion with masks and read/write settings in masks, always use the _all_fields mask
            data[i]["_mask"] = "_all_fields"
            try:
                data[i][datamodel]["formel"] = converted_formula
            except Exception:
                logger.debug("Problem saving formula: " + converted_formula)
        # always return if no exception was thrown, so the server and frontend are not blocked
        print(json.dumps(data, indent=4))
        return data
    except Exception as exception:
        logging.error(str(exception))
    finally:
        # "Local variable 'data' might be referenced before assignment" => This try-catch is also in the
        # documentation exactly like this. See: https://docs.easydb.de/en/technical/plugins/ => database callbacks
        return data
