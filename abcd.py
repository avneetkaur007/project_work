import streamlit as st
#st.balloons()
st.title('Hello this my first app')
st.write('let us create app')
st.text_input('Enter your name')
st.number_input('Enter your marks')
x=st.radio('Are you working',options=['Yes','No'])
if x=='Yes':
    st.write('You can choose Weekend batch')
else:
    st.write('You can choose weekdays batch')
st.sidebar.markdown('Test Results')
y=st.sidebar.checkbox('Are you interested in IT')
if y==1:
    st.sidebar.write('You can choose python')

