from django.conf import settings
from django.core.management import call_command

def main():
    # the minimum necessary to get Django running
    settings.configure(
        INSTALLED_APPS=(
            'scielo_extensions',
            'django_coverage',
        ),
        DATABASE_ENGINE='sqlite3'
    )
    settings.PAGINATION__ITEMS_PER_PAGE = 5
    settings.DOCUMENTATION_BASE_URL = ''

    call_command('test_coverage', 'scielo_extensions')

if __name__ == '__main__':
    main()
