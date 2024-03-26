import unittest
from flask import Flask
from flask_testing import TestCase
from website import views

class ViewsTestCase(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.register_blueprint(views.views)
        return app

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('index.html')

    def test_func(self):
        response = self.client.get('/python')
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('quizzes/python.html')

    def test_dashboard_authenticated(self):
        self.client.login_user('testuser')
        response = self.client.get('/quiz/dashboard', headers={'Referer': '/auth/Login.action'})
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('quizzes/dashboard.html')
        self.assert_context('user', 'testuser')

    def test_dashboard_unauthenticated(self):
        response = self.client.get('/quiz/dashboard')
        self.assertRedirects(response, '/auth/Login.action')

    def test_dashboard_quizzes_referer(self):
        response = self.client.get('/quiz/dashboard', headers={'Referer': '/quiz/quizzes/python'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "quizzes")

    def test_dashboard_other_referer(self):
        self.client.login_user('testuser')
        response = self.client.get('/quiz/dashboard', headers={'Referer': '/other/page'})
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('quizzes/dash_.html')
        self.assert_context('user', 'testuser')

if __name__ == '__main__':
    unittest.main()
    
