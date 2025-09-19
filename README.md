# Data Entry Automation

This project demonstrates a complete **data-entry automation pipeline**:

1. **Scrape** rental property listings (address, price, link) from a Zillow-Clone site.
2. **Automate form filling** with Selenium to input the scraped data into a Google Form.
3. **Automatically export** responses into **Google Sheets** using Google Forms’ built-in integration.

This transforms a simple scraper into an **end-to-end automation workflow** that eliminates repetitive copy-paste tasks.

<br/>

## 🚀 Features

- Scrapes property `addresses`, `prices`, and `links` from the Zillow-Clone website.
- Cleans and preprocesses the raw data.
- Automates **form submission** using Selenium WebDriver.
- Stores responses in **Google Sheets** automatically.
- Includes error handling and modular code for reliability.

<br/>

## 🛠️ Tech Stack

- **Python 3.10+**
- **BeautifulSoup4** – web scraping
- **Requests** – HTTP requests
- **Selenium** – browser automation
- **Chrome WebDriver** – Chrome browser control

<br/>

## 📦 Installation

**1. Clone this repository:**

```bash
git clone https://github.com/mudasirfayaz/data-entry-automation.git
cd data-entry-automation
```

<br/>

**2. Install dependencies:**

```bash
pip install -r requirements.txt
```

<br/>

**2. Set up your own Google Form:**

First, you need to create a new form in Google Forms.

1. Go to [https://docs.google.com/forms/](https://docs.google.com/forms/) and create your own form:

<br/>

![Create Form](/assets/step1.webp)

<br/>

2. Add 3 questions to the form, make all questions "short-answer":

<br/>

![Add Questions](/assets/step2.webp)

<br/>

3. Click send and copy the link address of the form. You will need to use this in your program.

<br/>

![Send & Copy](/assets/step3.webp)

<br/>

**3. Configuration**

1. Open `main.py`.

2. Update the Google Form link and the XPath selectors inside the `FORM_CONFIG` dictionary:

```bash
FORM_CONFIG = {
    "url": "YOUR_GOOGLE_FORM_LINK",
    "fields": {
        "address": "//input[@aria-label='Address']",
        "price": "//input[@aria-label='Price']",
        "link": "//input[@aria-label='Link']",
        "submit": "//span[text()='Submit']/ancestor::div[@role='button']",
    }
}
```

<br/>

## ▶️ Usage

Run the script:

```bash
python main.py
```

<br/>

The bot will:

- Scrape rental data from the Zillow-Clone site.
- Open your Google Form in Chrome.
- Auto-fill and submit the form for each property.
- Store responses directly in Google Sheets (via Google Forms’ built-in export).

<br/>

## 📚 Learning Outcomes

By completing this project, you’ll learn how to:

- Scrape structured data from websites using BeautifulSoup.
- Automate form submissions with Selenium WebDriver.
- Understand how Google Forms can act as a data pipeline into Google Sheets.
- Apply error handling and modular coding practices in automation.
- Conceptualize end-to-end data entry automation systems.

<br/>

## 🧑‍💻 Author

**[Mudasir Fayaz](https://github.com/mudasirfayaz/)** - Python Developer | Automation Engineer | Aspiring AI/ML Specialist<br/>
_Building fun and useful Python tools_

<br/>

# 📜 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.
