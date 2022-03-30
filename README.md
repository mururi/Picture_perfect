# Picture Perfect
#### Django Gallery Web App, Mar 27 2022 
#### By **Dennis Kiboi** 

## Description 
This is Django photo gallery web app where users can view photos and search different categories and locations.

![Photo Gallery Web App](static/picture_perfect.png)

## How to Use
### Requirements
* A computer, tablet or phone
* Access to the internet

### View Live Site 
Ensure that your device of choice has a browser installed.
Click the link provided below to view the site.

https://picture-perfect-app.herokuapp.com/

### Using the App
The user can navigate the web app easily and be able to:
* View different photos that interest them
* Click on a single photo to expand it and also view the details of the photo
* Search different categories of photos
* Copy a link to the photo to share with their friends
* View photos based on the location they were taken


## Run Locally
### Setup/Installation Requirements
To run this app locally, you need a PC with the following installed:
* Python 3.+
* pip

### Installation Process
1. Clone this repository using

    ```bash
      git clone https://github.com/mururi/Picture_perfect.git
    ```

    or by downloading a ZIP file of the code.
  
2. The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
3. Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands to do so:

    ```bash
      python3 -m venv --without-pip virtual 
    ```

    ```bash
      source virtual/bin/activate
    ```

    ```bash
      curl https://bootstrap.pypa.io/get-pip.py | python
    ```
 
4. Download the all dependencies in the requirements.txt using

    ```bash
      pip install -r requirements.txt
    ```
5. Open the terminal and navigate to the project directory and run the following commands to launch the program.

    ```bash
    python manage.py runserver
    ```

## Technologies Used
* Django
* Python
* HTML
* CSS/Bootstrap
* Heroku

## Support and Contact Details
Incase of any query, need for collaboration or issues with this code, feel free to reach me at
dennis.kiboi@student.moringaschool.com

## License 
MIT License

Copyright &copy; 2022 Dennis Kiboi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.