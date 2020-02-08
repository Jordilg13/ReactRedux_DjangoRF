import pickle
import cv2
import tempfile
import os
import face_recognition
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import numpy as np


class Faces():
    def __init__(self, pickle_file, image_input, detection_method="hog"):
        self.image_input = image_input
        self.data = pickle.loads(open(pickle_file, "rb").read())       
        nparr = np.fromstring(image_input.read(), np.uint8)
        self.image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.boxes = face_recognition.face_locations(
            rgb,
            model=detection_method)
        self.encodings = face_recognition.face_encodings(rgb, self.boxes)
        self.detected_faces = self.detect_faces()
        if self.detected_faces is None:
            self.detected_faces = [[],[],[]]
        self.draw_faces()

    def detect_faces(self):
        names = []
        detected = []
        num_matches = []
        # loop over the facial embeddings
        for encoding in self.encodings:
            # attempt to match each face in the input image to our known
            # encodings
            matches = face_recognition.compare_faces(self.data["encodings"],
                                                    encoding)
            name = "Unknown"
            # check to see if we have found a match
            if True in matches:
                # find the indexes of all matched faces then initialize a
                # dictionary to count the total number of times each face
                # was matched
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}

                # loop over the matched indexes and maintain a count for
                # each recognized face face
                for i in matchedIdxs:
                    name = self.data["names"][i]
                    counts[name] = counts.get(name, 0) + 1

                # determine the recognized face with the largest number of
                # votes (note: in the event of an unlikely tie Python will
                # select first entry in the dictionary)
                # #print("------------")
                # #print(counts)
                # if counts[max(counts)] > 20:
                name = max(counts, key=counts.get)
                detected.append(name)
                num_matches.append(counts[max(counts)])
                # else:
                # name = "Unknown"
                # #print(detected)
                # #print(boxes[2])

            # update the list of names
            names.append(name)
            return [names, detected, num_matches]


    def draw_faces(self):        
        names = self.detected_faces[0]
        num_matches = self.detected_faces[2]

        a = zip(self.boxes, names, num_matches)
        complete_info_faces = {}
        # a = sorted(a, key=operator.itemgetter(1,2))
        individual_recognized_faces = {}
        unknown_faces = []


        for ((top, right, bottom, left), name, num_matches) in a:
            #print((top, right, bottom, left), name, num_matches)
            if name != "Unknown": 
                try:
                    individual_recognized_faces[name]
                except:
                    #print("-----First match")
                    complete_info_faces[name] = ((top, right, bottom, left))
                    individual_recognized_faces[name] = num_matches
                    continue

                
            
            if name == "Unknown":
                #print("-----Directly_Unknown")
                unknown_faces.append(((top, right, bottom, left)))
            elif num_matches > individual_recognized_faces[name]:
                #print("-----Has_More_Matches")
                # add previous face to unknown
                unknown_faces.append((complete_info_faces[name]))
                # #print("previous: "+str(complete_info_faces[name]))
                # #print("new: "+str((top, right, bottom, left)))
                # add new face
                complete_info_faces[name] = ((top, right, bottom, left))
                individual_recognized_faces[name] = num_matches
            else:
                #print("-----Else")
                unknown_faces.append(((top, right, bottom, left)))

        #print(individual_recognized_faces)
        # #print(unknown_faces)
        # loop over the recognized faces
        for name in individual_recognized_faces.keys():
            (top, right, bottom, left) = complete_info_faces[name]
            
            # #print((top, right, bottom, left), name)
            # draw the predicted face name on the image
            cv2.rectangle(self.image, (left, top), (right, bottom), (0, 255, 0), 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(self.image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                        0.75, (0, 255, 0), 2)

        # unknow faces
        for (top, right, bottom, left) in unknown_faces:
            # #print((top, right, bottom, left), name)
            # draw the predicted face name on the image
            cv2.rectangle(self.image, (left, top), (right, bottom), (0, 255, 255), 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(self.image, "", (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                        0.75, (0, 255, 0), 2)


        filename = str(self.image_input)
        #print(filename)
        cv2.imwrite("/drf/utils/face_recognition/output/"+filename+"_faces.jpg", self.image)

        # show the output image
        # cv2.imshow("Image", image)
        # cv2.waitKey(0)
