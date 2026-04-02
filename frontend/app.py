import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/search"

st.set_page_config(
    page_title="Khoj - The Search",
    page_icon="🔎",
    layout="centered"
)

st.title("🔎 Khoj - The Search")
st.caption("Search restaurants all over Bangladesh.")

query = st.text_input(
    "Search for a restaurant",
    placeholder="e.g. kacchi, biriyani, pathao"
)

if st.button("Search", use_container_width=True):
    if not query.strip():
        st.warning("Please enter a search query.")
    else:
        try:
            response = requests.get(API_URL, params={"q": query}, timeout=10)
            response.raise_for_status()
            data = response.json()

            results = data.get("results", [])

            if not results:
                st.info("No results found.")
            else:
                st.subheader(f"Results for: {data.get('query', query)}")

                for i, item in enumerate(results, start=1):
                    name = item.get("name", "N/A")
                    address = item.get("address", "N/A")
                    rating = item.get("rating", 0)
                    reviews = item.get("reviews", 0)
                    score = item.get("score", 0)

                    with st.container():
                        st.markdown(f"### {i}. {name}")
                        st.write(f"📍 **Address:** {address}")
                        st.write(f"⭐ **Rating:** {rating}")
                        st.write(f"📝 **Reviews:** {reviews}")
                        st.write(f"🎯 **Score:** {score}")
                        st.divider()

        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the FastAPI server. Make sure it is running on http://127.0.0.1:8000")
        except requests.exceptions.Timeout:
            st.error("The request timed out.")
        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")