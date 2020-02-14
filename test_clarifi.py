from clarifai.rest import ClarifaiApp
import cv2, pprint


app = ClarifaiApp(api_key="ba60a25dbcc94c3f90948768264d7fac")

model = app.public_models.general_model
response = model.predict_by_filename("./backend/utils/face_recognition/examples/original/jordi.jpg")

# print(app.public_models.face_detection_model)
# model = app.models.get("face-v1.3")
# image = ClImage(url="./jordi.jpg")
# model.predict([image])
pprint.pprint(response)
# print(response["outputs"][0]['data']['regions'])
# array_faces = []
# for face, i in zip(response["outputs"][0]['data']['regions'], range(len(response["outputs"][0]['data']['regions']))):
#     # print("person "+str(i))
#     array_faces.append([])
#     for facecoords in face['region_info']['bounding_box']:
#         array_faces[i].append(face['region_info']['bounding_box'][facecoords])

# pprint.pprint(array_faces)
# image = cv2.imread("./jordi.jpg")
# for top, left, bottom, right in array_faces:
#     cv2.rectangle(image, (int(left), int(top)),
#                   (int(right), int(bottom)), (0, 255, 255), 2)
#     y = top - 15 if top - 15 > 15 else top + 15
#     cv2.putText(image, "test", (left, y), cv2.FONT_HERSHEY_SIMPLEX,
#                 0.75, (0, 255, 0), 2)

# cv2.imshow("Image", image)
# cv2.waitKey(0)
