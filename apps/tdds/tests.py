import json
import bcrypt
from django.test.testcases import TestCase
from django.test.client import Client
from tdds.models import Role, User


class TestUser(TestCase):
    def setUp(self):
        self.client = Client()
        
        role1 = Role.objects.create(id=1, name="admin1")
        role2 = Role.objects.create(id=2, name="normal1")
        
        User.objects.create(role=role1, nickname='kylee1', password=bcrypt.hashpw("1234".encode('utf-8'), bcrypt.gensalt()))
        User.objects.create(role=role2, nickname='kylee2', password=bcrypt.hashpw("1234".encode('utf-8'), bcrypt.gensalt()))
    
    
    def tearDown(self):
        Role.objects.all().delete()
        User.objects.all().delete()
        
    
    def test_success_create_user(self):
        
        data = {

            "role_id":1,
            "nickname" : "kylee3",
            "password" : "1234"
        }
        
        response = self.client.post("/tdds/signup", data=json.dumps(data), content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'message':'CREATE_USER'})
    
    
    def test_failure_create_user_raise_role_does_not_exist(self):
        
        data = {
            "role_id":100,
            "nickname" : "kylee3",
            "password" : "1234"
        }
        
        response = self.client.post("/tdds/signup", data=data, content_type='application/json')
        
        assert response.status_code == 500
        assert response.json() == {'message':'ROLE_DOES_NOT_EXIST'}
    
    
    def test_failure_create_user_raise_nickname_already_exist(self):
        
        data = {
            "role_id":1,
            "nickname" : "kylee1",
            "password" : "1234"
        }
        
        response = self.client.post("/tdds/signup", data=data, content_type='application/json')
        
        assert response.status_code == 500
        assert response.json() == {'meesage':'NICKNAME_ALREADY_EXIST'}

    
    def test_success_get_user_list(self):
        
        response = self.client.get("/tdds/users")
        
        self.assertEqual(response.status_code , 200)
        self.assertEqual(response.json() , {"user_list":[
            {
                "id":8,
                "role":"admin1",
                "nickname":"kylee1"
            },
            {
                "id":9,
                "role":"normal1",
                "nickname":"kylee2"
            }
        ]})
    

    