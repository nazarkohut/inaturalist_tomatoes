import copy

from local_code.utils.url_transformers import replace_square_image_with_original


# def flat_format_inaturalist_data(result: list[dict]): # TODO: rewrite this function in case of a need
#     # Flatten the 'photos' key for simpler DataFrame structure
#     flat_data = []
#     for entry in result:
#         for photo in entry['photos']:
#             flat_entry = {**entry}  # make a shallow copy of the entry
#             flat_entry.update(photo)  # add photo details to the entry
#             flat_entry.pop('photos', None)  # remove original photos key
#             flat_data.append(flat_entry)
#
#     return flat_data

def single_table_format_inaturalist_data(result: list[dict], curr_id: int):
    parsed_objects = list()
    for res in result:
        curr_observation_data = {
            'observation_id': curr_id,
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
        } # dbeaver, duckDB(plugin)

        for photo_data in res['photos']:
            # photo_data
            curr_observation_photo_record = copy.deepcopy(curr_observation_data)

            curr_observation_photo_record['image_url'] = photo_data['url']
            curr_observation_photo_record['original_image_url'] = replace_square_image_with_original(photo_data['url'])
            curr_observation_photo_record['original_width'] = photo_data['original_dimensions']['width']
            curr_observation_photo_record['original_height'] = photo_data['original_dimensions']['height']
            curr_observation_photo_record['license_code'] = photo_data['license_code']
            curr_observation_photo_record['attribution'] = photo_data['attribution']
            parsed_objects.append(copy.deepcopy(curr_observation_photo_record))

    return parsed_objects


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
        'observation_id': curr_id,
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


def format_two_table_inaturalist_data(result: list[dict], curr_id: int):
    observations_data, photos_data = [], []
    for result in result:
        # Collect data for the Observations table
        obs_record = {
            "observation_id": curr_id,
            # date and time related fields
            'time_observed_at_date': result['time_observed_at'],
            'observed_on_date': result['observed_on_details']['date'],
            'observed_on_year': result['observed_on_details']['year'],
            'observed_on_month': result['observed_on_details']['month'],
            'observed_on_week': result['observed_on_details']['week'],
            'observed_on_day': result['observed_on_details']['day'],
            'observed_on_hour': result['observed_on_details']['hour'],

            # location fields
            'location': result['location'],
            'place_guess': result['place_guess'],

            # time zone related fields
            'observed_time_zone': result['observed_time_zone'],
            'created_time_zone': result['created_time_zone'],
            'time_zone_offset': result['time_zone_offset'],

            # names related fields
            'english_common_name': result['taxon']['english_common_name'],
            'preferred_common_name': result['taxon']['preferred_common_name'],
            'taxon_name': result['taxon']['name'],
            'description': result['description'],

            # identifications info
            'identifications_most_disagree': result['identifications_most_disagree'],
            'identifications_most_agree': result['identifications_most_agree'],

            # other
            'quality_grade': result['quality_grade'],
            'uri': result['uri'],  # just in case we need to check out additional info
        }
        observations_data.append(obs_record)

        # Collect data for the Photos table, if photos exist
        if 'photos' in result:
            for photo in result['photos']:
                photo_record = {
                    "observation_id": curr_id,
                    'image_url': photo['url'],
                    'original_image_url': replace_square_image_with_original(photo['url']),
                    'original_width': photo['original_dimensions']['width'],
                    'original_height': photo['original_dimensions']['height'],
                    'license_code': photo['license_code'],
                    'attribution': photo['attribution'],
                }
                photos_data.append(photo_record)
    return observations_data, photos_data
