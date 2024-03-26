import requests
from bs4 import BeautifulSoup

# Start a session to maintain cookies and headers across requests
session = requests.Session()

# Set User-Agent and other relevant headers
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://bloompeermentor.powerappsportals.com/SignIn?returnUrl=%2F',
    # Add other headers as necessary
})

login_url = 'https://bloompeermentor.powerappsportals.com/SignIn?returnUrl=%2F'

# First, fetch the login page to get the CSRF token
response = session.get(login_url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
csrf_token = soup.find('input', {'name': '__RequestVerificationToken'}).get('value')

# Prepare the POST data
login_data = {
    'Username': 'aaronphil123',
    'PasswordValue': 'a2zSaintz',
    '__RequestVerificationToken': csrf_token,
    # Include any other required fields
}

# Send the login request
login_response = session.post(login_url, data=login_data)
login_response.raise_for_status()


if login_url not in login_response.url:
    print("Login successful!")
else:
    print("Still on login page. Login might have failed.")

protected_page_url = 'https://bloompeermentor.powerappsportals.com/PC/'
protected_page_response = session.get(protected_page_url)
protected_page_response.raise_for_status()  # Ensure the request was successful

protected_filename = 'protected_page.html'
with open(protected_filename, 'w', encoding='utf-8') as file:
    file.write(protected_page_response.text)



