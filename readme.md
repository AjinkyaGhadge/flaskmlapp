Note: This implementation was tested on Ubuntu 20.04, which is the recommended environment.
Team members: Nikita Agarwal, Varun Prasad, Ajinkya Ghadge

### Note: The submissions for all the team members is same


# Steps to build and test
1. Run the command ```sudo docker build -t flask-mlapplication:latest .``` and wait for the build process to complete
2. Run the command ```sudo docker run --name flask-mlapplication -p 5000:5000 flask-mlapplication```, this will start the server.
3. Open the testfolder folder, and paste the images you want to test
4. Open another terminal Run the python test script using the command ```python testscript.py```