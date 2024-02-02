import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader

st.set_page_config(
    page_title = "ChatBot App"
)


st.sidebar.success("Select a page")

# Load authentication data through config.yaml file
with open("./pages/config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)
    
st.title("Log In Page:")
st.text("Doc Source: https://github.com/mkhorasani/Streamlit-Authenticator")
st.header("Authenticator:")
st.subheader("Parameters:")
st.markdown(
        """
    \ncredentials: dict - Provides the usernames, names, passwords, and emails, and other user data.
    \ncookie_name: st - Specifies the name of the JWT cookie stored on the client's browser for passwordless reauthentication.
    \nkey: str - Specifies the key that will be used to hash the signature of the JWT cookie.
    \ncookie_expiry_days: float, default 30.0 - Specifies the number of days before the reauthentication cookie automatically expires on the client's browser.
    \npreauthorized: list, default None - Provides the list of emails of unregistered users who are authorized to register.
    \nvalidator: object, default None - Provides a validator object that will check the validity of the username, name, and email fields.
    """
        )


authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

st.header("Authenticate.login:")
st.subheader("Parameters:")
st.markdown(
    """
\nlocation: str, {'main', 'sidebar'}, default 'main' - Specifies the location of the login widget.
\nmax_concurrent_users: int, default None - Limits the number of concurrent users. If not specified there will be no limit to the number of users.
\nfields: dict, default {'Form name':'Login', 'Username':'Username', 'Password':'Password', 'Login':'Login'} - Customizes the text of headers, buttons and other fields.
\nReturns:
\nstr - The name of the authenticated user.
\nbool - The status of authentication, None: no credentials entered, False: incorrect credentials, True: correct credentials.
\nstr - The username of the authenticated user.
"""
    )

st.header("Login Form Logic:")
st.text(
    """
with st.form("log_form"):
    # Log in method for previous users - will  
    st.title("Login")
    log_user = st.text_input("Log In Username: ")
    log_pass = st.text_input("Log In Password: ")
            
    # Usernames and Passwords variables as lists, or pull up table
    # Iterate through the list of logged users
            
            
    st.form_submit_button("Log In")

    # st.error("Incorrect Username/Password")
    # st.success("Successfully Logged In")
"""
    )

st.header("Authenticate.logout:")
st.subheader("Parameters:")
st.markdown(
    """
\nbutton_name: str, default 'Logout' - Customizes the button name.
\nlocation: str, {'main', 'sidebar','unrendered'}, default 'main' - Specifies the location of the logout button. If 'unrendered' is passed, the logout logic will be implemented without rendering the button.
\nkey: str, default None - A unique key that should be used in multipage applications.
""")

if st.session_state["authentication_status"]:
    st.write(f'Hello User: **{st.session_state["name"]}**')
    st.subheader('You have logged in')
    # logout button
    authenticator.logout()
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Enter your username and password')

# Authentication for login page - should model code so data is stored in cookies, can move to database set up after
authenticator.login()

# Authentication for sign up page - should model code so data is stored in cookies, can move to database set up after
#authenticator.signup()


st.header("Sign Up Form Logic:")
st.markdown(
    """
with st.form("sign_form"):
    st.title("Sign Up")   
    sign_user = st.text_input("Sign Up Username: ")
    sign_pass = st.text_input("Sign Up Password: ")
        
    st.form_submit_button("Sign Up")
        
    # st.success("Successfully Signed Up")
    
    # st.warning("User already exists") - Iterate through list of logged users
    # Direct user to login panel - unsure if to make 2 pages or 1, still trying to figure out how to conditionally hide sections
"""
    )

with st.form("sign_form"):
    st.title("Sign Up")   
    sign_user = st.text_input("Sign Up Username: ")
    sign_pass = st.text_input("Sign Up Password: ")

        
    st.form_submit_button("Sign Up")
        
    # st.success("Successfully Signed Up")
    
    
    # st.warning("User already exists") - Iterate through list of logged users
    # Direct user to login panel - unsure if to make 2 pages or 1, still trying to figure out how to conditionally hide sections

