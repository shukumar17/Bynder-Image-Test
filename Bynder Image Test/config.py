"""Configuration file for authentication credentials.

Store your protected site credentials here.
"""

# Authentication Configuration
AUTH_CONFIG = {
    # HTTP Basic Authentication
    'username': 'storefront',
    'password': '72MarcJacobs',
    
    # Optional: Add more authentication configurations as needed
    # For different sites, you can add site-specific credentials:
    # 'site_credentials': {
    #     'dev.marcjacobs.com': {
    #         'username': 'storefront',
    #         'password': '72MarcJacobs'
    #     },
    #     'other-site.com': {
    #         'username': 'user',
    #         'password': 'pass'
    #     }
    # }
}

# Selenium Authentication (for sites requiring form-based login)
SELENIUM_AUTH = {
    'enabled': False,  # Set to True if you need form-based login
    'login_url': '',  # URL of the login page
    'username_field': 'username',  # ID or name of username field
    'password_field': 'password',  # ID or name of password field
    'submit_button': 'submit',  # ID or name of submit button
}

# Timeout settings
REQUEST_TIMEOUT = 90  # seconds
PAGE_LOAD_TIMEOUT = 90  # seconds
