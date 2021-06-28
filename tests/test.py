import pytest
with app.test_client() as c:
    response = c.get('/Index')
    self.assertEquals(response.status_code, 200)
