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