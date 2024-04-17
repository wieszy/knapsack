from os import environ

SESSION_CONFIGS = [
    dict(
        name="knapsack",
        app_sequence=[
            "welcome_prolific",
            "svo_en",
            "WMspan",
            "knapsack_sp_intro",
            "knapsack_sp_tasks",
            "knapsack_sp_results",
            "demographics",
        ],
        num_demo_participants=12,
        budget=100,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

ROOMS = [
    {
        'name': 'prolific',
        'display_name': 'Prolific'
    }
]

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = "en"

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = "EUR"
USE_POINTS = True

ADMIN_USERNAME = "admin"
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = "9815831165721"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'otree_db_d8k9',
        'USER': 'otree_db_d8k9_user',
        'PASSWORD': 'o29ssobrJxq7guG4ph3qFvM6gMGC82IM',
        'HOST': 'dpg-cofvgs779t8c73ccd5mg-a',
        'PORT': '5432',
    }
}

