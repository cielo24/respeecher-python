# respeecher.DefaultApi

All URIs are relative to *https://api.respeecher.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_calibration**](DefaultApi.md#create_calibration) | **POST** /api/calibration | Create a new Calibration
[**create_folder**](DefaultApi.md#create_folder) | **POST** /api/folders | Create a folder
[**create_note**](DefaultApi.md#create_note) | **POST** /api/notes | Create a note associated with a recording
[**create_order**](DefaultApi.md#create_order) | **POST** /api/v2/orders | Create a conversion order
[**create_original_recording**](DefaultApi.md#create_original_recording) | **POST** /api/recordings | Create an original recording
[**create_project**](DefaultApi.md#create_project) | **POST** /api/projects | Create a new project
[**create_tts_recording**](DefaultApi.md#create_tts_recording) | **POST** /api/v2/recordings/tts | Create an original text-to-speech recording
[**delete_api_key**](DefaultApi.md#delete_api_key) | **DELETE** /api/api-key | Delete the API key associated with your account
[**delete_calibration**](DefaultApi.md#delete_calibration) | **DELETE** /api/calibration/{calibration_id} | Delete a calibration
[**delete_folder**](DefaultApi.md#delete_folder) | **DELETE** /api/folders/{folder_id} | Delete a folder
[**delete_note**](DefaultApi.md#delete_note) | **DELETE** /api/notes | Delete a note
[**delete_project**](DefaultApi.md#delete_project) | **DELETE** /api/projects/{project_id} | Delete a project
[**delete_recording**](DefaultApi.md#delete_recording) | **DELETE** /api/recordings/{recording_id} | Delete a recording
[**download_file**](DefaultApi.md#download_file) | **GET** /storage/{file_to_download} | Download file
[**enable_calibration**](DefaultApi.md#enable_calibration) | **PUT** /api/calibration/{calibration_id}/enable | Set a calibration as the default enabled calibration
[**export_project**](DefaultApi.md#export_project) | **GET** /api/projects/{project_id}/export | Export a project
[**favorite_voice**](DefaultApi.md#favorite_voice) | **POST** /api/v2/voices/favorite/{voice_id} | Mark a voice as a favorite
[**generate_api_key**](DefaultApi.md#generate_api_key) | **POST** /api/api-key | Generate a new API key
[**get_accent_samples**](DefaultApi.md#get_accent_samples) | **GET** /api/v2/accents/samples | Get samples available for an accent
[**get_account_statistics**](DefaultApi.md#get_account_statistics) | **GET** /api/stats | Get the statistics for your account
[**get_calibration**](DefaultApi.md#get_calibration) | **GET** /api/calibration/{calibration_id} | Get a calibration by its ID
[**get_credits**](DefaultApi.md#get_credits) | **GET** /api/credits | Get the credits available to your account
[**get_folder_by_id**](DefaultApi.md#get_folder_by_id) | **GET** /api/folders/{folder_id} | Get a folder by its ID
[**get_folders_statistics**](DefaultApi.md#get_folders_statistics) | **POST** /api/stats/folders | Get statistics for a list of folders
[**get_project_by_url**](DefaultApi.md#get_project_by_url) | **GET** /api/projects/by-url | Get a project by its URL
[**get_projects_statistics**](DefaultApi.md#get_projects_statistics) | **GET** /api/stats/projects | Get statistics for a list of projects
[**get_recording_by_id**](DefaultApi.md#get_recording_by_id) | **GET** /api/recordings/{recording_id} | Get a recording by its ID
[**list_calibrations**](DefaultApi.md#list_calibrations) | **GET** /api/calibration | Get a list of calibrations associated with your account
[**list_conversions**](DefaultApi.md#list_conversions) | **GET** /api/recordings/conversions | Get a list of the conversions for an original recording
[**list_folders**](DefaultApi.md#list_folders) | **GET** /api/folders | Get a list of the folders in a project
[**list_original_recordings**](DefaultApi.md#list_original_recordings) | **GET** /api/recordings/originals | Get a list of the original recordings in a folder
[**list_projects**](DefaultApi.md#list_projects) | **GET** /api/projects | Get a list of your projects
[**list_recordings**](DefaultApi.md#list_recordings) | **GET** /api/recordings | Get a list of recordings for a specified folder or project
[**list_tts_voices**](DefaultApi.md#list_tts_voices) | **GET** /api/tts-voices | Get a list of the available TTS voices
[**list_voices**](DefaultApi.md#list_voices) | **GET** /api/v2/voices | Get a list of the voices available
[**login**](DefaultApi.md#login) | **POST** /api/login | Log in to an account and start a new session
[**logout**](DefaultApi.md#logout) | **POST** /api/logout | End your session
[**rename_folder**](DefaultApi.md#rename_folder) | **PATCH** /api/folders/{folder_id} | Rename a folder
[**retry_order_v2**](DefaultApi.md#retry_order_v2) | **POST** /api/v2/orders/retry/{recording_id} | Retry a conversion order for a specific original
[**search_voices**](DefaultApi.md#search_voices) | **GET** /api/v2/voices/search | Search for a voice by its name
[**set_voice_settings**](DefaultApi.md#set_voice_settings) | **POST** /api/v2/voices/settings | Set the settings for a voice
[**update_note**](DefaultApi.md#update_note) | **PUT** /api/notes | Update a note
[**update_project**](DefaultApi.md#update_project) | **PATCH** /api/projects/{project_id} | Change the name of a project
[**update_recording**](DefaultApi.md#update_recording) | **PATCH** /api/recordings/{recording_id} | Update a recording


# **create_calibration**
> CalibrationResponse create_calibration(name=name, data=data)

Create a new Calibration

Currently the supported audio formats are wav, ogg, mp3 or flac.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.calibration_response import CalibrationResponse
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
    except Exception as e:
        print("Exception when calling DefaultApi->create_calibration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Unique name for the calibration. | [optional] 
 **data** | **bytearray**| The audio binary data. | [optional] 

### Return type

[**CalibrationResponse**](CalibrationResponse.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Calibration created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder**
> Folder create_folder(folder_request)

Create a folder

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.folder import Folder
from respeecher.models.folder_request import FolderRequest
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
    folder_request = respeecher.FolderRequest() # FolderRequest | 

    try:
        # Create a folder
        api_response = api_instance.create_folder(folder_request)
        print("The response of DefaultApi->create_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_request** | [**FolderRequest**](FolderRequest.md)|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_note**
> NoteResponse create_note(note_request)

Create a note associated with a recording

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.note_request import NoteRequest
from respeecher.models.note_response import NoteResponse
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
    note_request = respeecher.NoteRequest() # NoteRequest | 

    try:
        # Create a note associated with a recording
        api_response = api_instance.create_note(note_request)
        print("The response of DefaultApi->create_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_request** | [**NoteRequest**](NoteRequest.md)|  | 

### Return type

[**NoteResponse**](NoteResponse.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Note created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> List[Order] create_order(order_request)

Create a conversion order

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.order import Order
from respeecher.models.order_request import OrderRequest
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
    order_request = respeecher.OrderRequest() # OrderRequest | 

    try:
        # Create a conversion order
        api_response = api_instance.create_order(order_request)
        print("The response of DefaultApi->create_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_request** | [**OrderRequest**](OrderRequest.md)|  | 

### Return type

[**List[Order]**](Order.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_original_recording**
> Recording create_original_recording(data=data, parent_folder_id=parent_folder_id, microphone=microphone, label=label)

Create an original recording

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.recording import Recording
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
    data = None # bytearray | The audio binary data (optional)
    parent_folder_id = 'parent_folder_id_example' # str |  (optional)
    microphone = 'microphone_example' # str | Name of the microphone used, set to 'file' if uploading a file (optional)
    label = 'label_example' # str |  (optional)

    try:
        # Create an original recording
        api_response = api_instance.create_original_recording(data=data, parent_folder_id=parent_folder_id, microphone=microphone, label=label)
        print("The response of DefaultApi->create_original_recording:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_original_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **bytearray**| The audio binary data | [optional] 
 **parent_folder_id** | **str**|  | [optional] 
 **microphone** | **str**| Name of the microphone used, set to &#39;file&#39; if uploading a file | [optional] 
 **label** | **str**|  | [optional] 

### Return type

[**Recording**](Recording.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Original recording created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> ProjectResponse create_project(project_request)

Create a new project

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.project_request import ProjectRequest
from respeecher.models.project_response import ProjectResponse
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
    project_request = respeecher.ProjectRequest() # ProjectRequest | 

    try:
        # Create a new project
        api_response = api_instance.create_project(project_request)
        print("The response of DefaultApi->create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_request** | [**ProjectRequest**](ProjectRequest.md)|  | 

### Return type

[**ProjectResponse**](ProjectResponse.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tts_recording**
> Recording create_tts_recording(tts_recording_request)

Create an original text-to-speech recording

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.recording import Recording
from respeecher.models.tts_recording_request import TTSRecordingRequest
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
    tts_recording_request = respeecher.TTSRecordingRequest() # TTSRecordingRequest | 

    try:
        # Create an original text-to-speech recording
        api_response = api_instance.create_tts_recording(tts_recording_request)
        print("The response of DefaultApi->create_tts_recording:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_tts_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tts_recording_request** | [**TTSRecordingRequest**](TTSRecordingRequest.md)|  | 

### Return type

[**Recording**](Recording.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TTS recording created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> delete_api_key()

Delete the API key associated with your account

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

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

    try:
        # Delete the API key associated with your account
        api_instance.delete_api_key()
    except Exception as e:
        print("Exception when calling DefaultApi->delete_api_key: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API key deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_calibration**
> CalibrationResponse delete_calibration(calibration_id)

Delete a calibration

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.calibration_response import CalibrationResponse
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
    calibration_id = 'calibration_id_example' # str | 

    try:
        # Delete a calibration
        api_response = api_instance.delete_calibration(calibration_id)
        print("The response of DefaultApi->delete_calibration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_calibration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calibration_id** | **str**|  | 

### Return type

[**CalibrationResponse**](CalibrationResponse.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deleted calibration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> List[DeleteProject200Response] delete_folder(folder_id)

Delete a folder

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.delete_project200_response import DeleteProject200Response
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
    folder_id = 'folder_id_example' # str | 

    try:
        # Delete a folder
        api_response = api_instance.delete_folder(folder_id)
        print("The response of DefaultApi->delete_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  | 

### Return type

[**List[DeleteProject200Response]**](DeleteProject200Response.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_note**
> NoteResponse delete_note(note_delete_request)

Delete a note

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.note_delete_request import NoteDeleteRequest
from respeecher.models.note_response import NoteResponse
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
    note_delete_request = respeecher.NoteDeleteRequest() # NoteDeleteRequest | 

    try:
        # Delete a note
        api_response = api_instance.delete_note(note_delete_request)
        print("The response of DefaultApi->delete_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_delete_request** | [**NoteDeleteRequest**](NoteDeleteRequest.md)|  | 

### Return type

[**NoteResponse**](NoteResponse.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Note deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> DeleteProject200Response delete_project(project_id)

Delete a project

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.delete_project200_response import DeleteProject200Response
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
    project_id = 'project_id_example' # str | 

    try:
        # Delete a project
        api_response = api_instance.delete_project(project_id)
        print("The response of DefaultApi->delete_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**DeleteProject200Response**](DeleteProject200Response.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recording**
> delete_recording(recording_id)

Delete a recording

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

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
    recording_id = 'recording_id_example' # str | The ID of the recording to delete

    try:
        # Delete a recording
        api_instance.delete_recording(recording_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_id** | **str**| The ID of the recording to delete | 

### Return type

void (empty response body)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Recording deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> bytearray download_file(file_to_download)

Download file

Downloads the specified file in binary format.

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

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
    file_to_download = 'file_to_download_example' # str | The name of the file to be downloaded, including its extension.

    try:
        # Download file
        api_response = api_instance.download_file(file_to_download)
        print("The response of DefaultApi->download_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->download_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_to_download** | **str**| The name of the file to be downloaded, including its extension. | 

### Return type

**bytearray**

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File downloaded successfully. |  -  |
**404** | File not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_calibration**
> List[CalibrationResponse] enable_calibration(calibration_id)

Set a calibration as the default enabled calibration

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.calibration_response import CalibrationResponse
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
    calibration_id = 'calibration_id_example' # str | 

    try:
        # Set a calibration as the default enabled calibration
        api_response = api_instance.enable_calibration(calibration_id)
        print("The response of DefaultApi->enable_calibration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->enable_calibration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calibration_id** | **str**|  | 

### Return type

[**List[CalibrationResponse]**](CalibrationResponse.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Calibration enabled successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_project**
> bytearray export_project(project_id, starred_only=starred_only)

Export a project

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

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
    project_id = 'project_id_example' # str | 
    starred_only = True # bool |  (optional)

    try:
        # Export a project
        api_response = api_instance.export_project(project_id, starred_only=starred_only)
        print("The response of DefaultApi->export_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->export_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **starred_only** | **bool**|  | [optional] 

### Return type

**bytearray**

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project exported successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **favorite_voice**
> Voice favorite_voice(voice_id, favorite_voice_request)

Mark a voice as a favorite

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.favorite_voice_request import FavoriteVoiceRequest
from respeecher.models.voice import Voice
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
    voice_id = 'voice_id_example' # str | 
    favorite_voice_request = respeecher.FavoriteVoiceRequest() # FavoriteVoiceRequest | 

    try:
        # Mark a voice as a favorite
        api_response = api_instance.favorite_voice(voice_id, favorite_voice_request)
        print("The response of DefaultApi->favorite_voice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->favorite_voice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voice_id** | **str**|  | 
 **favorite_voice_request** | [**FavoriteVoiceRequest**](FavoriteVoiceRequest.md)|  | 

### Return type

[**Voice**](Voice.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Voice updated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_api_key**
> GenerateApiKey200Response generate_api_key(generate_api_key_request)

Generate a new API key

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.generate_api_key200_response import GenerateApiKey200Response
from respeecher.models.generate_api_key_request import GenerateApiKeyRequest
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
    generate_api_key_request = respeecher.GenerateApiKeyRequest() # GenerateApiKeyRequest | 

    try:
        # Generate a new API key
        api_response = api_instance.generate_api_key(generate_api_key_request)
        print("The response of DefaultApi->generate_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->generate_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_api_key_request** | [**GenerateApiKeyRequest**](GenerateApiKeyRequest.md)|  | 

### Return type

[**GenerateApiKey200Response**](GenerateApiKey200Response.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API key generated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accent_samples**
> AccentSamplesResponse get_accent_samples(accent_id)

Get samples available for an accent

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.accent_samples_response import AccentSamplesResponse
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
    accent_id = 'accent_id_example' # str | 

    try:
        # Get samples available for an accent
        api_response = api_instance.get_accent_samples(accent_id)
        print("The response of DefaultApi->get_accent_samples:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_accent_samples: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accent_id** | **str**|  | 

### Return type

[**AccentSamplesResponse**](AccentSamplesResponse.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accent samples |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_statistics**
> AccountStatistics get_account_statistics()

Get the statistics for your account

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.account_statistics import AccountStatistics
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

    try:
        # Get the statistics for your account
        api_response = api_instance.get_account_statistics()
        print("The response of DefaultApi->get_account_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_account_statistics: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountStatistics**](AccountStatistics.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account statistics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calibration**
> CalibrationResponse get_calibration(calibration_id)

Get a calibration by its ID

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.calibration_response import CalibrationResponse
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
    calibration_id = 'calibration_id_example' # str | 

    try:
        # Get a calibration by its ID
        api_response = api_instance.get_calibration(calibration_id)
        print("The response of DefaultApi->get_calibration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_calibration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calibration_id** | **str**|  | 

### Return type

[**CalibrationResponse**](CalibrationResponse.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Calibration details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credits**
> GetCredits200Response get_credits()

Get the credits available to your account

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.get_credits200_response import GetCredits200Response
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

    try:
        # Get the credits available to your account
        api_response = api_instance.get_credits()
        print("The response of DefaultApi->get_credits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_credits: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetCredits200Response**](GetCredits200Response.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Credits information retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_by_id**
> Folder get_folder_by_id(folder_id)

Get a folder by its ID

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.folder import Folder
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
    folder_id = 'folder_id_example' # str | 

    try:
        # Get a folder by its ID
        api_response = api_instance.get_folder_by_id(folder_id)
        print("The response of DefaultApi->get_folder_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_folder_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folders_statistics**
> List[FolderStatistics] get_folders_statistics(folders_statistics_request)

Get statistics for a list of folders

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.folder_statistics import FolderStatistics
from respeecher.models.folders_statistics_request import FoldersStatisticsRequest
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
    folders_statistics_request = respeecher.FoldersStatisticsRequest() # FoldersStatisticsRequest | 

    try:
        # Get statistics for a list of folders
        api_response = api_instance.get_folders_statistics(folders_statistics_request)
        print("The response of DefaultApi->get_folders_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_folders_statistics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folders_statistics_request** | [**FoldersStatisticsRequest**](FoldersStatisticsRequest.md)|  | 

### Return type

[**List[FolderStatistics]**](FolderStatistics.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folders statistics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_by_url**
> ProjectResponse get_project_by_url(project_url)

Get a project by its URL

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.project_response import ProjectResponse
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
    project_url = 'project_url_example' # str | 

    try:
        # Get a project by its URL
        api_response = api_instance.get_project_by_url(project_url)
        print("The response of DefaultApi->get_project_by_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_project_by_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_url** | **str**|  | 

### Return type

[**ProjectResponse**](ProjectResponse.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects_statistics**
> List[List[ProjectStatistics]] get_projects_statistics(project_ids=project_ids)

Get statistics for a list of projects

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.project_statistics import ProjectStatistics
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
    project_ids = 'project_ids_example' # str | Comma-separated list of project IDs to fetch statistics for. (optional)

    try:
        # Get statistics for a list of projects
        api_response = api_instance.get_projects_statistics(project_ids=project_ids)
        print("The response of DefaultApi->get_projects_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_projects_statistics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_ids** | **str**| Comma-separated list of project IDs to fetch statistics for. | [optional] 

### Return type

**List[List[ProjectStatistics]]**

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statistics for the specified projects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_by_id**
> Recording get_recording_by_id(recording_id)

Get a recording by its ID

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.recording import Recording
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
    recording_id = 'recording_id_example' # str | The ID of the recording to fetch

    try:
        # Get a recording by its ID
        api_response = api_instance.get_recording_by_id(recording_id)
        print("The response of DefaultApi->get_recording_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_recording_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_id** | **str**| The ID of the recording to fetch | 

### Return type

[**Recording**](Recording.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recording fetched successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_calibrations**
> List[CalibrationResponse] list_calibrations()

Get a list of calibrations associated with your account

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.calibration_response import CalibrationResponse
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

    try:
        # Get a list of calibrations associated with your account
        api_response = api_instance.list_calibrations()
        print("The response of DefaultApi->list_calibrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_calibrations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CalibrationResponse]**](CalibrationResponse.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of calibrations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_conversions**
> RecordingListResponse list_conversions(original_id=original_id, limit=limit, offset=offset, direction=direction)

Get a list of the conversions for an original recording

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.recording_list_response import RecordingListResponse
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
    original_id = 'original_id_example' # str |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    direction = 'direction_example' # str |  (optional)

    try:
        # Get a list of the conversions for an original recording
        api_response = api_instance.list_conversions(original_id=original_id, limit=limit, offset=offset, direction=direction)
        print("The response of DefaultApi->list_conversions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_conversions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **original_id** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **direction** | **str**|  | [optional] 

### Return type

[**RecordingListResponse**](RecordingListResponse.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of recordings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_folders**
> FolderListResponse list_folders(project_id, limit=limit, offset=offset, direction=direction)

Get a list of the folders in a project

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.folder_list_response import FolderListResponse
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
    project_id = 'project_id_example' # str | 
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    direction = 'direction_example' # str |  (optional)

    try:
        # Get a list of the folders in a project
        api_response = api_instance.list_folders(project_id, limit=limit, offset=offset, direction=direction)
        print("The response of DefaultApi->list_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_folders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **direction** | **str**|  | [optional] 

### Return type

[**FolderListResponse**](FolderListResponse.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folders list retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_original_recordings**
> RecordingListResponse list_original_recordings()

Get a list of the original recordings in a folder

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.recording_list_response import RecordingListResponse
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

    try:
        # Get a list of the original recordings in a folder
        api_response = api_instance.list_original_recordings()
        print("The response of DefaultApi->list_original_recordings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_original_recordings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RecordingListResponse**](RecordingListResponse.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of original recordings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> ProjectListResponse list_projects(limit=limit, offset=offset, sort=sort, direction=direction, owner=owner)

Get a list of your projects

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.project_list_response import ProjectListResponse
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
    limit = 56 # int | The maximum number of projects to list. (optional)
    offset = 56 # int | The number of projects to offset the list by. (optional)
    sort = 'sort_example' # str | Sort by name, created_at or last_recording_at. (optional)
    direction = 'direction_example' # str | Order projects by asc or desc. (optional)
    owner = 'owner_example' # str | List projects for a specific owner ID. (optional)

    try:
        # Get a list of your projects
        api_response = api_instance.list_projects(limit=limit, offset=offset, sort=sort, direction=direction, owner=owner)
        print("The response of DefaultApi->list_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of projects to list. | [optional] 
 **offset** | **int**| The number of projects to offset the list by. | [optional] 
 **sort** | **str**| Sort by name, created_at or last_recording_at. | [optional] 
 **direction** | **str**| Order projects by asc or desc. | [optional] 
 **owner** | **str**| List projects for a specific owner ID. | [optional] 

### Return type

[**ProjectListResponse**](ProjectListResponse.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Projects list retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_recordings**
> RecordingListResponse list_recordings(project_id=project_id, folder_id=folder_id, limit=limit, offset=offset, direction=direction)

Get a list of recordings for a specified folder or project

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.recording_list_response import RecordingListResponse
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
    project_id = 'project_id_example' # str |  (optional)
    folder_id = 'folder_id_example' # str |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    direction = 'direction_example' # str |  (optional)

    try:
        # Get a list of recordings for a specified folder or project
        api_response = api_instance.list_recordings(project_id=project_id, folder_id=folder_id, limit=limit, offset=offset, direction=direction)
        print("The response of DefaultApi->list_recordings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_recordings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | [optional] 
 **folder_id** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **direction** | **str**|  | [optional] 

### Return type

[**RecordingListResponse**](RecordingListResponse.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of recordings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tts_voices**
> List[TTSVoice] list_tts_voices()

Get a list of the available TTS voices

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.tts_voice import TTSVoice
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

    try:
        # Get a list of the available TTS voices
        api_response = api_instance.list_tts_voices()
        print("The response of DefaultApi->list_tts_voices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_tts_voices: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TTSVoice]**](TTSVoice.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TTS voices retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_voices**
> VoicesListResponse list_voices(limit=limit, offset=offset, sort=sort, direction=direction, visibility=visibility, species=species, gender=gender, age_group=age_group, pitch_group=pitch_group, nationality=nationality)

Get a list of the voices available

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.voices_list_response import VoicesListResponse
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
    limit = 25 # int | Limits the number of voices returned in the response. Defaults to 25. (optional) (default to 25)
    offset = 0 # int | Offsets the list of voices to paginate through results. Defaults to 0. (optional) (default to 0)
    sort = 'sort_example' # str | Sorts the voices by a specified attribute (e.g., name, pitch, rating, or created_at). (optional)
    direction = 'direction_example' # str | Specifies the direction of sorting. Can be 'asc' for ascending or 'desc' for descending. (optional)
    visibility = 'visibility_example' # str | Filters voices by their visibility status (e.g., public, paid, private, or kids). (optional)
    species = 'species_example' # str | Filters voices by species category (e.g., human, animal, or other). (optional)
    gender = 'gender_example' # str | Filters voices by gender (e.g., male or female). (optional)
    age_group = 'age_group_example' # str | Filters voices by age group (e.g., child, young, adult, or senior). (optional)
    pitch_group = 'pitch_group_example' # str | Filters voices by pitch group (e.g., low, mid, or high). (optional)
    nationality = 'nationality_example' # str | Filters voices by nationality. (optional)

    try:
        # Get a list of the voices available
        api_response = api_instance.list_voices(limit=limit, offset=offset, sort=sort, direction=direction, visibility=visibility, species=species, gender=gender, age_group=age_group, pitch_group=pitch_group, nationality=nationality)
        print("The response of DefaultApi->list_voices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_voices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the number of voices returned in the response. Defaults to 25. | [optional] [default to 25]
 **offset** | **int**| Offsets the list of voices to paginate through results. Defaults to 0. | [optional] [default to 0]
 **sort** | **str**| Sorts the voices by a specified attribute (e.g., name, pitch, rating, or created_at). | [optional] 
 **direction** | **str**| Specifies the direction of sorting. Can be &#39;asc&#39; for ascending or &#39;desc&#39; for descending. | [optional] 
 **visibility** | **str**| Filters voices by their visibility status (e.g., public, paid, private, or kids). | [optional] 
 **species** | **str**| Filters voices by species category (e.g., human, animal, or other). | [optional] 
 **gender** | **str**| Filters voices by gender (e.g., male or female). | [optional] 
 **age_group** | **str**| Filters voices by age group (e.g., child, young, adult, or senior). | [optional] 
 **pitch_group** | **str**| Filters voices by pitch group (e.g., low, mid, or high). | [optional] 
 **nationality** | **str**| Filters voices by nationality. | [optional] 

### Return type

[**VoicesListResponse**](VoicesListResponse.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of available voices |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> Login200Response login(login_request)

Log in to an account and start a new session

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.login200_response import Login200Response
from respeecher.models.login_request import LoginRequest
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
    login_request = respeecher.LoginRequest() # LoginRequest | 

    try:
        # Log in to an account and start a new session
        api_response = api_instance.login(login_request)
        print("The response of DefaultApi->login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)|  | 

### Return type

[**Login200Response**](Login200Response.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Login successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> Logout200Response logout()

End your session

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.logout200_response import Logout200Response
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

    try:
        # End your session
        api_response = api_instance.logout()
        print("The response of DefaultApi->logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->logout: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Logout200Response**](Logout200Response.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Logout successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_folder**
> Folder rename_folder(folder_id, update_project_request)

Rename a folder

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.folder import Folder
from respeecher.models.update_project_request import UpdateProjectRequest
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
    folder_id = 'folder_id_example' # str | 
    update_project_request = respeecher.UpdateProjectRequest() # UpdateProjectRequest | 

    try:
        # Rename a folder
        api_response = api_instance.rename_folder(folder_id, update_project_request)
        print("The response of DefaultApi->rename_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rename_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  | 
 **update_project_request** | [**UpdateProjectRequest**](UpdateProjectRequest.md)|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder renamed successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_order_v2**
> retry_order_v2(recording_id)

Retry a conversion order for a specific original

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

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
    recording_id = 'recording_id_example' # str | 

    try:
        # Retry a conversion order for a specific original
        api_instance.retry_order_v2(recording_id)
    except Exception as e:
        print("Exception when calling DefaultApi->retry_order_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order retried successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_voices**
> List[Voice] search_voices(name, limit=limit)

Search for a voice by its name

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.voice import Voice
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
    name = 'name_example' # str | 
    limit = 56 # int |  (optional)

    try:
        # Search for a voice by its name
        api_response = api_instance.search_voices(name, limit=limit)
        print("The response of DefaultApi->search_voices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->search_voices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **limit** | **int**|  | [optional] 

### Return type

[**List[Voice]**](Voice.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_voice_settings**
> Voice set_voice_settings(voice_settings_request)

Set the settings for a voice

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.voice import Voice
from respeecher.models.voice_settings_request import VoiceSettingsRequest
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
    voice_settings_request = respeecher.VoiceSettingsRequest() # VoiceSettingsRequest | 

    try:
        # Set the settings for a voice
        api_response = api_instance.set_voice_settings(voice_settings_request)
        print("The response of DefaultApi->set_voice_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->set_voice_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voice_settings_request** | [**VoiceSettingsRequest**](VoiceSettingsRequest.md)|  | 

### Return type

[**Voice**](Voice.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Voice settings updated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_note**
> NoteResponse update_note(note_request)

Update a note

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.note_request import NoteRequest
from respeecher.models.note_response import NoteResponse
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
    note_request = respeecher.NoteRequest() # NoteRequest | 

    try:
        # Update a note
        api_response = api_instance.update_note(note_request)
        print("The response of DefaultApi->update_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_request** | [**NoteRequest**](NoteRequest.md)|  | 

### Return type

[**NoteResponse**](NoteResponse.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Note updated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> ProjectResponse update_project(project_id, update_project_request)

Change the name of a project

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.project_response import ProjectResponse
from respeecher.models.update_project_request import UpdateProjectRequest
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
    project_id = 'project_id_example' # str | 
    update_project_request = respeecher.UpdateProjectRequest() # UpdateProjectRequest | 

    try:
        # Change the name of a project
        api_response = api_instance.update_project(project_id, update_project_request)
        print("The response of DefaultApi->update_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **update_project_request** | [**UpdateProjectRequest**](UpdateProjectRequest.md)|  | 

### Return type

[**ProjectResponse**](ProjectResponse.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project updated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recording**
> Recording update_recording(recording_id, update_recording_request)

Update a recording

### Example

* Api Key Authentication (CookieAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import respeecher
from respeecher.models.recording import Recording
from respeecher.models.update_recording_request import UpdateRecordingRequest
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
    recording_id = 'recording_id_example' # str | The ID of the recording to update
    update_recording_request = respeecher.UpdateRecordingRequest() # UpdateRecordingRequest | 

    try:
        # Update a recording
        api_response = api_instance.update_recording(recording_id, update_recording_request)
        print("The response of DefaultApi->update_recording:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_id** | **str**| The ID of the recording to update | 
 **update_recording_request** | [**UpdateRecordingRequest**](UpdateRecordingRequest.md)|  | 

### Return type

[**Recording**](Recording.md)

### Authorization

[CookieAuth](../README.md#CookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recording updated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

