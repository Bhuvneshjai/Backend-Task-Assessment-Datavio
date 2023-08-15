# About Task Detail

#### 1. Project Setup
* Created a virtual environment to isolate the project dependencies.
* Installed necessary Python packages including Django, Django Rest Framework, JWT support, Postgres driver, BeautifulSoup, and Requests.

#### 2. JWT Authentication
* Configured Django settings to use the djangorestframework_simplejwt for JWT authentication.
* Defined JWT token lifespan using timedelta.

#### 3. Database Setup
* Used PostgreSQL as the database and configured the Django project to connect to it.

#### 4. Django Model: Product
* Created a Product model that has fields such as user, URL, title, price, description, review count, ratings, and media count. This model will represent the scraped data from Flipkart.

#### 5. Flipkart Scraper API
* Defined a DRF APIView (ScrapingView) that accepts a Flipkart URL, scrapes the product details, and saves them in the database.
* For scraping, used BeautifulSoup and requests to fetch the webpage and parse its content.
* Ensured that only authenticated users can access the scraping API.

#### 6. URLs Configuration
* Configured URLs to route requests to the correct views.
* Defined paths for Django's admin and the scraping endpoint.

#### 7. Error Handling
* Incorporated checks to handle scenarios such as unauthenticated access, missing URL in the request, invalid URL, and scraping failures.

#### 8. Issues & Resolutions
* Encountered and resolved issues with the INSTALLED_APPS setting (the flipkart_scraper app needed to be added).
* Addressed issues with JWT configurations such as missing timedelta import and corrected the naming for the Django Rest Framework in the INSTALLED_APPS.
* Dealt with the 401 Unauthorized error which indicates a need for valid authentication to access the API endpoint.
* This is a high-level breakdown of the project and the steps you've undertaken. Each point can be expanded further into detailed steps and considerations based on your specific project requirements.
