# AWS Amplify Scrapy Application

This project is an AWS Amplify application that utilizes Scrapy to scrape contact information from a specified website and displays the results in real time.

## Project Structure

```
aws-amplify-scrapy-app
├── amplify
│   └── backend
├── src
│   ├── scraper
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   ├── settings.py
│   │   └── spiders
│   │       └── contact_spider.py
│   ├── app.js
│   ├── components
│   │   └── ResultsDisplay.js
│   └── styles
│       └── app.css
├── package.json
├── requirements.txt
├── amplify.yml
└── README.md
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd aws-amplify-scrapy-app
   ```

2. **Install Python Dependencies**
   Ensure you have Python installed, then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Node.js Dependencies**
   Make sure you have Node.js installed, then install the necessary packages:
   ```bash
   npm install
   ```

4. **Configure AWS Amplify**
   Set up your AWS Amplify project by following the instructions in the `amplify` directory.

5. **Run the Scraper**
   To start the Scrapy spider, navigate to the `src/scraper` directory and run:
   ```bash
   scrapy crawl contact_spider
   ```

6. **Run the Application**
   Start the React application:
   ```bash
   npm start
   ```

## Usage

Once the application is running, it will scrape the specified website for contact information and display the results in real time using the `ResultsDisplay` component.

## Contributing

Feel free to submit issues or pull requests to improve the application. 

## License

This project is licensed under the MIT License.