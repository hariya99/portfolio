# import os
# import secrets
# from PIL import Image 
# from flask import current_app #, url_for
# # from flask_mail import Message

# # from flaskblog import mail  

# def save_prodile_picture(form_pic):

#     file_hex = secrets.token_hex(8)
#     _, f_ext = os.path.splitext(form_pic.filename)
#     picture_fn = file_hex + f_ext
#     picture_path = os.path.join(current_app.root_path, 'static', 'profile_pics', picture_fn)
    
#     # scale down the image to 125 px 
#     output_size = (125,125)
#     i = Image.open(form_pic)
#     i.thumbnail(output_size)

#     # save to file system
#     i.save(picture_path)

#     # form_pic.save(picture_path)

#     return picture_fn