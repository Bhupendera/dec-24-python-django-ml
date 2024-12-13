# Setup and run Flask app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
flask run

# Powershell
$response = Invoke-WebRequest -Uri http://127.0.0.1:5000/login `
    -Method POST `
    -Headers @{ "Content-Type" = "application/json" } `
    -Body '{"username": "admin", "password": "password123"}'

# Save the token
$token = ($response.Content | ConvertFrom-Json).access_token

Write-Host "Token: $token"


Invoke-WebRequest -Uri http://127.0.0.1:5000/employees `
    -Method GET `
    -Headers @{ 
        "Content-Type" = "application/json"; 
        "Authorization" = "Bearer $token" 
    }



Invoke-WebRequest -Uri http://127.0.0.1:5000/employee `
    -Method POST `
    -Headers @{ 
        "Content-Type" = "application/json"; 
        "Authorization" = "Bearer $token" 
    } `
    -Body '{"name": "Atin", "position": "Software Engineer", "department": "Engineering"}'



Invoke-WebRequest -Uri http://127.0.0.1:5000/employee/1 `
    -Method GET `
    -Headers @{ 
        "Content-Type" = "application/json"; 
        "Authorization" = "Bearer $token" 
    }



Invoke-WebRequest -Uri http://127.0.0.1:5000/employee/1 `
    -Method PUT `
    -Headers @{ 
        "Content-Type" = "application/json"; 
        "Authorization" = "Bearer $token" 
    } `
    -Body '{"name": "Updated Name", "position": "Senior Engineer", "department": "Engineering"}'



Invoke-WebRequest -Uri http://127.0.0.1:5000/employee/1 `
    -Method DELETE `
    -Headers @{ 
        "Content-Type" = "application/json"; 
        "Authorization" = "Bearer $token" 
    }



