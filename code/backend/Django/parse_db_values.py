from urllib.parse import urlparse


def get_db_components(db_url):
    result = urlparse(db_url)
    
    # Special handling for SQLite URLs
    if db_url.startswith("sqlite://"):
        if db_url == "sqlite://:memory:":
            # Special case for SQLite memory database
            return {
                'engine': 'sqlite',
                'username': None,
                'password': None,
                'host': None,
                'port': None,
                'database_name': ':memory:'
                }
        else:
            # Handle file paths for SQLite
            return {
                'engine': 'sqlite',
                'username': None,
                'password': None,
                'host': None,
                'port': None,
                'database_name': result.path[1:]  # File path as database name
                }
    
    # Standard handling for other database engines
    return {
        'engine': result.scheme,
        'username': result.username,
        'password': result.password,
        'host': result.hostname,
        'port': result.port,
        'database_name': result.path[1:] if result.path else None
        }


# Testing the function with different database URLs
urls = [
    # TESTING ENVIRONMENT
    "sqlite://:memory:",
    "sqlite:///tmp/mydatabase.db",
    # STAGING ENVIRONMENT
    "postgres://staging_user:staging_password@staging_host:5432/staging_db",
    # PRODUCTION ENVIRONMENT
    "postgres://prod_user:prod_password@prod_host:5432/prod_db"
    ]

for url in urls:
    components = get_db_components(url)
    print(components)