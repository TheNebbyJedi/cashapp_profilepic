# cashapp_profilepic
This is a small Python script that allows the input of a cashtag and will output the URL of the profile picture

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
</head>
<body>
  <h1>CashTag OSINT Tool</h1>
  <p>This Python script allows users to input a Cashtag (Cash App username) and retrieve the source URL for the profile photo associated with that username. It can be used by investigators and researchers for open-source intelligence (OSINT) purposes.</p>
  
  <h2>Usage</h2>
  <p>To use the script, follow these steps:</p>
  <ol>
    <li>Ensure you have Python installed on your system.</li>
    <li>Download the script file (cashappprofilepic.py) from this repository.</li>
    <li>Run the script in your terminal or command prompt.</li>
    <li>Enter the Cashtag when prompted.</li>
    <li>The script will then retrieve and display the source URL for the profile photo associated with the provided Cashtag.</li>
  </ol>
  
  <h2>Dependencies</h2>
  <p>This script requires the following Python packages:</p>
  <ul>
    <li>requests</li>
  </ul>
  <p>You can install these dependencies using pip:</p>
  <pre><code>pip install requests</code></pre>
  
 
  <h2>Python Script</h2>
  <p>Below is the Python script (cashappprofilepic.py) included in this repository:</p>
  <pre><code>
import requests

def get_profile_photo(username):
    # Construct the URL for the Cash App profile
    url = f"https://cash.app/${username}"
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Search for the profile picture URL in the page source
        start_index = response.text.find("https://franklin-assets.s3.amazonaws.com/apps/imgs")
        if start_index != -1:
            end_index = response.text.find('"', start_index)
            profile_photo_url = response.text[start_index:end_index]
            return profile_photo_url
        else:
            # No profile photo found, provide explanation and link
            explanation = ("No profile photo was found, but this account does exist. "
                           f"Click this link to see the account: "
                           f"https://cash.app/${username}")
            return explanation
    else:
        # No profile photo found, provide explanation
        explanation = ("There is no Cash App account with this username.")
        return explanation

def main():
    # Prompt the user to enter a Cash App username
    username = input("Enter Cash App username: ")
    
    # Get the profile photo URL or explanation
    result = get_profile_photo(username)
    
    # Display the profile photo URL or explanation
    print("Profile photo URL or Explanation:", result)

if __name__ == "__main__":
    main()

  </code></pre>
</body>
</html>
