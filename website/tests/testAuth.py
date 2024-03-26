import unittest
from flask_testing import TestCase
from website import auth, db, app, models

class AuthViewsTestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
        app.register_blueprint(auth.auth)
        return app

    def setUp(self):
        db.create_all()
        self.client = self.app.test_client()
        self.bcrypt = app.bcrypt
        with self.app.app_context():
            user = models.User(email='percymagoras@outlook.com', password=self.bcrypt.generate_password_hash('password').decode('utf-8'))
            db.session.add(user)
            db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_login_valid_credentials(self):
        response = self.client.post('/auth/Login.action', data={'email': 'percymagoras@outlook.com', 'password': 'L3mm1ng$'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Logged in successfully!', response.data)
        self.assert_template_used('views/dashboard.html')

    def test_login_invalid_password(self):
        response = self.client.post('/auth/Login.action', data={'email': 'percymagoras@outlook.com', 'password': 'wrong_password'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Incorrect password', response.data)
        self.assert_template_used('/auth/login.html')

    def test_login_nonexistent_email(self):
        response = self.client.post('/auth/Login.action', data={'email': 'nonexistent@example.com', 'password': 'password'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Email does not exist', response.data)
        self.assert_template_used('/auth/login.html')

    def test_logout(self):
        response = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        #self.assertIn(b'You have been logged out', response.data)
        self.assert_template_used('/auth/login.html')

    def test_signup_valid_credentials(self):
        response = self.client.post('/auth/Registration.action', data={'email': 'newuser@example.com', 'password': 'M7_K@33bvKf$R'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Account created successfully', response.data)
        self.assert_template_used('views/dashboard.html')

    def test_signup_existing_email(self):
        response = self.client.post('/auth/Registration.action', data={'email': 'percymagoras@outlook.com', 'password': 'Password!123'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Email already exists', response.data)
        self.assert_template_used('/auth/signup.html')

    def test_signup_weak_password(self):
        response = self.client.post('/auth/Registration.action', data={'email': 'newuser@example.com', 'password': 'password123'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Password should contain at least a symbol and uppercase characters', response.data)
        self.assert_template_used('/auth/signup.html')

    def test_signup_recaptcha_failed(self):
        response = self.client.post('/auth/Registration.action', data={'email': 'newuser@example.com', 'password': 'P0pp_23@T'}, follow_redirects=True,
                                    headers={'Referer': '/auth/Registration.action'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Recaptcha failed', response.data)
        self.assert_template_used('/auth/signup.html')

if __name__ == '__main__':
    unittest.main()
