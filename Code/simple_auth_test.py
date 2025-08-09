def login(username, password):
    users = {
        "user1": "password123",
        "user2": "securepass"
    }
    return users.get(username) == password

def test_login():
    assert login("user1", "password123") == True, "Correct login should pass"
    assert login("user1", "wrongpass") == False, "Wrong password should fail"
    assert login("unknown", "password123") == False, "Unknown user should fail"
    print("All tests passed!")

if __name__ == "__main__":
    test_login()
