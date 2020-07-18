import requests as req

response = req.post('http://localhost:5000/joystick',
    headers={'Content-Type': 'application/json'},
    json = {'x': 0.0, 'y': 0.5})

print(response.text)
