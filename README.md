# Final project for courses Web Technologies & Application Development, spring 2022 NTNU


## Project description
The project covers both frontend and backend for a bicycle rental website. The company is called KRRR - Keep Roling Roling Roling.

## Project navigation
- HTML Files: Django/ WebAppProj/ templates
- JS Files: Django/ WebAppProj/ static/ js
- CSS Files: Django/ WebAppProj/ static/ css
- Images: Django/ WebAppProj/ static/ img

## User groups
1. Customer, can do the following:
   - signup
   - login
   - select products
   - add products to shopping cart
   - send in an order
   - write a comment for a product
   - edit their own comments
   - see comments from other users

2. Site owner (admin), can do the following:
   - add new products (pictures can be added as URLs to external images)
   - update products
   - delete products
   - see all user orders
   - mark an order as processed
   - see all user comments fo reach product
   - delete any user comment

## Requirements
All of the modules required to run the projects are listed in `requirements.txt` file.

## Environment variables
The project needs two environment variables:
`SECRET_KEY` and `SENDGRID_API_KEY`.

## Configuration
To configure the project, open `Django/WebAppProj/WebAppProj/settings.py`. 
1. Set `MEDIA_ROOT` in line 22 to match your domain name or comment this line and uncomment line 21 if you are running the project locally.
2. In line 37 add your domain name and server's IP to the list of allowed hosts.
3. Set `STATIC_ROOT` in line 136 to match your domain name or change it to an empty string if you are running the project locally.
4. Configure the email sending host in lines 150 - 156 or comment them out if you don't have an email provider prepared. Then you won't be able to get emails for password changing.

## Usage
To run the project, use the following commands:
```
python Django/WebAppProj/manage.py makemigrations
python Django/WebAppProj/manage.py migrate
python Django/WebAppProj/manage.py runserver
```
Open in your browser at http://localhost:8000 or http://127.0.0.1:8000/
