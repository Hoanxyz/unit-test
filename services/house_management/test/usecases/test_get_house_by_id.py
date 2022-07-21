from services.house_management.presentation.apis.get_house import get_house_by_id
from services.house_management.data.dao.house_dao import HouseDAO


async def test_get_house_by_id():
    
    assert HouseDAO.from_json({
            'owner_id': 1,
            'country': 'Viet Nam',
            'city': 'Ha Noi',
            'district': 'Cau Giay',
            'address_detail': 'Duong Dinh Nghe',
            'note': 'my note',
            'house_status': 1,
            'house_type_id': 1
        })