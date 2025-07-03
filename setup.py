from setuptools import find_packages,setup
from typing import List
from custom_logging.logger import get_logger

logger = get_logger(__name__)

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []
    
    try:

        logger.info("Setting Up The environment")
        # Open and read the requirements.txt file
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Process each line
            for line in lines:
                # Strip whitespace and newline characters
                requirement = line.strip()
                # Ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    
        
    return requirement_list
print(get_requirements())

setup(
    name="Agentic-AI-Trip-Planner",
    version="0.0.1",
    author="Meet Wadekar",
    author_email="meetwadekar7@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements()
)