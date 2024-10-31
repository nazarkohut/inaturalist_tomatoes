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


def format_inaturalist_data(result: list[dict], curr_id: int):
    parsed_objects = [{
        # photo urls
        'photos': [
            {
                'image_url': photo['url'],
                'original_image_url': replace_square_image_with_original(photo['url']),
                'original_width': photo['original_dimensions']['width'],
                'original_height': photo['original_dimensions']['height'],
                'license_code': photo['license_code'],
                'attribution': photo['attribution'],
            } for photo in res['photos']
        ],
        'observation_id': curr_id, # partition key in DynamoDB
        # date and time related fields
        'time_observed_at_date': res['time_observed_at'],
        'observed_on_date': res['observed_on_details']['date'],
        'observed_on_year': res['observed_on_details']['year'],
        'observed_on_month': res['observed_on_details']['month'],
        'observed_on_week': res['observed_on_details']['week'],
        'observed_on_day': res['observed_on_details']['day'],
        'observed_on_hour': res['observed_on_details']['hour'],

        # location fields
        'location': res['location'],
        'place_guess': res['place_guess'],

        # time zone related fields
        'observed_time_zone': res['observed_time_zone'],
        'created_time_zone': res['created_time_zone'],
        'time_zone_offset': res['time_zone_offset'],

        # names related fields
        'english_common_name': res['taxon']['english_common_name'],
        'preferred_common_name': res['taxon']['preferred_common_name'],
        'taxon_name': res['taxon']['name'],
        'description': res['description'],

        # identifications info
        'identifications_most_disagree': res['identifications_most_disagree'],
        'identifications_most_agree': res['identifications_most_agree'],

        # other
        'quality_grade': res['quality_grade'],
        'uri': res['uri'],  # just in case we need to check out additional info

    } for res in result]
    return parsed_objects
