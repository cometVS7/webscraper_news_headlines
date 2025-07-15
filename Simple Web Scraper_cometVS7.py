import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import scrolledtext

def scrape_headlines():
    url = "https://www.indiatoday.in/india"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all('h2')  # headlines are in <h2> tags
        
        results = [headline.get_text(strip=True) for headline in headlines]
        return results
    else:
        return ["Failed to retrieve data."]
    
def display_headlines():
    headlines = scrape_headlines()  # Get scraped data
    
    # Clear the text area before inserting new content
    result_text.delete(1.0, tk.END)
    
    # Insert each headline into the text area
    for headline in headlines:
        result_text.insert(tk.END, headline + "\n\n")

# Initialize main window
root = tk.Tk()
root.title("News Headlines Scraper")
root.geometry("500x400")

# Add title label
title_label = tk.Label(root, text="Simple News Headlines Scraper", font=("Arial", 14))
title_label.pack(pady=10)

# Add scrolled text widget for displaying results
result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15, font=("Arial", 10))
result_text.pack(pady=10)

# Add scrape button
scrape_button = tk.Button(root, text="Get Latest Headlines", command=display_headlines, font=("Arial", 12), bg="blue", fg="white")
scrape_button.pack(pady=10)

# Run the main loop
root.mainloop()