# socials/twitter_api.py

from django.conf import settings
from social_django.models import UserSocialAuth
import twitter


def post_twitter(user, twi_content, image_box):
    social_auth = UserSocialAuth.objects.get(user=user, provider='twitter')

    client_key = social_auth.extra_data['access_token']['oauth_token']
    client_secret = social_auth.extra_data['access_token']['oauth_token_secret']

    auth = twitter.OAuth(
        consumer_key=settings.SOCIAL_AUTH_TWITTER_KEY,  # settings.pyに設定しているトークン
        consumer_secret=settings.SOCIAL_AUTH_TWITTER_SECRET,  # settings.pyに設定しているシークレットキー
        token=client_key,
        token_secret=client_secret
    )
    t = twitter.Twitter(auth=auth)

    t_upload = twitter.Twitter(domain='upload.twitter.com',
                               auth=auth)

    id_imgs = []
    for image in image_box:
        id_img = t_upload.media.upload(media=image)["media_id_string"]
        id_imgs.append(id_img)

    charas = ' \n '.join(twi_content)
    content = '私が好きなものは…\n\n' + twi_content + '\n\nです！' + '\n#Favorite4' + '\nurl'

    status_update = t.statuses.update(status=content, media_ids=",".join(id_imgs))

    return status_update
