import pandas as pd
import numpy as np
import pickle
import streamlit as st


# loading in the model to predict on the data
pickle_in = open('clf.pkl', 'rb')
classifier = pickle.load(pickle_in)

def welcome():
	return 'welcome all'

# defining the function which will make the prediction using
# the data which the user inputs
def prediction(Price, Area, Location, No. of Bedrooms, New/Resale,
       Gymnasium, Lift Available, Car Parking, Maintenance Staff,
       24x7 Security, Childrens Play Area, Clubhouse, Intercom,
       Landscaped Gardens, Indoor Games, Gas Connection, Jogging Track,
       Swimming Pool):

	prediction = classifier.predict(
		[[Price, Area, Location, No. of Bedrooms, New/Resale,
       Gymnasium, Lift Available, Car Parking, Maintenance Staff,
       24x7 Security, Childrens Play Area, Clubhouse, Intercom,
       Landscaped Gardens, Indoor Games, Gas Connection, Jogging Track,
       Swimming Pool]])
	print(prediction)
	return prediction
	

# this is the main function in which we define our webpage
def main():
	# giving the webpage a title
	st.title("Mumbai House Pricing Prediction")
	
	# here we define some of the front end elements of the web page like
	# the font and background color, the padding and the text to be displayed
	html_temp = """
	<div style ="background-color:yellow;padding:13px">
	<h1 style ="color:black;text-align:center;">Streamlit Mumbai Housing Set ML App </h1>
	</div>
	"""
	
	# this line allows us to display the front end aspects we have
	# defined in the above code
	st.markdown(html_temp, unsafe_allow_html = True)
	
	# the following lines create text boxes in which the user can enter
	# the data required to make the prediction
	Price = st.text_input("Price", "Type Here")
	Area = st.text_input("Area", "Type Here")
	Location = st.text_input("Location", "Type Here")
	No. of Bedrooms = st.text_input("No. of Bedrooms", "Type Here")
	New/Resale=st.text_input("New/Resale", "Type Here")
	Gymnasium=st.text_input("Gymnasium", "Type Here")
	Lift Available=st.text_input("Lift Available", "Type Here")
	Car Parking=st.text_input("Car Parking", "Type Here")
	Maintenance Staff=st.text_input("Maintenance Staff", "Type Here")
        24x7 Security=st.text_input("24x7 Security", "Type Here")
        Childrens Play Area=st.text_input("Childrens Play Area", "Type Here")
        Clubhouse=st.text_input("Clubhouse", "Type Here")
        Intercom=st.text_input("Intercom", "Type Here")
        Landscaped Gardens=st.text_input("Landscaped Gardens", "Type Here")
        Indoor Games=st.text_input("Indoor Games", "Type Here")
        Gas Connection=st.text_input("Gas Connection", "Type Here")
        Jogging Track=st.text_input("Jogging Track", "Type Here")
        Swimming Pool=st.text_input("Swimming Pool", "Type Here")
	result =""
	
	# the below line ensures that when the button called 'Predict' is clicked,
	# the prediction function defined above is called to make the prediction
	# and store it in the variable result
	if st.button("Predict"):
		result = prediction(Price, Area, Location, No. of Bedrooms, New/Resale,
       Gymnasium, Lift Available, Car Parking, Maintenance Staff,
       24x7 Security, Childrens Play Area, Clubhouse, Intercom,
       Landscaped Gardens, Indoor Games, Gas Connection, Jogging Track,
       Swimming Pool)
	st.success('The output is {}'.format(result))
	
if __name__=='__main__':
	main()
