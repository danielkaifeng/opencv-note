
### imread / imwrite
```
img = cv2.imread("0.png")
cv2.imwrite("2.png", img)
```

### resize
```
img = cv2.resize(img, (512, 512))

#enlarge x4
img = cv2.resize(img, (img.shape[1]*4, img.shape[0]*4))
```

### crop
```
img = img[x:x+h, y:y+w]
```


### findContour

```
ret, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
contours, hier = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,0,0), 8)
```

### canny

`img = cv2.Canny(img,s1,s2)`

### affine tranform by triangulation
```
rect = (0, 0, 500, 500)
subdiv = cv2.Subdiv2D(rect)

keypoints = [(random.randint(0, 500), random.randint(0, 500)) for x in range(10)]
for p in keypoints:
     subdiv.insert(p)

#Delaunay Triangulation
triangleList = subdiv.getTriangleList();

```
