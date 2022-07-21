from services.house_management.presentation.apis.create_house import create_house
from services.house_management.data.dao.house_dao import HouseDAO

async def create_house():
    # Access to db here to create house then return new house json object
    return HouseDAO.from_json({
        'owner_id': 1,
        'country': 'Viet Nam',
        'city': 'HCM',
        'district': 'Quan 7',
        'address_detail': 'Ba Trieu',
        'note': 'my note',
        'house_status': 1,
        'house_type_id': 1
    })