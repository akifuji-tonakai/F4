from .settings_common import *


# デバッグモードを有効にするかどうか(本番運用では必ずFalseにする)
DEBUG = False

# 許可するホスト名のリスト
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]

# 静的ファイルを配置する場所
STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_ROOT = '/usr/share/nginx/html/media'

# # Amazon SES関連設定
# AWS_SES_ACCESS_KEY_ID = os.environ.get('AWS_SES_ACCESS_KEY_ID')
# AWS_SES_SECRET_ACCESS_KEY = os.environ.get('AWS_SES_SECRET_ACCESS_KEY')
# EMAIL_BACKEND = 'django_ses.SESBackend'

# ロギング
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#
#     # ロガーの設定
#     'loggers': {
#         # Djangoが利用するロガー
#         'django': {
#             'handlers': ['file'],
#             'level': 'INFO',
#         },
#         # diaryアプリケーションが利用するロガー
#         'diary': {
#             'handlers': ['file'],
#             'level': 'INFO',
#         },
#     },
#
#     # ハンドラの設定
#     'handlers': {
#         'file': {
#             'level': 'INFO',
#             'class': 'logging.handlers.TimedRotatingFileHandler',
#             'filename': os.path.join(BASE_DIR, 'logs/django.log'),
#             'formatter': 'prod',
#             'when': 'D',  # ログローテーション(新しいファイルへの切り替え)間隔の単位(D=日)
#             'interval': 1,  # ログローテーション間隔(1日単位)
#             'backupCount': 7,  # 保存しておくログファイル数
#         },
#     },
#
#     # フォーマッタの設定
#     'formatters': {
#         'prod': {
#             'format': '\t'.join([
#                 '%(asctime)s',
#                 '[%(levelname)s]',
#                 '%(pathname)s(Line:%(lineno)d)',
#                 '%(message)s'
#             ])
#         },
#     }
# }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'production': {
            'format': '%(asctime)s [%(levelname)s] %(process)d %(thread)d '
                      '%(pathname)s:%(lineno)d %(message)s'
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'logs/django.log',  #環境に合わせて変更
            'formatter': 'production',
            'level': 'INFO',
        },
    },
    'loggers': {
        # 自作したログ出力
        '': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
        # Djangoの警告・エラー
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
