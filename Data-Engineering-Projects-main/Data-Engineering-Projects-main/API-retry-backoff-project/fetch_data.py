import time    #Used to add delays between retries
import requests   #Used to send HTTP requests (like calling an API).


# This function tries to fetch data from an API URL.
# It will retry up to max_retries times (default is 5)
def fetch_data_with_retry(url, max_retries=5):

    #	If the API fails, the script will wait 1 second before retrying.
    #   Each time it fails, the delay will double (exponential backoff).
    delay = 1  # start with 1 second delay

    # A loop that runs up to 5 times (or any number you set)
    # attempt tracks which try we’re on (1st, 2nd, etc.)
    for attempt in range(1, max_retries + 1):

        # Sends a GET request to the API with a 5-second timeout.
	# raise_for_status() throws an error if the response is bad (like 404 or 500).
	# If it works, it returns the data and exits the function.
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # raise error for bad status codes
            return response.json()  # or response.text depending on your needs

        # If the request fails, the error is caught here and printed.
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt} failed: {e}")

            # If we haven’t reached the last attempt, wait delay seconds.
	    # Then double the delay time for the next try.
            if attempt < max_retries:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
                delay *= 2  # exponential backoff

            # If we’ve tried all attempts and still failed, return None.
            else:
                print("All retries failed.")
                return None


# Calls the function with a sample API endpoint.
# Example usage:
data = fetch_data_with_retry("https://api.example.com/data")
# data = fetch_data_with_retry("https://jsonplaceholder.typicode.com/posts/1")  # a real working API

# If the function returned data, it prints success.
# Otherwise, it says it failed.
if data:
    print("Data retrieved successfully!")
else:
    print("Failed to retrieve data.")
