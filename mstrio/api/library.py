from mstrio.utils.helper import response_handler


def get_document(connection, id, error_msg=None):
    """Get information for a document with document Id.

    Args:
        connection: MicroStrategy REST API connection object
        id (string): Document ID
        error_msg (string, optional): Custom Error Message for Error Handling

    Returns:
        Complete HTTP response object.
    """
    url = connection.base_url + '/api/library/' + id
    response = connection.session.get(url=url)
    if not response.ok:
        if error_msg is None:
            error_msg = "Error getting document"
        response_handler(response, error_msg)
    return response


def unpublish_document(connection, id, error_msg=None):
    """Unpublish a previously published document. This makes the document no
    longer available in the library of each user it was originally published
    to.

    Args:
        connection: MicroStrategy REST API connection object
        id (string): Document ID
        error_msg (string, optional): Custom Error Message for Error Handling

    Returns:
        Complete HTTP response object.
    """
    url = connection.base_url + f'/api/library/{id}'
    response = connection.session.delete(url=url)
    if not response.ok:
        if error_msg is None:
            error_msg = "Error unpublishing document"
        response_handler(response, error_msg)
    return response


def unpublish_document_for_user(connection, document_id, user_id,
                                error_msg=None):
    """Unpublish a previously published document. This makes the document no
    longer available in the library of each user specified in `user_id`

    Args:
        connection: MicroStrategy REST API connection object
        document_id (string): Document ID
        user_id (string): user ID
        error_msg (string, optional): Custom Error Message for Error Handling

    Returns:
        Complete HTTP response object.
    """
    connection._validate_project_selected()
    url = connection.base_url + f'/api/library/{document_id}/recipients/{user_id}'
    response = connection.session.delete(url=url)
    if not response.ok:
        if error_msg is None:
            error_msg = "Error unpublishing document"
        response_handler(response, error_msg)
    return response


def get_library(connection, error_msg=None):
    """Get the library for the authenticated user.

    Args:
        connection: MicroStrategy REST API connection object
        error_msg (string, optional): Custom Error Message for Error Handling

    Returns:
        Complete HTTP response object.
    """
    url = connection.base_url + '/api/library'
    response = connection.session.get(url=url,
                                      headers={'X-MSTR-ProjectID': None})
    if not response.ok:
        if error_msg is None:
            error_msg = "Error getting library"
        response_handler(response, error_msg)
    return response


def publish_document(connection, body, error_msg=None):
    """Publish a document to users or user groups in a specific project.

    Args:
        connection: MicroStrategy REST API connection object
        body: JSON-formatted definition of the dataset. Generated by
            `utils.formjson()`.
        error_msg (string, optional): Custom Error Message for Error Handling

    Returns:
        Complete HTTP response object.
    """
    connection._validate_project_selected()
    url = connection.base_url + '/api/library'
    response = connection.session.post(url=url, json=body)
    if not response.ok:
        if error_msg is None:
            error_msg = f"Error publishing document {body['id']}"
        response_handler(response, error_msg)
    return response