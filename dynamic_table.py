import boto3


def get_dynamo_table(table_name):
    ddb = boto3.resource('dynamodb')
    return ddb.Table(table_name)


def create_product(category, sku, **item):
    table = get_dynamo_table('CSV-log-leveling')
    keys = {
        'log-level': category,
        'message': sku,
    }
    item.update(keys)
    table.put_item(Item=item)
    return table.get_item(Key=keys)['Item']


def dynamic(to_make):
    with open(to_make, "r") as file:
        for line in file:
            filling = line.split('|')
            product = create_product(filling[0], filling[1], details=filling[2], source_application=filling[3])
