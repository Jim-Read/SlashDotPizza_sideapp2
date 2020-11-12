import unittest
from main import create_app, db
from models.Pizza import Pizza

class TestPizzas(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()

        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db", "seed"])

    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()
    
    def test_pizza_index(self):
        response = self.client.get("/pizzas/")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_pizza_create(self):
        response = self.client.post("/pizzas/", json={
            "pizza_name": "Test Pizza",
            "description": "A very hot pizza",
            "price": "16.22",
            "location": "Down back",
            "pizza_image": "http://"
        })

        data = response.get_json()

        #self.assertEqual(response.status_code, 200)
        self.assertTrue(bool(response.status_code >= 200 and response.status_code < 300))
        self.assertIsInstance(data, dict)
        self.assertTrue(bool("pizza_id" in data.keys()))

        pizza = Pizza.query.get(data["pizza_id"])
        self.assertIsNotNone(pizza)

    def test_pizza_delete(self):
        pizza = Pizza.query.first()

        response = self.client.delete(f"/pizzas/{pizza.pizza_id}")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)

        pizza = Pizza.query.get(pizza.pizza_id)
        self.assertIsNone(pizza)