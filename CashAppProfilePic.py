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
            return "Profile photo not found."
    else:
        return "Failed to fetch page source."

def main():
    # Prompt the user to enter a Cash App username
    username = input("Enter Cash App username: ")
    
    # Get the profile photo URL
    profile_photo_url = get_profile_photo(username)
    
    # Display the profile photo URL
    print("Profile photo URL:", profile_photo_url)

if __name__ == "__main__":
    main()
