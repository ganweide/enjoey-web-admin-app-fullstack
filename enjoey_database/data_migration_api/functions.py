from slugify import slugify
import random
import string
import boto3
import logging
from botocore.exceptions import ClientError
from .models import App_user
client = boto3.client('cognito-idp', region_name='ap-southeast-1')
logger = logging.getLogger(__name__)

def generate_random_cognito_password():
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = ['^', '$', '*', '.',
                     '{', '}', '(', ')', '?', '-', '!', '@', '#', '%', '&', '/', '>', '<', '|', '_', '~', '+', '=']

    password_list = []
    for char in range(1, 3 + 1):
        password_list.append(random.choice(lowercase))

    for char in range(1, 2 + 1):
        password_list.append(random.choice(uppercase))

    for char in range(1, 3 + 1):
        password_list.append(random.choice(digits))

    for char in range(1, 2 + 1):
        password_list.append(random.choice(special_chars))

    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    print("char", char)

    pwd = ''.join(password_list)
    print(f"Your random password to use is: {pwd}")
    return pwd

def create_cognito_user(authenticated_user, user_model, pwd, profile_image_url):
    try:        
        response = client.admin_create_user(
            UserPoolId=authenticated_user.userPoolId,
            Username=user_model.email.strip(),
            UserAttributes=[
                {
                    'Name': 'name',
                    'Value': user_model.name
                },
                {
                    'Name': 'picture',
                    'Value': profile_image_url
                },
                {
                    'Name': 'email',
                    'Value': user_model.email
                },
                {
                    'Name': 'email_verified',
                    'Value': 'true'
                },
                {
                    'Name': 'phone_number',
                    'Value': user_model.phone
                },
                {
                    'Name': 'phone_number_verified',
                    'Value': 'true'
                },
                {
                    'Name': 'custom:user-id',
                    'Value': str(user_model.id)
                },
                {
                    'Name': 'custom:role',
                    'Value': user_model.roles[0]
                },
                {
                    'Name': 'custom:tenant-id',
                    'Value': authenticated_user.tenantId
                },
                {
                    'Name': 'custom:stroage',
                    'Value': authenticated_user.bucket
                },
            ],
            TemporaryPassword=pwd,
            MessageAction='SUPPRESS',
        )
        return response

    except ClientError as err:
        logger.error(
            "some error %s. Here's why: %s: %s", user_model.email,
            err.response['Error']['Code'], err.response['Error']['Message'])
        return err.response
    except Exception as e:
        print(e)
        return e
    
def get_staff_profile_image(staff):
    if staff.profileImage != None:
        media_storage = AvatarStorage()
        media_storage.bucket_name = settings.APP_PUBLIC_MEDIA_S3_BUCKET_NAME
        media_storage.location = "enjoey/user/avatar"
        profile_pic = media_storage.url(
            name=staff.profileImage.name)
        return profile_pic
    else:
        photoUrl = ''
        if staff.gender == 'Male':
            photoUrl = 'https://enjoey-public-bucket.s3.ap-southeast-1.amazonaws.com/avatar/male_avatar_2.png'
        else:
            photoUrl = 'https://enjoey-public-bucket.s3.ap-southeast-1.amazonaws.com/avatar/female_avatar_2.png'
        return photoUrl

