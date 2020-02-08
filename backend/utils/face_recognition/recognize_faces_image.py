# USAGE
# python recognize_faces_image.py --encodings encodings.pickle --image examples/example_01.png

# import the necessary packages
import face_recognition
import argparse
import pickle
import cv2
import operator


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-e", "--encodings", required=True,
                help="path to serialized db of facial encodings")
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
ap.add_argument("-d", "--detection-method", type=str, default="cnn",
                help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args())

# load the known faces and embeddings
print("[INFO] loading encodings...")
data = pickle.loads(open(args["encodings"], "rb").read())

# load the input image and convert it from BGR to RGB
image = cv2.imread(args["image"])
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# detect the (x, y)-coordinates of the bounding boxes corresponding
# to each face in the input image, then compute the facial embeddings
# for each face
print("[INFO] recognizing faces...")
boxes = face_recognition.face_locations(rgb,
                                        model=args["detection_method"])
encodings = face_recognition.face_encodings(rgb, boxes)

# initialize the list of names for each face detected
names = []
detected = []
num_matches = []
# loop over the facial embeddings
for encoding in encodings:
    # attempt to match each face in the input image to our known
    # encodings
    matches = face_recognition.compare_faces(data["encodings"],
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
            name = data["names"][i]
            counts[name] = counts.get(name, 0) + 1

        # determine the recognized face with the largest number of
        # votes (note: in the event of an unlikely tie Python will
        # select first entry in the dictionary)
        # print("------------")
        # print(counts)
        # if counts[max(counts)] > 20:
        name = max(counts, key=counts.get)
        detected.append(name)
        num_matches.append(counts[max(counts)])
        # else:
        # name = "Unknown"
        # print(detected)
        # print(boxes[2])

    # update the list of names
    names.append(name)


a = zip(boxes, names, num_matches)
complete_info_faces = {}
# a = sorted(a, key=operator.itemgetter(1,2))
individual_recognized_faces = {}
unknown_faces = []

print("---------------------------------------------------------")

for ((top, right, bottom, left), name, num_matches) in a:
    print((top, right, bottom, left), name, num_matches)
    if name != "Unknown": 
        try:
            individual_recognized_faces[name]
        except:
            print("-----First match")
            complete_info_faces[name] = ((top, right, bottom, left))
            individual_recognized_faces[name] = num_matches
            continue

        
    
    if name == "Unknown":
        print("-----Directly_Unknown")
        unknown_faces.append(((top, right, bottom, left)))
    elif num_matches > individual_recognized_faces[name]:
        print("-----Has_More_Matches")
        # add previous face to unknown
        unknown_faces.append((complete_info_faces[name]))
        # print("previous: "+str(complete_info_faces[name]))
        # print("new: "+str((top, right, bottom, left)))
        # add new face
        complete_info_faces[name] = ((top, right, bottom, left))
        individual_recognized_faces[name] = num_matches
    else:
        print("-----Else")
        unknown_faces.append(((top, right, bottom, left)))

print("---------------------------------------------------------")
print(individual_recognized_faces)
# print(unknown_faces)
# loop over the recognized faces
for name in individual_recognized_faces.keys():
    (top, right, bottom, left) = complete_info_faces[name]
    
    # print((top, right, bottom, left), name)
    # draw the predicted face name on the image
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
    y = top - 15 if top - 15 > 15 else top + 15
    cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                0.75, (0, 255, 0), 2)

# unknow faces
for (top, right, bottom, left) in unknown_faces:
    # print((top, right, bottom, left), name)
    # draw the predicted face name on the image
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 255), 2)
    y = top - 15 if top - 15 > 15 else top + 15
    cv2.putText(image, "", (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                0.75, (0, 255, 0), 2)


filename = args["image"].split("/")[3].split(".")[0]
cv2.imwrite("/drf/utils/face_recognition/output/"+filename+"_faces.jpg", image)

# show the output image
# cv2.imshow("Image", image)
# cv2.waitKey(0)
