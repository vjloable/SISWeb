import os

import cloudinary
import cloudinary.uploader
import cloudinary.api


from dotenv import load_dotenv

load_dotenv()

class CloudService:
    def __init__(self):
        self.cloud_name = os.getenv('CLOUD_NAME')
        self.api_key = os.getenv('CLOUD_KEY')
        self.api_secret = os.getenv('CLOUD_SECRET')
        print("Initialize cloud")

    def configure(self):
        config = cloudinary.config(
            cloud_name = self.cloud_name,
            api_key = self.api_key,
            api_secret = self.api_secret,
            secure = True
        )
        print("Configuring cloud")
        print("Credentials: ", config.cloud_name, config.api_key, "\n")

    @staticmethod
    def upload(image, uid, category):
        response = {}
        try:
            result = cloudinary.uploader.upload(
                image,
                public_id = "{}/{}".format(category, uid),
                folder = "sisweb",
                resource_type = "image",
                type = "upload",
                overwrite = True,
                phash = True,
                eager = [{"width": 500, "height": 500, "crop": "fill"}]
            )
            response = {'success': True, 'results': {"url": result["url"]}}
        except:
            response = {'success': False, 'results': {"url": ""}}
        finally:
            return response

    @staticmethod
    def delete(uid, category):
        response = {}
        try:
            result = cloudinary.uploader.destroy(f"sisweb/{category}/{uid}")
            response = {'success': True, 'results': result}
        except:
            response = {'success': False, 'results': "No file deleted"}
        finally:
            return response

    @staticmethod
    def rename(old_uid, new_uid, category):
        response = {}
        try:
            result = cloudinary.uploader.rename(f"sisweb/{category}/{old_uid}", f"sisweb/{category}/{new_uid}", invalidate = True)
            response = {'success': True, 'results': {"url": result["url"]}}
        except:
            response = {'success': False, 'results': {"url": ""}}
        finally:
            return response
