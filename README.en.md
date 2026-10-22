# RideAlong · 一路黔行

[简体中文](README.md) | **English**

RideAlong is a team Web course project focused on tourism and local culture in Guizhou, China. It combines destination content, map-based route queries, and user stories in a Django website.

The application uses server-rendered Django templates and SQLite. Leaflet and Folium display maps and driving routes supplied by external services.

## Demo

[Watch the project demonstration on Bilibili](https://www.bilibili.com/video/BV1i1421y7fA/)

## Features

- **Destination content:** a home page, city and culture pages, and five cultural feature pages.
- **Route queries:** select departure and destination cities and counties, look up their stored coordinates, request a driving route from OSRM, and display the path with start/end markers.
- **Interactive maps:** browse maps, select points, and use Esri reverse geocoding.
- **Travel stories:** story lists and detail pages, Markdown rendering, and logic for creating, editing, deleting, and uploading story images.
- **User accounts:** registration, login, logout, profile and avatar updates, and personal story lists. Large avatars are resized to fit within 300 × 300 pixels.
- **Administration:** a Django Admin entry point.

“My Trips” currently provides a page entry rather than a complete trip storage and management system.

## Technology

| Layer | Tools |
| --- | --- |
| Backend | Python, Django, Django ORM |
| Storage | SQLite |
| UI and interaction | Django Templates, HTML, CSS, JavaScript, jQuery, HTMX |
| Forms and content | django-crispy-forms, crispy-bootstrap5, django-mdeditor, Markdown |
| Maps and routes | Leaflet, Folium, OpenStreetMap tiles, Esri geocoding, OSRM |
| Image processing | Pillow |

## Project Layout

```text
ridealong/                 # Directory containing this README
├── manage.py              # Django command entry point
├── requirements.txt       # Original dependency list; requires cleanup
├── db.sqlite3             # Database included with the project
├── ridealong/             # Settings, URLs, WSGI and ASGI configuration
├── pages/                 # Home, city, culture and route selection pages
├── city/                  # City/county models and data loading command
├── route/                 # Map rendering and OSRM requests
├── story/                 # Story models, views and templates
├── users/                 # Profiles, forms, signals and templates
├── static/                # Shared images, styles and static assets
└── media/                 # Avatars, story images and media assets
```

## Local Setup with Conda

These instructions are derived from source inspection. Dependency installation and the complete application flow have not yet been verified in a clean environment. Use Python 3.10 to reproduce the historical dependencies rather than installing these old versions on Python 3.13.

### 1. Create an environment

Run in Anaconda Prompt or a terminal configured for Conda:

```shell
conda create -n ridealong python=3.10 pip -y
conda activate ridealong
python --version
```

### 2. Open the source directory

Work in the directory containing `manage.py`. If it is the repository root, open a terminal there. If the repository has an outer directory containing the application folder, run:

```shell
cd ridealong
```

### 3. Install dependencies

```shell
python -m pip install "Django==4.0.2" "django-crispy-forms==2.0" "crispy-bootstrap5==0.7" "Pillow==9.0.1" django-mdeditor Markdown folium polyline requests
```

### 4. Check configuration and database state

```shell
python manage.py check
python manage.py showmigrations
```

Keep the supplied `db.sqlite3` and `media/` to preserve existing content and images. If migrations are pending, copy the database to a backup before running:

```shell
python manage.py migrate
```

Only when setting up a new database that needs city and county records, run:

```shell
python manage.py load_data
```

**Warning: `load_data` deletes existing city and county records first and can affect related data through model relationships. Do not rerun it on the supplied demonstration database without reviewing and backing up the data.** It does not restore stories, accounts or media files.

### 5. Start the server

```shell
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Keep the terminal open and press `Ctrl+C` to stop.

For subsequent sessions, activate the environment, enter the source directory and run `python manage.py runserver`. Some map templates hard-code `http://localhost:8000`; changing the server port also requires updating those links.

### 6. Optional: create an administrator

```shell
python manage.py createsuperuser
```

Then visit `/admin/`. Regular users can register at `/register/`.

## Page Routes

| Path | Page |
| --- | --- |
| `/` | Home |
| `/city/` | City information |
| `/culture/` | Cultural content |
| `/route/` | Departure/destination selection |
| `/route/showmap` | Interactive point selection map |
| `/story/list/` | Story list |
| `/story/add/` | Create a story; login required |
| `/register/`, `/login/` | Registration and login |
| `/profile/` | Profile; login required |
| `/about/` | About |
| `/admin/` | Administration |

## Team Contributions and Assets

This is a team course project. The source alone does not establish individual ownership of modules, so this document does not attribute all team work to one contributor. For a personal portfolio, add the pages, modules and implementation details you personally worked on.

This document does not declare an open-source license. Confirm applicable permissions before reuse or redistribution, and retain required map and asset attribution.
