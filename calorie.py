import streamlit as st
import requests

# Filtered words
filtered_words = [
    "illegal", "hack", "pirate", "script", "source code", "game",
    "website", "coupons", "keys", "activation", "jailbreak", "nudity",
    "python", "porn", "laptop", "mobile", "electronic device", "google",
    "youtube", "social media", "app", "links", "machine", "malicious",
    "bug", "trojan", "sex", "webpages", "kill", "pedofile", "attract",
    "dick", "fuck", "adult websites", "private parts", "free coupons",
    "guns", "drugs", "mafia", "crack", "modification", "stealing", "dark",
    "racist", "api", "ban", "upi", "movies", "webseries", "entertainment",
    "comic", "manga", "books", "animation", "bikini","computer","technology"
]

# Function to fetch data from API
def fetch_data(query):
    for word in filtered_words:
        if word in query.lower():
            st.warning(f"The word '{word}' is not allowed.")
            return None

    api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
    api_key = 'IpjuGmYZ9Cv55BxE2ddH1A==DTbYGkRSKPhv9g9Z'  # Replace 'your_api_key_here' with your actual API key
    response = requests.get(api_url + query, headers={'X-Api-Key': api_key})
    return response.json() if response.status_code == requests.codes.ok else None

# Streamlit app
def main():
    st.title("Calorie Calculator")

    query = st.text_input("Enter the Query to Calculate Calories:")
    if st.button("Calculate"):
        if query:
            data = fetch_data(query)
            if data:
                for item in data['items']:
                    st.subheader("Item: " + item['name'])
                    st.write("Calories:", item['calories'])
                    st.write("Protein (g):", item['protein_g'])
                    st.write("Carbohydrates (g):", item['carbohydrates_total_g'])
                    st.write("Fat (g):", item['fat_total_g'])
                    st.write("Fiber (g):", item['fiber_g'])
                    st.write("Sugar (g):", item['sugar_g'])
                    st.write("Serving Size:", item['serving_size_g'])
                    st.write("===================================")
            else:
                st.error("Error fetching data. Please try again.")
        else:
            st.warning("Please enter a query.")

if __name__ == "_main_":
    main()