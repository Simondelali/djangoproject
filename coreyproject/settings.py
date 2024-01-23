"""
Django settings for coreyproject project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+q_sdp=!rqt2u)*2tnov5xl0&pcv9x%ug2l*l8f_4)dr047vc6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'crispy_forms',
    'crispy_bootstrap4',
    'ckeditor',
    'tinymce',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'coreyproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'coreyproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'    
   
TIME_ZONE = 'UTC'   
          
USE_I18N = True
     
USE_TZ = True        
   

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'blog-home'  
    
LOGIN_URL = 'login'    

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')


TINYMCE_DEFAULT_CONFIG = {
    'height': '520px',
    'width': '680px',
    'menubar': 'file edit view insert format tools table help',
    'plugins': (
        'advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code '
        'fullscreen insertdatetime media table paste codesample'
    ),
    'toolbar': (
        'undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft '
        'aligncenter alignright alignjustify | outdent indent | numlist bullist checklist | forecolor '
        'backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | '
        'fullscreen preview save print | insertfile image media pageembed template link anchor codesample | '
        'a11ycheck ltr rtl | showcomments addcomment code'
    ),
    'custom_undo_redo_levels': 10,
    'content_css': [
        'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.0/codemirror.min.css',
        'https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.0/theme/monokai.min.css',
    ],
    'setup': 'function(editor) { editor.on("init", function() { tinymce.ScriptLoader.load("https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.0/codemirror.min.js"); tinymce.ScriptLoader.load("https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.0/mode/javascript/javascript.min.js"); tinymce.ScriptLoader.load("https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.0/mode/htmlmixed/htmlmixed.min.js"); }); }',
    'codesample_languages': [
        {'text': 'HTML/XML', 'value': 'xml'},
        {'text': 'JavaScript', 'value': 'javascript'},
        {'text': 'CSS', 'value': 'css'},
        {'text': 'Python', 'value': 'python'},
        {'text': 'Java', 'value': 'java'},
        {'text': 'C', 'value': 'c'},
        {'text': 'C#', 'value': 'csharp'},
        {'text': 'C++', 'value': 'cpp'},
        {'text': 'PHP', 'value': 'php'},
        {'text': 'Ruby', 'value': 'ruby'},
        {'text': 'Go', 'value': 'go'},
        {'text': 'Scala', 'value': 'scala'},
        {'text': 'Swift', 'value': 'swift'},
        {'text': 'TypeScript', 'value': 'typescript'},
        {'text': 'SQL', 'value': 'sql'},
        {'text': 'YAML', 'value': 'yaml'},
        {'text': 'JSON', 'value': 'json'},
        {'text': 'Docker', 'value': 'docker'},
        {'text': 'Markdown', 'value': 'markdown'},
    ],
    'codesample_global_prismjs': True, 
}
