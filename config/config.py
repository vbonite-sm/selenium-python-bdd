"""
Configuration file for framework settings
"""

class Config:
    # Base URL
    BASE_URL = "https://the-internet.herokuapp.com"
    
    # Browser settings
    BROWSER = "chrome"  # chrome, firefox, edge
    HEADLESS = False
    
    # Timeouts (in seconds)
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 15
    PAGE_LOAD_TIMEOUT = 30
    
    # Screenshot settings
    SCREENSHOT_ON_FAILURE = True
    SCREENSHOT_PATH = "screenshots/"
    
    # Report settings
    REPORT_PATH = "reports/"