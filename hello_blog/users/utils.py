import cloudinary.api
import cloudinary.uploader
import os
if os.path.exists("env.py"):
    import env


#  create a function that uplaods the users image file
# to cloudinary and then return its url so it can be saved in the database.
#  The url uses cloudinary dynamic functions to resize the image
#  while keeping the users face in the image
def save_user_image(form_image):
    # gets cloudinaries response upon upload
    response = cloudinary.uploader.upload(form_image)
    # get cloud name from os
    cloud_name = os.environ.get("CLOUD_NAME")
    # the first part of url
    start_url = f"https://res.cloudinary.com/{cloud_name}/"
    #  set image sizing details
    image_sizing = "image/upload/w_200,h_200,c_fill,g_face/"
    # set details from response
    version = response["version"]
    public_id = response["public_id"]
    image_format = response["format"]

    # then return the full url
    return f"{start_url}{image_sizing}v{version}/{public_id}.\
{image_format}"
