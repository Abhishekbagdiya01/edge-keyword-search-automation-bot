import random
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# List of random keywords to search
keywords = ["cats", "dogs", "python programming",
            "machine learning", "openAI", "chatbots", "artificial intelligence", "data science", "natural language processing",
            "computer vision", "neural networks", "deep learning",
            "web development", "cloud computing", "cybersecurity",
            "internet of things", "augmented reality", "virtual reality",
            "blockchain", "cryptocurrency", "quantum computing",
            "bioinformatics", "genomics", "robotics",
            "space exploration", "astronomy", "physics",
            "chemistry", "biology", "environmental science",
            "geology", "meteorology", "oceanography",
            "economics", "finance", "stock market",
            "entrepreneurship", "business management", "marketing",
            "advertising", "branding", "public relations",
            "journalism", "writing", "literature",
            "history", "archaeology", "anthropology",
            "sociology", "psychology", "philosophy",
            "art", "music", "film",
            "theater", "dance", "photography",
            "painting", "sculpture", "architecture",
            "sports", "fitness", "nutrition",
            "cooking", "baking", "gardening",
            "DIY projects", "crafts", "knitting",
            "crocheting", "sewing", "woodworking",
            "metalworking", "electronics", "coding",
            "programming", "algorithms", "data structures",
            "software engineering", "game development", "mobile apps",
            "user experience", "user interface", "design",
            "graphic design", "UI/UX design", "product design",
            "fashion design", "interior design", "industrial design",
            "mechanical engineering", "civil engineering", "electrical engineering",
            "chemical engineering", "aerospace engineering", "biomedical engineering",
            "environmental engineering", "pet care", "veterinary medicine"]


# Initialize the Microsoft Edge web browser
driver_path = "/msedgedriver.exe"
service = Service(driver_path)
driver = webdriver.Edge(service=service)


try:
    while True:
        # Open a new browser window and navigate to Bing
        url = "https://www.bing.com/"  # Replace with the desired URL
        driver.get(url)

        # Find the search input field and enter the keyword
        for keyword in keywords:
            search_box = driver.find_element(By.NAME, "q")
            search_box.clear()
            # Choose a keyword from the list
            search_box.send_keys(keyword + Keys.RETURN)
            # Wait for some time before searching the next keyword
            timeDelay = random.randrange(5, 10)
            print("Keyword : " + keyword + "|| Delay : " + str(timeDelay))
            time.sleep(timeDelay)  # Adjust the delay as needed
except KeyboardInterrupt:
    # Close the browser window when the script is stopped
    driver.quit()
