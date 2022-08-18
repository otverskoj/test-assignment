class DBCantHandleQuery(Exception):
    """DB can't process your query."""


class UserDoesNotExist(Exception):
    """Such User does not exist in system."""
