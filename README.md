# wiki

## Overview
This project is an online encyclopedia that functions like Wikipedia. It's a part of Harvard's CS50 Web Programming with Python and JavaScript course. It includes functionalities for creating new entries, editing existing ones, and searching within entries.

## Key Features
- **View Entry:** Allows users to click on an entry name to go directly to that entry page.
- **Index Page:** Lists all names of encyclopedia entries.
- **Search:** Lets users type a query into the search box in the sidebar to find an encyclopedia entry.
- **New Page:** Allows users to add new encyclopedia entries.
- **Edit Page:** Allows users to edit existing encyclopedia entries.
- **Random Page:** Takes users to a random encyclopedia entry.

## Setup
1. **Clone this repository**

    ```bash
    git clone https://github.com/qildeli/wiki.git
    ```

2. **Navigate into the repository's directory**

    ```bash
    cd wiki
    ```

3. **Create a virtual environment** (optional)

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the application**

    ```bash
    python manage.py runserver
    ```
