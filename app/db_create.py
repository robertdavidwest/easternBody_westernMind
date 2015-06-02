# db_create.py

from oauth2client.client import SignedJwtAssertionCredentials
import json
import gspread

from views import db
from models import ChakraAttribute

def get_oath_credentials(json_key):
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = SignedJwtAssertionCredentials(json_key['client_email'],
                                            json_key['private_key'], scope)
    return credentials


if __name__ == '__main__':
    # create the database and the db table
    db.create_all()

    # get data from google sheets
    json_key = json.load(open('../easternBody-westernMind-c7c15d12b616.json'))
    gc = gspread.authorize(get_oath_credentials(json_key))
    worksheet = gc.open("Chakra Template").worksheet('Chakra Attributes')
    data = worksheet.get_all_values()

    # add data to database table
    for i, row in enumerate(data):
        if i == 0:
            assert(row[0] == 'Chakra')
            assert(row[1] == 'Attribute Type')
            assert(row[2] == 'Attribute Description')
            assert(row[3] == 'Attribute Description Detail')
        else:
            row_obj = ChakraAttribute(chakra_number=row[0],
                                      attribute_type=row[1],
                                      attribute_description=row[2],
                                      attribute_detail=row[3])

            db.session.add(row_obj)


    # commit the changes
    db.session.commit()