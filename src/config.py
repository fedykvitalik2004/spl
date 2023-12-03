"""
All data for configuration is stored in the file
"""
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

ASCII_ART_GENERATOR = "./data/lab3/output.txt"
ASCII_ART_GENERATOR_OUTPUT = "./data/lab4/output.txt"
OWN_ASCII_ART_GENERATOR_OUTPUT_FONT = "./data/lab4/fori.txt"
JSON_FILE_PATH = "./data/lab4/result.json"
FIGURE_2D = "./data/lab5/2d.txt"
FIGURE_3D = "./data/lab5/3d.txt"
DIFFERENCE_IN_YEARS_HISTOGRAM = "./data/lab8/difference-in-years-histogram.png"
SEX_PIE_CHART_PHOTO = "./data/lab8/sex-pie-chart.png"
JOB_BAR_CHART_PHOTO = "./data/lab8/job-bar-chart.png"
COMBINED_DIAGRAM_PHOTO = "./data/lab8/combined-diagram.png"
USERS_DATA = "./data/lab9/users.csv"

# credentials
# used for service RapidApi for LinkedIn Api
X_RAPID_API_KEY = "c7a26a1867mshab3dbfc2dad5fe2p1332a0jsn2e2fe8fdf0ae"
# used for service RapidApi for LinkedIn Api
X_RAPID_API_HOST = "fresh-linkedin-profile-data.p.rapidapi.com"
# urls
GET_PERSONAL_PROFILE = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile"
GET_PROFILES_PHOTO = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-profile-posts"
