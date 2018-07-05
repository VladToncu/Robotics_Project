import eigenfaces

class security_guard:

    def __init__(self):
        print "Initialising security_guard class\n"



if __name__ == "__main__":
    print "Executing main code\n"
    sec_guard = security_guard()
    face_recog = eigenfaces.FaceRecog()


    while True:
        # Search for faces to process
        # Once we find one,
        print "Got to while true loop"