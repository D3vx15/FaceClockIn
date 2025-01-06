# FaceClockIn

-AIM OF THE PROJECT:
A facial recognition system can streamline attendance tracking in schools, ensuring 
that students are present and accounted for. This software is a facial attendance 
system made using Python and SQL. The system uses a facial recognition module 
(cv2) and a camera to identify individuals and record their attendance information 
in a database.

-DOCUMENTATION
To efficiently store data in tabular form, we use MySQL. Python is used to send 
commands to MySQL in a procedural manner so that the user never needs to 
manually type in commands.
The module used to connect MySQL to Python is 'mysql.connector'. Python is called 
the 'front end' and MySQL is the 'back end'.

Some of the main commands are:-
1. connect() - Returns a MySQL connection object if the connection is stable. The 
arguments are host, database, user, and password.
2. cursor() - Creates a cursor object to perform various functions.
3. execute() - Runs the SQL query passed as argument(string).
4. fetchall() - Fetches all the rows of a query's result, with all the rows as a list of 
tuples.
5. cursor.close() and connection.close() - are used to close database cursors and 
connections, respectively, to prevent resource leaks and ensure proper 
database management.
6. connection.commit() - used to confirm the changes made by the user and that 
they are reflected in the database.
Description of other modules used:

--cv2 (OpenCV)
 Purpose: OpenCV is a comprehensive open-source computer vision library. 
It provides a wide range of functions for image processing, video analysis, 
and object detection.

 Key Commands:
o cv2.imread(): Reads an image file.
o cv2.imshow(): Displays an image.
o cv2.waitKey(): Waits for a key press.
o cv2.imwrite(): Writes an image to a file.
o cv2.cvtColor(): Converts an image from one color space to another.
o cv2.resize(): Resizes an image.

--dlib
 Purpose: dlib is a C++ toolkit for machine learning, including facial 
recognition. It offers efficient algorithms for face detection, landmark 
localization, and face recognition.

 Key Commands:
o dlib.get_frontal_face_detector(): Creates a face detector.
o dlib.shape_predictor(): Loads a pre-trained shape predictor.
o dlib.face_recognition_model_v1(): Loads a pre-trained face recognition 
model.

--CMake
 Purpose: CMake is a build system generator that can be used to manage the 
compilation process for C++ projects, including dlib. It simplifies the process 
of building projects across different platforms.

 Key Commands:
o cmake -B build: Creates a build directory.
o cmake --build build: Builds the project.

--face_recognition
 Purpose: face_recognition is a Python wrapper for dlib's face recognition 
functions. It provides a simplified interface for face detection, landmark 
localization, and face encoding.

 Key Commands:
o face_recognition.load_image_file(): Loads an image file.
o face_recognition.face_locations(): Detects faces in an image.
o face_recognition.face_encodings(): Encodes faces into numerical 
representations.
o face_recognition.compare_faces(): Compares two face encodings

