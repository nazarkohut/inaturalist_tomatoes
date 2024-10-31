import re

def replace_square_image_with_original(url: str) -> str:
    """
    Replace 'square' with 'original' in the given URL, but only in the image filename.

    Parameters:
    url (str): The URL to be modified.

    Returns:
    str: The modified URL with 'square' replaced by 'original' in the filename.
    """
    # Use regex to find 'square' before the image extension
    modified_url = re.sub(r'/(square)(\.\w+)$', r'/original\2', url)
    return modified_url


if __name__ == '__main__':
    url = 'https://inaturalist-open-data.s3.amazonaws.com/photos/445474362/square.jpeg'
    modified_url = replace_square_image_with_original(url)
    print(modified_url)  # Output: https://inaturalist-open-data.s3.amazonaws.com/photos/445474362/original.jpeg

    # Testing with a URL that contains 'square' elsewhere
    url_with_square_elsewhere = 'https://example.com/path/to/square_image/square.jpeg'
    modified_url_elsewhere = replace_square_image_with_original(url_with_square_elsewhere)
    print(modified_url_elsewhere)  # Output: https://example.com/path/to/square_image/original.jpeg
