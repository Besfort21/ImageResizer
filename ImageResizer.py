from PIL import Image
import userpaths


def resize_image(imageLocation, sizel, size2):
    my_docs = userpaths.get_my_pictures()
    imgLoc = imageLocation.strip('"')
    image = Image.open(imgLoc)

    print(f"Current size : {image.size}")

    resized_image = image.resize((sizel, size2))

    resized_image.save(my_docs + "/ImageResizerResult_" +
                       "("+str(size1)+","+str(size2)+")" + '.jpeg')


imagelocation = input(' Enter Location: ')
size1 = int(input(' Enter Width: '))
size2 = int(input('Enter Length: '))
resize_image(imagelocation, size1, size2)
