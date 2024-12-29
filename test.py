import unittest
import json
from app import app
from app.models import db
from app.settings import DB_NAME, DB_USER, DB_PASSWORD, TOKEN_CASTING_DIRECTOR, TOKEN_CASTING_ASSISTANT, TOKEN_EXPIRED

class CastingAgencyTestCase(unittest.TestCase):
    def setUp(self):
        self.database_name = DB_NAME
        self.database_user = DB_USER
        self.database_password = DB_PASSWORD
        self.database_path = 'postgresql://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, 'localhost:5432', DB_NAME)

        self.app = app
        self.client = app.test_client

        with app.app_context():
            db.create_all()

    def tearDown(self):
        """Executed after each test"""
        pass

    def get_headers(self, token):
        return {
            "Authorization": token
        }

    # # test get_movies
    def test_get_movies(self):
        res = self.client().get('/movies', headers=self.get_headers(TOKEN_CASTING_DIRECTOR))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movies"])

    def test_failed_get_movies(self):
        res = self.client().get('/movies', headers=self.get_headers(TOKEN_EXPIRED))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"])

    # # test get_actors
    def test_get_actors(self):
        res = self.client().get('/actors', headers=self.get_headers(TOKEN_CASTING_DIRECTOR))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    def test_failed_get_actors(self):
        res = self.client().get('/actors', headers=self.get_headers(TOKEN_EXPIRED))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"])

    # # test get_movie_by_id
    def test_get_movie_by_id(self):
        res = self.client().get('/movies/1', headers=self.get_headers(TOKEN_CASTING_DIRECTOR))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movie"]) 

    def test_failed_get_movies_by_id(self):
        res = self.client().get('/movies/1', headers=self.get_headers(TOKEN_EXPIRED))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"])

    # # test get_actor_by_id
    def test_get_actor_by_id(self):
        res = self.client().get('/actors/1', headers=self.get_headers(TOKEN_CASTING_DIRECTOR))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actor"])

    def test_failed_get_actor_by_id(self):
        res = self.client().get('/actors/1', headers=self.get_headers(TOKEN_EXPIRED))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"])

    # # test delete_movies
    def test_delete_movies(self):
        res = self.client().delete('/movies/1', headers=self.get_headers(TOKEN_CASTING_DIRECTOR))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["delete"]) 

    def test_error_404_when_delete_movie_by_id(self):
        res = self.client().delete('/movies/1000', headers=self.get_headers(TOKEN_CASTING_DIRECTOR))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"])

    # # test delete_actors
    def test_delete_actor(self):
        res = self.client().delete('/actors/1', headers=self.get_headers(TOKEN_CASTING_DIRECTOR))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["delete"]) 

    def test_error_404_when_delete_actor_by_id(self):
        res = self.client().delete('/actors/1000', headers=self.get_headers(TOKEN_CASTING_DIRECTOR))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"])

    # # test create_movie    
    def test_create_movie(self):
        res = self.client().post('/movies', headers=self.get_headers(TOKEN_CASTING_DIRECTOR), json = {"title":"movie test","releaseDate":"2024-12-25T18:46:38.455Z","idsActor":[1]})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movie"])

    def test_failed_create_movie(self):
        res = self.client().post('/movies', headers=self.get_headers(TOKEN_CASTING_ASSISTANT), json = {"title":"movie test","releaseDate":"2024-12-25T18:46:38.455Z","idsActor":[1]})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"])

    # # test create actor   
    def test_create_actor(self):
        res = self.client().post('/actors', headers=self.get_headers(TOKEN_CASTING_DIRECTOR), json = {"name":"test actor","age":4,"gender":"male","idsMovie":[2]})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actor"])

    def test_failed_create_actor(self):
        res = self.client().post('/actors', headers=self.get_headers(TOKEN_CASTING_DIRECTOR), json = {"age":4,"gender":"male","idsMovie":[2]})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"])

    # # test update_movie   
    def update_movie(self):
        res = self.client().patch('/movies/1', headers=self.get_headers(TOKEN_CASTING_DIRECTOR), json = {"id": 1,"title":"iphone","releaseDate":"2024-12-26T17:00:00.000Z","idsActor":[1,3]})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movie"])

    def test_failed_update_movie(self):
        res = self.client().patch('/movies/1', headers=self.get_headers(TOKEN_CASTING_DIRECTOR), json = {"id": 1,"releaseDate":"2024-12-26T17:00:00.000Z","idsActor":[1,3]})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"])

    # # test update_actor  
    def update_actor(self):
        res = self.client().patch('/actors/1', headers=self.get_headers(TOKEN_CASTING_DIRECTOR), json = {"name":"test actor","age":5,"gender":"male","idsMovie":[2]})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actor"])

    def test_failed_update_actor(self):
        res = self.client().patch('/actors/1', headers=self.get_headers(TOKEN_CASTING_DIRECTOR), json = {"age":5,"gender":"male","idsMovie":[2]})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertTrue(data["message"])
    
    # # RBAC tests
    def test_brac_create_movie(self):
        res = self.client().post('/movies', headers=self.get_headers(TOKEN_CASTING_DIRECTOR), json = {"title":"movie test","releaseDate":"2024-12-25T18:46:38.455Z","idsActor":[1]})
        self.assertEqual(res.status_code, 200)

        res = self.client().post('/movies', headers=self.get_headers(TOKEN_CASTING_ASSISTANT), json = {"title":"movie test","releaseDate":"2024-12-25T18:46:38.455Z","idsActor":[1]})
        self.assertEqual(res.status_code, 403)

    def test_brac_update_movie(self):
        res = self.client().patch('/movies/1', headers=self.get_headers(TOKEN_CASTING_DIRECTOR), json = {"id": 1,"title":"iphone","releaseDate":"2024-12-26T17:00:00.000Z","idsActor":[1,3]})
        self.assertEqual(res.status_code, 200)

        res = self.client().patch('/movies/1', headers=self.get_headers(TOKEN_CASTING_ASSISTANT), json = {"id": 1,"title":"iphone","releaseDate":"2024-12-26T17:00:00.000Z","idsActor":[1,3]})
        self.assertEqual(res.status_code, 403)
    
# Run tests
if __name__ == "__main__":
    unittest.main()