# test_simple_unittest.py
import unittest
from services.house_management.data.dao.house_dao import HouseDAO
from services.house_management.data.repository.house_repository_impl import HouseRepositoryImpl


class TestUserService(unittest.TestCase):
        
    def test_get_owner_id(self):
        arg = HouseDAO.from_json({
            'owner_id': 1,
            'country': 'Viet Nam',
            'city': 'HCM',
            'district': 'Quan 7',
            'address_detail': 'Ba Trieu',
            'note': 'my note',
            'house_status': 1,
            'house_type_id': 1,
            'price': 10,
            'special_price': 9
        })
        self.assertEqual(HouseRepositoryImpl.get_owner_id(arg), 1)
        
    def test_get_country(self):
        arg = HouseDAO.from_json({
            'owner_id': 1,
            'country': 'Viet Nam',
            'city': 'HCM',
            'district': 'Quan 7',
            'address_detail': 'Ba Trieu',
            'note': 'my note',
            'house_status': 1,
            'house_type_id': 1,
            'price': 10,
            'special_price': 9
        })
        self.assertEqual(HouseRepositoryImpl.get_owner_id(arg), 'Viet Nam')

if __name__ == '__main__':
    unittest.main(verbosity=2)
