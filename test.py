from app import app 


#testing
def test1():
    '''
    This is function tets that the flask appplication
    has a correct response code
    when the application goes live 
    '''
    response = app.test_client().get("/")
    assert response.status_code == 200 
    
def test2():
    response = app.test_client().get("/edit")
    assert response.status_code == 200
    
#passed 
def test3():
    response = app.test_client().get("/edit")
    assert b"To Do App" in response.data 
    assert b"Todo Title" in response.data
    assert b"Add" in response.data
