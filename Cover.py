import streamlit as st
#import simulator as sim
import pandas as pd
import matplotlib.pyplot as plt
# streamlit run Cover.py --client.showErrorDetails=false   

st.set_page_config(page_title="Pokemon App",page_icon=":kangaroo:",layout="wide")
st.title("The Pokemon App")
st.image('imagenes\logo_pokemon.png',width=800)
st.logo('imagenes\pokebal_icon.png')

# Load Dataset
@st.cache_data
def load_data():
    pokemon_data = pd.read_csv('dataset/pokemon_final.csv')
    pokemon_data.drop(columns='Unnamed: 0', inplace=True)
    pokemon_data['Base_type'].replace('Fighting', 'Fight', inplace=True)
    pokemon_data['Secondary_type'].replace('Fighting', 'Fight', inplace=True)
    pokemon_data["Generation"] = pokemon_data["Generation"].astype(int)
    pokemon_data["Legendary"] = pokemon_data["Legendary"].astype(int)
    return pokemon_data

# Load Dataset
pokemon_data = load_data()

def main():
    st.title("Project Summary")
    st.markdown("This final project aims to recreate one of the great pastimes of my childhood through a :red[Pokédex], using two Kaggle datasets—one containing information on eight generations of Pokémon and another with their images—along with a ninth generation dataset that I fully extracted myself. The goal is to display :blue-background[Pokémon statistics], develop a :blue-background[machine learning model] that accurately classifies whether a Pokémon is legendary based on its features, implement a :blue-background[battle simulator] as the core challenge of the project, and add a small :blue-background[quiz] to enhance interactivity within the Streamlit interface")

    st.subheader("1. Data Extraction")
    st.write("In this project, I performed extensive data extraction using Python, leveraging web scraping techniques with Selenium and API data retrieval. The process involved significant trial and error to standardize the scraped data to match a Kaggle dataset. Additionally, I explored methods to scrape and download images. The final step focused on data transformation, merging, and mapping across multiple dataframes, highlighting the importance of raw data extraction over using pre-processed datasets.")
    
    st.subheader("2. Data Cleaning")
    st.write("After extracting and formatting the data, I performed data cleaning and transformation using Python. This process involved removing unnecessary columns, handling null values, converting data types, and ensuring data consistency. These steps were essential to achieving a robust dataset. This project highlights the importance of data cleaning in any data-driven initiative and how proper preprocessing enhances data quality. By leveraging Python libraries and custom functions, I ensured efficient data transformation, leading to more accurate and reliable machine learning results.")
    
    st.subheader("3. Pokemon Modeling")
    st.markdown("In this project, I developed a machine learning model using a Random Forest Classifier to predict whether a Pokémon is legendary based on its features. After testing multiple classifiers, Random Forest was chosen for its strong performance, achieving a :blue-background[Recall score of 0.98]. The process began with data cleaning, feature selection, and multicollinearity analysis using VIF, followed by data normalization to ensure balanced input variables. The dataset was then split into training and testing sets to evaluate model performance.") 
    st.write("Various classification models were tested and fine-tuned to optimize results. Once the best model and parameters were identified, the final model was evaluated on unseen data. Lastly, I applied the model to predict legendary Pokémon for the first eight generations and integrated the results into a Streamlit interface, allowing users to predict outcomes for the ninth generation.")
    
    st.subheader("4. Battle Simulation")
    st.write("A key feature of this project is a Pokémon battle simulation built entirely with Python logic, classes, and functions. The process began with creating a main class to define all attributes, followed by implementing various functions to simulate battles. This was the most challenging yet enjoyable part of the project. After completing the simulation, I faced difficulties integrating it into Streamlit due to differences in logic and vocabulary. However, this integration enhanced the project by providing a more interactive and dynamic user interface.") 
    st.write("Although it was not possible to fully integrate the complete simulator code, a functional part was successfully implemented in Streamlit, demonstrating its core mechanics. The full code includes additional functionalities beyond what is shown in the interface")
    
    st.subheader("5. Image Classification for the Quizz")
    st.write("This project also includes an interactive component with a user interface. Using a dataset of images and leveraging the PIL and OpenCV (CV2) libraries, I implemented various image transformations. These include converting color images to black and white to isolate figures and applying filters to create a quiz-like experience")
    
    st.subheader("6. Visualization & Interface in Streamlit")
    st.write("In addition to other components, this project incorporates data visualization and a user interface. Visualizing data is crucial for understanding relationships between variables, and using Python libraries like Matplotlib, Plotly, and Seaborn, I created interactive visualizations to explore the data effectively. To enhance accessibility, I developed an interface where users can input features to participate in the battle simulation or quiz. This interface was built using Streamlit, enabling a more interactive and user-friendly experience.")
    st.write("Overall, this project showcases the power of combining data extraction, analysis, machine learning, Python logic, and UI design. By integrating data visualization and interactive elements, it delivers both accuracy and accessibility in a seamless application.")
    
if __name__ =='__main__':
    main()



