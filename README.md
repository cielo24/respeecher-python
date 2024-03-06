# respeecher
API for interacting with Respeecher services, including key and session management, and calibration functionalities.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import respeecher
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import respeecher
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.respeecher.com
# See configuration.py for a list of all supported configuration parameters.
configuration = respeecher.Configuration(
    host = "https://api.respeecher.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CookieAuth
configuration.api_key['CookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CookieAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'


# Enter a context with an instance of the API client
with respeecher.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = respeecher.DefaultApi(api_client)
    name = 'name_example' # str | Unique name for the calibration. (optional)
    data = None # bytearray | The audio binary data. (optional)

    try:
        # Create a new Calibration
        api_response = api_instance.create_calibration(name=name, data=data)
        print("The response of DefaultApi->create_calibration:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->create_calibration: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.respeecher.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**create_calibration**](docs/DefaultApi.md#create_calibration) | **POST** /api/calibration | Create a new Calibration
*DefaultApi* | [**create_folder**](docs/DefaultApi.md#create_folder) | **POST** /api/folders | Create a folder
*DefaultApi* | [**create_note**](docs/DefaultApi.md#create_note) | **POST** /api/notes | Create a note associated with a recording
*DefaultApi* | [**create_order**](docs/DefaultApi.md#create_order) | **POST** /api/v2/orders | Create a conversion order
*DefaultApi* | [**create_original_recording**](docs/DefaultApi.md#create_original_recording) | **POST** /api/recordings | Create an original recording
*DefaultApi* | [**create_project**](docs/DefaultApi.md#create_project) | **POST** /api/projects | Create a new project
*DefaultApi* | [**create_tts_recording**](docs/DefaultApi.md#create_tts_recording) | **POST** /api/v2/recordings/tts | Create an original text-to-speech recording
*DefaultApi* | [**delete_api_key**](docs/DefaultApi.md#delete_api_key) | **DELETE** /api/api-key | Delete the API key associated with your account
*DefaultApi* | [**delete_calibration**](docs/DefaultApi.md#delete_calibration) | **DELETE** /api/calibration/{calibration_id} | Delete a calibration
*DefaultApi* | [**delete_folder**](docs/DefaultApi.md#delete_folder) | **DELETE** /api/folders/{folder_id} | Delete a folder
*DefaultApi* | [**delete_note**](docs/DefaultApi.md#delete_note) | **DELETE** /api/notes | Delete a note
*DefaultApi* | [**delete_project**](docs/DefaultApi.md#delete_project) | **DELETE** /api/projects/{project_id} | Delete a project
*DefaultApi* | [**delete_recording**](docs/DefaultApi.md#delete_recording) | **DELETE** /api/recordings/{recording_id} | Delete a recording
*DefaultApi* | [**download_file**](docs/DefaultApi.md#download_file) | **GET** /storage/{file_to_download} | Download file
*DefaultApi* | [**enable_calibration**](docs/DefaultApi.md#enable_calibration) | **PUT** /api/calibration/{calibration_id}/enable | Set a calibration as the default enabled calibration
*DefaultApi* | [**export_project**](docs/DefaultApi.md#export_project) | **GET** /api/projects/{project_id}/export | Export a project
*DefaultApi* | [**favorite_voice**](docs/DefaultApi.md#favorite_voice) | **POST** /api/v2/voices/favorite/{voice_id} | Mark a voice as a favorite
*DefaultApi* | [**generate_api_key**](docs/DefaultApi.md#generate_api_key) | **POST** /api/api-key | Generate a new API key
*DefaultApi* | [**get_accent_samples**](docs/DefaultApi.md#get_accent_samples) | **GET** /api/v2/accents/samples | Get samples available for an accent
*DefaultApi* | [**get_account_statistics**](docs/DefaultApi.md#get_account_statistics) | **GET** /api/stats | Get the statistics for your account
*DefaultApi* | [**get_calibration**](docs/DefaultApi.md#get_calibration) | **GET** /api/calibration/{calibration_id} | Get a calibration by its ID
*DefaultApi* | [**get_credits**](docs/DefaultApi.md#get_credits) | **GET** /api/credits | Get the credits available to your account
*DefaultApi* | [**get_folder_by_id**](docs/DefaultApi.md#get_folder_by_id) | **GET** /api/folders/{folder_id} | Get a folder by its ID
*DefaultApi* | [**get_folders_statistics**](docs/DefaultApi.md#get_folders_statistics) | **POST** /api/stats/folders | Get statistics for a list of folders
*DefaultApi* | [**get_project_by_url**](docs/DefaultApi.md#get_project_by_url) | **GET** /api/projects/by-url | Get a project by its URL
*DefaultApi* | [**get_projects_statistics**](docs/DefaultApi.md#get_projects_statistics) | **GET** /api/stats/projects | Get statistics for a list of projects
*DefaultApi* | [**get_recording_by_id**](docs/DefaultApi.md#get_recording_by_id) | **GET** /api/recordings/{recording_id} | Get a recording by its ID
*DefaultApi* | [**list_calibrations**](docs/DefaultApi.md#list_calibrations) | **GET** /api/calibration | Get a list of calibrations associated with your account
*DefaultApi* | [**list_conversions**](docs/DefaultApi.md#list_conversions) | **GET** /api/recordings/conversions | Get a list of the conversions for an original recording
*DefaultApi* | [**list_folders**](docs/DefaultApi.md#list_folders) | **GET** /api/folders | Get a list of the folders in a project
*DefaultApi* | [**list_original_recordings**](docs/DefaultApi.md#list_original_recordings) | **GET** /api/recordings/originals | Get a list of the original recordings in a folder
*DefaultApi* | [**list_projects**](docs/DefaultApi.md#list_projects) | **GET** /api/projects | Get a list of your projects
*DefaultApi* | [**list_recordings**](docs/DefaultApi.md#list_recordings) | **GET** /api/recordings | Get a list of recordings for a specified folder or project
*DefaultApi* | [**list_tts_voices**](docs/DefaultApi.md#list_tts_voices) | **GET** /api/tts-voices | Get a list of the available TTS voices
*DefaultApi* | [**list_voices**](docs/DefaultApi.md#list_voices) | **GET** /api/v2/voices | Get a list of the voices available
*DefaultApi* | [**login**](docs/DefaultApi.md#login) | **POST** /api/login | Log in to an account and start a new session
*DefaultApi* | [**logout**](docs/DefaultApi.md#logout) | **POST** /api/logout | End your session
*DefaultApi* | [**rename_folder**](docs/DefaultApi.md#rename_folder) | **PATCH** /api/folders/{folder_id} | Rename a folder
*DefaultApi* | [**retry_order_v2**](docs/DefaultApi.md#retry_order_v2) | **POST** /api/v2/orders/retry/{recording_id} | Retry a conversion order for a specific original
*DefaultApi* | [**search_voices**](docs/DefaultApi.md#search_voices) | **GET** /api/v2/voices/search | Search for a voice by its name
*DefaultApi* | [**set_voice_settings**](docs/DefaultApi.md#set_voice_settings) | **POST** /api/v2/voices/settings | Set the settings for a voice
*DefaultApi* | [**update_note**](docs/DefaultApi.md#update_note) | **PUT** /api/notes | Update a note
*DefaultApi* | [**update_project**](docs/DefaultApi.md#update_project) | **PATCH** /api/projects/{project_id} | Change the name of a project
*DefaultApi* | [**update_recording**](docs/DefaultApi.md#update_recording) | **PATCH** /api/recordings/{recording_id} | Update a recording


## Documentation For Models

 - [Accent](docs/Accent.md)
 - [AccentInfo](docs/AccentInfo.md)
 - [AccentSamplesResponse](docs/AccentSamplesResponse.md)
 - [AccountStatistics](docs/AccountStatistics.md)
 - [AccountStatisticsConversions](docs/AccountStatisticsConversions.md)
 - [AccountStatisticsModelsInner](docs/AccountStatisticsModelsInner.md)
 - [AccountStatisticsTimeConverted](docs/AccountStatisticsTimeConverted.md)
 - [AccountStatisticsTimeConvertedPreviousMonthesInner](docs/AccountStatisticsTimeConvertedPreviousMonthesInner.md)
 - [CalibrationResponse](docs/CalibrationResponse.md)
 - [ConversionDetail](docs/ConversionDetail.md)
 - [DeleteProject200Response](docs/DeleteProject200Response.md)
 - [FavoriteVoiceRequest](docs/FavoriteVoiceRequest.md)
 - [Folder](docs/Folder.md)
 - [FolderListResponse](docs/FolderListResponse.md)
 - [FolderRequest](docs/FolderRequest.md)
 - [FolderStatistics](docs/FolderStatistics.md)
 - [FolderStatisticsStats](docs/FolderStatisticsStats.md)
 - [FoldersStatisticsRequest](docs/FoldersStatisticsRequest.md)
 - [GenerateApiKey200Response](docs/GenerateApiKey200Response.md)
 - [GenerateApiKeyRequest](docs/GenerateApiKeyRequest.md)
 - [GetCredits200Response](docs/GetCredits200Response.md)
 - [Login200Response](docs/Login200Response.md)
 - [LoginRequest](docs/LoginRequest.md)
 - [Logout200Response](docs/Logout200Response.md)
 - [NoteDeleteRequest](docs/NoteDeleteRequest.md)
 - [NoteRequest](docs/NoteRequest.md)
 - [NoteResponse](docs/NoteResponse.md)
 - [Order](docs/Order.md)
 - [OrderRequest](docs/OrderRequest.md)
 - [Pagination](docs/Pagination.md)
 - [ProjectListResponse](docs/ProjectListResponse.md)
 - [ProjectListResponsePagination](docs/ProjectListResponsePagination.md)
 - [ProjectRequest](docs/ProjectRequest.md)
 - [ProjectResponse](docs/ProjectResponse.md)
 - [ProjectStatistics](docs/ProjectStatistics.md)
 - [ProjectStatisticsConversions](docs/ProjectStatisticsConversions.md)
 - [ProjectStatisticsTimeConverted](docs/ProjectStatisticsTimeConverted.md)
 - [ProjectsStatisticsRequest](docs/ProjectsStatisticsRequest.md)
 - [Recording](docs/Recording.md)
 - [RecordingListResponse](docs/RecordingListResponse.md)
 - [RecordingModeration](docs/RecordingModeration.md)
 - [TTSRecordingRequest](docs/TTSRecordingRequest.md)
 - [TTSVoice](docs/TTSVoice.md)
 - [Tier](docs/Tier.md)
 - [UpdateProjectRequest](docs/UpdateProjectRequest.md)
 - [UpdateRecordingRequest](docs/UpdateRecordingRequest.md)
 - [Voice](docs/Voice.md)
 - [VoiceSettingsRequest](docs/VoiceSettingsRequest.md)
 - [VoicesListResponse](docs/VoicesListResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: api-key
- **Location**: HTTP header

<a id="CookieAuth"></a>
### CookieAuth

- **Type**: API key
- **API key parameter name**: X-Csrf-Token
- **Location**: HTTP header


## Author




