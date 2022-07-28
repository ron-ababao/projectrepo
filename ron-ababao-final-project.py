import csv
import requests
import logging
from ron_finales import to_gateway

logging.basicConfig(filename="log-file.txt",
                    level=logging.INFO,
                    format='[%(asctime)s]|%(levelname)s|\
                    %(module)s|%(lineno)d|%(message)s',)
log = logging.getLogger()


def process_valid_products(in_file):
    log_level = "WARNING"
    msg = "File will be converted"\
        "to a comma-separated values (CSV) file"
    input_params = api_info(log_level, msg)
    log.warning(msg)
    to_gateway(api_url, input_params)
    headers = None
    valid_products = []

    with open(in_file, newline='') as fh:
        reader = csv.DictReader(fh, fieldnames=headers)
        headers = reader.fieldnames
        for row in reader:
            if row.get('Categories'):
                valid_products.append(row)
    return headers, valid_products


def create_output_file(headers, valid_products):
    out_file = 'cleaned_products.csv'

    if headers and valid_products:
        with open(out_file, 'w', newline='') as fh:
            writer = csv.DictWriter(fh, fieldnames=headers)
            writer.writeheader()
            writer.writerows(valid_products)
    else:
        print('No valid products found!')
    log.critical(f"Output file written in: {out_file}")
    log_level = "CRITICAL"
    msg = "Clean file has been made"
    input_params = api_info(log_level, msg)
    log.info(msg)
    to_gateway(api_url, input_params)


def main(data_file):
    log_level = "ERROR"
    msg = "Just for show. beginning file-ification"
    input_params = api_info(log_level, msg)
    log.error(msg)
    to_gateway(api_url, input_params)
    headers, valid_products = process_valid_products(data_file)
    create_output_file(headers, valid_products)
    


def api_info(loglvl, note):
    parameters = {
        "email": "ron.ababao@globe.com.ph",
        "log_level": loglvl,
        "msg": note,
    }

    return parameters


if __name__ == '__main__':

    api_url = "https://pqrs6ra63b.execute-api.us"\
        "-east-1.amazonaws.com/shinsekaiyori/ron-test"

    data_file_in = 'https://raw.githubusercontent.com/woocommerce\
                /woocommerce/master/sample-data/sample_products.csv'

    log_level = "INFO"
    msg = "Initiating Process"
    input_params = api_info(log_level, msg)
    log.info(msg)
    to_gateway(api_url, input_params)

    data_file_req = requests.get(data_file_in)
    url_content = data_file_req.content
    csv_file = open('raw_file.csv', 'wb').write(url_content)
    data_file = 'raw_file.csv'

    log_level = "DEBUG"
    msg = "Link instantiated"
    input_params = api_info(log_level, msg)
    log.debug(msg)
    to_gateway(api_url, input_params)

    main(data_file)
