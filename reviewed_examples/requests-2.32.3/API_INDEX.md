# API index

[Quick start](QUICKSTART.md) · [Package overview](README.md)

Search this page in your editor or run `python search_api.py "keyword"`. Public names are candidates, not a guarantee of API stability. Private definitions and raw imports remain in [full inspection](REFERENCE.md).

The index lists module-level functions and classes. Open a class page for its member table, or use search to find methods directly.

## requests

| API | Kind | Purpose from docstring |
| --- | --- | --- |
| [ConnectTimeout](api/00000-requests.ConnectTimeout.md) | class | The request timed out while trying to connect to the remote server. |
| [ConnectionError](api/00003-requests.ConnectionError.md) | class | A Connection error occurred. |
| [FileModeWarning](api/00006-requests.FileModeWarning.md) | class | A file was opened in text mode, but Requests determined its binary length. |
| [HTTPError](api/00009-requests.HTTPError.md) | class | An HTTP error occurred. |
| [JSONDecodeError](api/00012-requests.JSONDecodeError.md) | class | Couldn't decode the text into json |
| [PreparedRequest](api/00015-requests.PreparedRequest.md) | class | The fully mutable :class:`PreparedRequest <PreparedRequest>` object, |
| [ReadTimeout](api/00029-requests.ReadTimeout.md) | class | The server did not send any data in the allotted amount of time. |
| [Request](api/00032-requests.Request.md) | class | A user-created :class:`Request <Request>` object. |
| [RequestException](api/00036-requests.RequestException.md) | class | There was an ambiguous exception that occurred while handling your |
| [RequestsDependencyWarning](api/00039-requests.RequestsDependencyWarning.md) | class | An imported dependency doesn't match the expected version range. |
| [Response](api/00042-requests.Response.md) | class | The :class:`Response <Response>` object, which contains a |
| [Session](api/00056-requests.Session.md) | class | A Requests session. |
| [Timeout](api/00077-requests.Timeout.md) | class | The request timed out. |
| [TooManyRedirects](api/00080-requests.TooManyRedirects.md) | class | Too many redirects. |
| [URLRequired](api/00083-requests.URLRequired.md) | class | A valid URL is required to make a request. |
| [check_compatibility](api/00086-requests.check_compatibility.md) | function | No description supplied by the package. |
| [delete](api/00087-requests.delete.md) | function | Sends a DELETE request. |
| [get](api/00088-requests.get.md) | function | Sends a GET request. |
| [head](api/00089-requests.head.md) | function | Sends a HEAD request. |
| [options](api/00090-requests.options.md) | function | Sends an OPTIONS request. |
| [patch](api/00091-requests.patch.md) | function | Sends a PATCH request. |
| [post](api/00092-requests.post.md) | function | Sends a POST request. |
| [put](api/00093-requests.put.md) | function | Sends a PUT request. |
| [request](api/00094-requests.request.md) | function | Constructs and sends a :class:`Request <Request>`. |
| [session](api/00095-requests.session.md) | function | Returns a :class:`Session` for context-management. |

## requests.adapters

| API | Kind | Purpose from docstring |
| --- | --- | --- |
| [BaseAdapter](api/00096-requests.adapters.BaseAdapter.md) | class | The Base Transport Adapter |
| [CaseInsensitiveDict](api/00099-requests.adapters.CaseInsensitiveDict.md) | class | A case-insensitive ``dict``-like object. |
| [ConnectTimeout](api/00111-requests.adapters.ConnectTimeout.md) | class | The request timed out while trying to connect to the remote server. |
| [ConnectionError](api/00114-requests.adapters.ConnectionError.md) | class | A Connection error occurred. |
| [HTTPAdapter](api/00117-requests.adapters.HTTPAdapter.md) | class | The built-in HTTP Adapter for urllib3. |
| [InvalidHeader](api/00130-requests.adapters.InvalidHeader.md) | class | The header value provided was somehow invalid. |
| [InvalidProxyURL](api/00133-requests.adapters.InvalidProxyURL.md) | class | The proxy URL provided is invalid. |
| [InvalidSchema](api/00136-requests.adapters.InvalidSchema.md) | class | The URL scheme provided is either invalid or unsupported. |
| [InvalidURL](api/00139-requests.adapters.InvalidURL.md) | class | The URL provided was somehow invalid. |
| [PreparedRequest](api/00142-requests.adapters.PreparedRequest.md) | class | The fully mutable :class:`PreparedRequest <PreparedRequest>` object, |
| [ProxyError](api/00153-requests.adapters.ProxyError.md) | class | A proxy error occurred. |
| [ReadTimeout](api/00156-requests.adapters.ReadTimeout.md) | class | The server did not send any data in the allotted amount of time. |
| [Response](api/00159-requests.adapters.Response.md) | class | The :class:`Response <Response>` object, which contains a |
| [RetryError](api/00173-requests.adapters.RetryError.md) | class | Custom retries logic failed |
| [SOCKSProxyManager](api/00176-requests.adapters.SOCKSProxyManager.md) | function | No description supplied by the package. |
| [SSLError](api/00177-requests.adapters.SSLError.md) | class | An SSL error occurred. |
| [extract_cookies_to_jar](api/00180-requests.adapters.extract_cookies_to_jar.md) | function | Extract the cookies from the response into a CookieJar. |
| [extract_zipped_paths](api/00181-requests.adapters.extract_zipped_paths.md) | function | Replace nonexistent paths that look like they refer to a member of a zip |
| [get_auth_from_url](api/00182-requests.adapters.get_auth_from_url.md) | function | Given a url with authentication components, extract them into a tuple of |
| [get_encoding_from_headers](api/00183-requests.adapters.get_encoding_from_headers.md) | function | Returns encodings from given HTTP Header Dict. |
| [prepend_scheme_if_needed](api/00184-requests.adapters.prepend_scheme_if_needed.md) | function | Given a URL that may or may not have a scheme, prepend the given scheme. |
| [select_proxy](api/00185-requests.adapters.select_proxy.md) | function | Select a proxy for the url, if applicable. |
| [urldefragauth](api/00186-requests.adapters.urldefragauth.md) | function | Given a url remove the fragment and the authentication part. |

## requests.api

| API | Kind | Purpose from docstring |
| --- | --- | --- |
| [delete](api/00187-requests.api.delete.md) | function | Sends a DELETE request. |
| [get](api/00188-requests.api.get.md) | function | Sends a GET request. |
| [head](api/00189-requests.api.head.md) | function | Sends a HEAD request. |
| [options](api/00190-requests.api.options.md) | function | Sends an OPTIONS request. |
| [patch](api/00191-requests.api.patch.md) | function | Sends a PATCH request. |
| [post](api/00192-requests.api.post.md) | function | Sends a POST request. |
| [put](api/00193-requests.api.put.md) | function | Sends a PUT request. |
| [request](api/00194-requests.api.request.md) | function | Constructs and sends a :class:`Request <Request>`. |

## requests.auth

| API | Kind | Purpose from docstring |
| --- | --- | --- |
| [AuthBase](api/00195-requests.auth.AuthBase.md) | class | Base class that all auth implementations derive from |
| [HTTPBasicAuth](api/00196-requests.auth.HTTPBasicAuth.md) | class | Attaches HTTP Basic Authentication to the given Request object. |
| [HTTPDigestAuth](api/00197-requests.auth.HTTPDigestAuth.md) | class | Attaches HTTP Digest Authentication to the given Request object. |
| [HTTPProxyAuth](api/00202-requests.auth.HTTPProxyAuth.md) | class | Attaches HTTP Proxy Authentication to a given Request object. |
| [extract_cookies_to_jar](api/00203-requests.auth.extract_cookies_to_jar.md) | function | Extract the cookies from the response into a CookieJar. |
| [parse_dict_header](api/00204-requests.auth.parse_dict_header.md) | function | Parse lists of key, value pairs as described by RFC 2068 Section 2 and |
| [to_native_string](api/00205-requests.auth.to_native_string.md) | function | Given a string object, regardless of type, returns a representation of |

## requests.compat

| API | Kind | Purpose from docstring |
| --- | --- | --- |
| [builtin_str](api/00206-requests.compat.builtin_str.md) | class | str(object='') -> str |
| [bytes](api/00254-requests.compat.bytes.md) | class | bytes(iterable_of_ints) -> bytes |
| [str](api/00297-requests.compat.str.md) | class | str(object='') -> str |

## requests.cookies

| API | Kind | Purpose from docstring |
| --- | --- | --- |
| [CookieConflictError](api/00345-requests.cookies.CookieConflictError.md) | class | There are two cookies that meet the criteria specified in the cookie jar. |
| [MockRequest](api/00348-requests.cookies.MockRequest.md) | class | Wraps a `requests.Request` to mimic a `urllib2.Request`. |
| [MockResponse](api/00362-requests.cookies.MockResponse.md) | class | Wraps a `httplib.HTTPMessage` to mimic a `urllib.addinfourl`. |
| [RequestsCookieJar](api/00365-requests.cookies.RequestsCookieJar.md) | class | Compatibility class; is a http.cookiejar.CookieJar, but exposes a dict |
| [cookiejar_from_dict](api/00393-requests.cookies.cookiejar_from_dict.md) | function | Returns a CookieJar from a key/value dictionary. |
| [create_cookie](api/00394-requests.cookies.create_cookie.md) | function | Make a cookie from underspecified parameters. |
| [extract_cookies_to_jar](api/00395-requests.cookies.extract_cookies_to_jar.md) | function | Extract the cookies from the response into a CookieJar. |
| [get_cookie_header](api/00396-requests.cookies.get_cookie_header.md) | function | Produce an appropriate Cookie header string to be sent with `request`, or None. |
| [merge_cookies](api/00397-requests.cookies.merge_cookies.md) | function | Add cookies to cookiejar and returns a merged CookieJar. |
| [morsel_to_cookie](api/00398-requests.cookies.morsel_to_cookie.md) | function | Convert a Morsel object into a Cookie containing the one k/v pair. |
| [remove_cookie_by_name](api/00399-requests.cookies.remove_cookie_by_name.md) | function | Unsets a cookie by name, by default over all domains and paths. |
| [to_native_string](api/00400-requests.cookies.to_native_string.md) | function | Given a string object, regardless of type, returns a representation of |

## requests.exceptions

| API | Kind | Purpose from docstring |
| --- | --- | --- |
| [ChunkedEncodingError](api/00401-requests.exceptions.ChunkedEncodingError.md) | class | The server declared chunked encoding but sent an invalid chunk. |
| [ConnectTimeout](api/00404-requests.exceptions.ConnectTimeout.md) | class | The request timed out while trying to connect to the remote server. |
| [ConnectionError](api/00407-requests.exceptions.ConnectionError.md) | class | A Connection error occurred. |
| [ContentDecodingError](api/00410-requests.exceptions.ContentDecodingError.md) | class | Failed to decode response content. |
| [FileModeWarning](api/00413-requests.exceptions.FileModeWarning.md) | class | A file was opened in text mode, but Requests determined its binary length. |
| [HTTPError](api/00416-requests.exceptions.HTTPError.md) | class | An HTTP error occurred. |
| [InvalidHeader](api/00419-requests.exceptions.InvalidHeader.md) | class | The header value provided was somehow invalid. |
| [InvalidJSONError](api/00422-requests.exceptions.InvalidJSONError.md) | class | A JSON error occurred. |
| [InvalidProxyURL](api/00425-requests.exceptions.InvalidProxyURL.md) | class | The proxy URL provided is invalid. |
| [InvalidSchema](api/00428-requests.exceptions.InvalidSchema.md) | class | The URL scheme provided is either invalid or unsupported. |
| [InvalidURL](api/00431-requests.exceptions.InvalidURL.md) | class | The URL provided was somehow invalid. |
| [JSONDecodeError](api/00434-requests.exceptions.JSONDecodeError.md) | class | Couldn't decode the text into json |
| [MissingSchema](api/00437-requests.exceptions.MissingSchema.md) | class | The URL scheme (e.g. http or https) is missing. |
| [ProxyError](api/00440-requests.exceptions.ProxyError.md) | class | A proxy error occurred. |
| [ReadTimeout](api/00443-requests.exceptions.ReadTimeout.md) | class | The server did not send any data in the allotted amount of time. |
| [RequestException](api/00446-requests.exceptions.RequestException.md) | class | There was an ambiguous exception that occurred while handling your |
| [RequestsDependencyWarning](api/00449-requests.exceptions.RequestsDependencyWarning.md) | class | An imported dependency doesn't match the expected version range. |
| [RequestsWarning](api/00452-requests.exceptions.RequestsWarning.md) | class | Base warning for Requests. |
| [RetryError](api/00455-requests.exceptions.RetryError.md) | class | Custom retries logic failed |
| [SSLError](api/00458-requests.exceptions.SSLError.md) | class | An SSL error occurred. |
| [StreamConsumedError](api/00461-requests.exceptions.StreamConsumedError.md) | class | The content for this response was already consumed. |
| [Timeout](api/00464-requests.exceptions.Timeout.md) | class | The request timed out. |
| [TooManyRedirects](api/00467-requests.exceptions.TooManyRedirects.md) | class | Too many redirects. |
| [URLRequired](api/00470-requests.exceptions.URLRequired.md) | class | A valid URL is required to make a request. |
| [UnrewindableBodyError](api/00473-requests.exceptions.UnrewindableBodyError.md) | class | Requests encountered an error when trying to rewind a body. |

## requests.help

| API | Kind | Purpose from docstring |
| --- | --- | --- |
| [info](api/00476-requests.help.info.md) | function | Generate information for a bug report. |
| [main](api/00477-requests.help.main.md) | function | Pretty-print the bug information as JSON. |

## requests.hooks

| API | Kind | Purpose from docstring |
| --- | --- | --- |
| [default_hooks](api/00478-requests.hooks.default_hooks.md) | function | No description supplied by the package. |
| [dispatch_hook](api/00479-requests.hooks.dispatch_hook.md) | function | Dispatches a hook dictionary on a given piece of data. |

## requests.models

| API | Kind | Purpose from docstring |
| --- | --- | --- |
| [CaseInsensitiveDict](api/00480-requests.models.CaseInsensitiveDict.md) | class | A case-insensitive ``dict``-like object. |
| [ChunkedEncodingError](api/00492-requests.models.ChunkedEncodingError.md) | class | The server declared chunked encoding but sent an invalid chunk. |
| [ConnectionError](api/00495-requests.models.ConnectionError.md) | class | A Connection error occurred. |
| [ContentDecodingError](api/00498-requests.models.ContentDecodingError.md) | class | Failed to decode response content. |
| [HTTPBasicAuth](api/00501-requests.models.HTTPBasicAuth.md) | class | Attaches HTTP Basic Authentication to the given Request object. |
| [HTTPError](api/00502-requests.models.HTTPError.md) | class | An HTTP error occurred. |
| [InvalidJSONError](api/00505-requests.models.InvalidJSONError.md) | class | A JSON error occurred. |
| [InvalidURL](api/00508-requests.models.InvalidURL.md) | class | The URL provided was somehow invalid. |
| [MissingSchema](api/00511-requests.models.MissingSchema.md) | class | The URL scheme (e.g. http or https) is missing. |
| [PreparedRequest](api/00514-requests.models.PreparedRequest.md) | class | The fully mutable :class:`PreparedRequest <PreparedRequest>` object, |
| [Request](api/00528-requests.models.Request.md) | class | A user-created :class:`Request <Request>` object. |
| [RequestEncodingMixin](api/00532-requests.models.RequestEncodingMixin.md) | class | No description supplied by the package. |
| [RequestHooksMixin](api/00534-requests.models.RequestHooksMixin.md) | class | No description supplied by the package. |
| [RequestsJSONDecodeError](api/00537-requests.models.RequestsJSONDecodeError.md) | class | Couldn't decode the text into json |
| [RequestsSSLError](api/00540-requests.models.RequestsSSLError.md) | class | An SSL error occurred. |
| [Response](api/00543-requests.models.Response.md) | class | The :class:`Response <Response>` object, which contains a |
| [StreamConsumedError](api/00557-requests.models.StreamConsumedError.md) | class | The content for this response was already consumed. |
| [check_header_validity](api/00560-requests.models.check_header_validity.md) | function | Verifies that header parts don't contain leading whitespace |
| [cookiejar_from_dict](api/00561-requests.models.cookiejar_from_dict.md) | function | Returns a CookieJar from a key/value dictionary. |
| [default_hooks](api/00562-requests.models.default_hooks.md) | function | No description supplied by the package. |
| [get_auth_from_url](api/00563-requests.models.get_auth_from_url.md) | function | Given a url with authentication components, extract them into a tuple of |
| [get_cookie_header](api/00564-requests.models.get_cookie_header.md) | function | Produce an appropriate Cookie header string to be sent with `request`, or None. |
| [guess_filename](api/00565-requests.models.guess_filename.md) | function | Tries to guess the filename of the given object. |
| [guess_json_utf](api/00566-requests.models.guess_json_utf.md) | function | :rtype: str |
| [iter_slices](api/00567-requests.models.iter_slices.md) | function | Iterate over slices of a string. |
| [parse_header_links](api/00568-requests.models.parse_header_links.md) | function | Return a list of parsed link headers proxies. |
| [requote_uri](api/00569-requests.models.requote_uri.md) | function | Re-quote the given URI. |
| [stream_decode_response_unicode](api/00570-requests.models.stream_decode_response_unicode.md) | function | Stream decodes an iterator. |
| [super_len](api/00571-requests.models.super_len.md) | function | No description supplied by the package. |
| [to_key_val_list](api/00572-requests.models.to_key_val_list.md) | function | Take an object and test to see if it can be represented as a |
| [to_native_string](api/00573-requests.models.to_native_string.md) | function | Given a string object, regardless of type, returns a representation of |
| [unicode_is_ascii](api/00574-requests.models.unicode_is_ascii.md) | function | Determine if unicode string only contains ASCII characters. |

## requests.sessions

| API | Kind | Purpose from docstring |
| --- | --- | --- |
| [CaseInsensitiveDict](api/00575-requests.sessions.CaseInsensitiveDict.md) | class | A case-insensitive ``dict``-like object. |
| [ChunkedEncodingError](api/00587-requests.sessions.ChunkedEncodingError.md) | class | The server declared chunked encoding but sent an invalid chunk. |
| [ContentDecodingError](api/00590-requests.sessions.ContentDecodingError.md) | class | Failed to decode response content. |
| [HTTPAdapter](api/00593-requests.sessions.HTTPAdapter.md) | class | The built-in HTTP Adapter for urllib3. |
| [InvalidSchema](api/00606-requests.sessions.InvalidSchema.md) | class | The URL scheme provided is either invalid or unsupported. |
| [PreparedRequest](api/00609-requests.sessions.PreparedRequest.md) | class | The fully mutable :class:`PreparedRequest <PreparedRequest>` object, |
| [Request](api/00623-requests.sessions.Request.md) | class | A user-created :class:`Request <Request>` object. |
| [RequestsCookieJar](api/00627-requests.sessions.RequestsCookieJar.md) | class | Compatibility class; is a http.cookiejar.CookieJar, but exposes a dict |
| [Session](api/00655-requests.sessions.Session.md) | class | A Requests session. |
| [SessionRedirectMixin](api/00676-requests.sessions.SessionRedirectMixin.md) | class | No description supplied by the package. |
| [TooManyRedirects](api/00683-requests.sessions.TooManyRedirects.md) | class | Too many redirects. |
| [cookiejar_from_dict](api/00686-requests.sessions.cookiejar_from_dict.md) | function | Returns a CookieJar from a key/value dictionary. |
| [default_headers](api/00687-requests.sessions.default_headers.md) | function | :rtype: requests.structures.CaseInsensitiveDict |
| [default_hooks](api/00688-requests.sessions.default_hooks.md) | function | No description supplied by the package. |
| [dispatch_hook](api/00689-requests.sessions.dispatch_hook.md) | function | Dispatches a hook dictionary on a given piece of data. |
| [extract_cookies_to_jar](api/00690-requests.sessions.extract_cookies_to_jar.md) | function | Extract the cookies from the response into a CookieJar. |
| [get_auth_from_url](api/00691-requests.sessions.get_auth_from_url.md) | function | Given a url with authentication components, extract them into a tuple of |
| [get_environ_proxies](api/00692-requests.sessions.get_environ_proxies.md) | function | Return a dict of environment proxies. |
| [get_netrc_auth](api/00693-requests.sessions.get_netrc_auth.md) | function | Returns the Requests tuple auth for a given url from netrc. |
| [merge_cookies](api/00694-requests.sessions.merge_cookies.md) | function | Add cookies to cookiejar and returns a merged CookieJar. |
| [merge_hooks](api/00695-requests.sessions.merge_hooks.md) | function | Properly merges both requests and session hooks. |
| [merge_setting](api/00696-requests.sessions.merge_setting.md) | function | Determines appropriate setting for a given request, taking into account |
| [preferred_clock](api/00697-requests.sessions.preferred_clock.md) | function | perf_counter() -> float |
| [requote_uri](api/00698-requests.sessions.requote_uri.md) | function | Re-quote the given URI. |
| [resolve_proxies](api/00699-requests.sessions.resolve_proxies.md) | function | This method takes proxy information from a request and configuration |
| [rewind_body](api/00700-requests.sessions.rewind_body.md) | function | Move file pointer back to its recorded starting position |
| [session](api/00701-requests.sessions.session.md) | function | Returns a :class:`Session` for context-management. |
| [should_bypass_proxies](api/00702-requests.sessions.should_bypass_proxies.md) | function | Returns whether we should bypass proxies or not. |
| [to_key_val_list](api/00703-requests.sessions.to_key_val_list.md) | function | Take an object and test to see if it can be represented as a |
| [to_native_string](api/00704-requests.sessions.to_native_string.md) | function | Given a string object, regardless of type, returns a representation of |

## requests.status_codes

| API | Kind | Purpose from docstring |
| --- | --- | --- |
| [LookupDict](api/00705-requests.status_codes.LookupDict.md) | class | Dictionary lookup object. |

## requests.structures

| API | Kind | Purpose from docstring |
| --- | --- | --- |
| [CaseInsensitiveDict](api/00717-requests.structures.CaseInsensitiveDict.md) | class | A case-insensitive ``dict``-like object. |
| [LookupDict](api/00729-requests.structures.LookupDict.md) | class | Dictionary lookup object. |

## requests.utils

| API | Kind | Purpose from docstring |
| --- | --- | --- |
| [CaseInsensitiveDict](api/00741-requests.utils.CaseInsensitiveDict.md) | class | A case-insensitive ``dict``-like object. |
| [FileModeWarning](api/00753-requests.utils.FileModeWarning.md) | class | A file was opened in text mode, but Requests determined its binary length. |
| [InvalidHeader](api/00756-requests.utils.InvalidHeader.md) | class | The header value provided was somehow invalid. |
| [InvalidURL](api/00759-requests.utils.InvalidURL.md) | class | The URL provided was somehow invalid. |
| [UnrewindableBodyError](api/00762-requests.utils.UnrewindableBodyError.md) | class | Requests encountered an error when trying to rewind a body. |
| [add_dict_to_cookiejar](api/00765-requests.utils.add_dict_to_cookiejar.md) | function | Returns a CookieJar from a key/value dictionary. |
| [address_in_network](api/00766-requests.utils.address_in_network.md) | function | This function allows you to check if an IP belongs to a network subnet |
| [atomic_open](api/00767-requests.utils.atomic_open.md) | function | Write a file to the disk in an atomic fashion |
| [check_header_validity](api/00768-requests.utils.check_header_validity.md) | function | Verifies that header parts don't contain leading whitespace |
| [cookiejar_from_dict](api/00769-requests.utils.cookiejar_from_dict.md) | function | Returns a CookieJar from a key/value dictionary. |
| [default_headers](api/00770-requests.utils.default_headers.md) | function | :rtype: requests.structures.CaseInsensitiveDict |
| [default_user_agent](api/00771-requests.utils.default_user_agent.md) | function | Return a string representing the default user agent. |
| [dict_from_cookiejar](api/00772-requests.utils.dict_from_cookiejar.md) | function | Returns a key/value dictionary from a CookieJar. |
| [dict_to_sequence](api/00773-requests.utils.dict_to_sequence.md) | function | Returns an internal sequence dictionary update. |
| [dotted_netmask](api/00774-requests.utils.dotted_netmask.md) | function | Converts mask from /xx format to xxx.xxx.xxx.xxx |
| [extract_zipped_paths](api/00775-requests.utils.extract_zipped_paths.md) | function | Replace nonexistent paths that look like they refer to a member of a zip |
| [from_key_val_list](api/00776-requests.utils.from_key_val_list.md) | function | Take an object and test to see if it can be represented as a |
| [get_auth_from_url](api/00777-requests.utils.get_auth_from_url.md) | function | Given a url with authentication components, extract them into a tuple of |
| [get_encoding_from_headers](api/00778-requests.utils.get_encoding_from_headers.md) | function | Returns encodings from given HTTP Header Dict. |
| [get_encodings_from_content](api/00779-requests.utils.get_encodings_from_content.md) | function | Returns encodings from given content string. |
| [get_environ_proxies](api/00780-requests.utils.get_environ_proxies.md) | function | Return a dict of environment proxies. |
| [get_netrc_auth](api/00781-requests.utils.get_netrc_auth.md) | function | Returns the Requests tuple auth for a given url from netrc. |
| [get_unicode_from_response](api/00782-requests.utils.get_unicode_from_response.md) | function | Returns the requested content back in unicode. |
| [guess_filename](api/00783-requests.utils.guess_filename.md) | function | Tries to guess the filename of the given object. |
| [guess_json_utf](api/00784-requests.utils.guess_json_utf.md) | function | :rtype: str |
| [is_ipv4_address](api/00785-requests.utils.is_ipv4_address.md) | function | :rtype: bool |
| [is_valid_cidr](api/00786-requests.utils.is_valid_cidr.md) | function | Very simple check of the cidr format in no_proxy variable. |
| [iter_slices](api/00787-requests.utils.iter_slices.md) | function | Iterate over slices of a string. |
| [parse_dict_header](api/00788-requests.utils.parse_dict_header.md) | function | Parse lists of key, value pairs as described by RFC 2068 Section 2 and |
| [parse_header_links](api/00789-requests.utils.parse_header_links.md) | function | Return a list of parsed link headers proxies. |
| [parse_list_header](api/00790-requests.utils.parse_list_header.md) | function | Parse lists as described by RFC 2068 Section 2. |
| [prepend_scheme_if_needed](api/00791-requests.utils.prepend_scheme_if_needed.md) | function | Given a URL that may or may not have a scheme, prepend the given scheme. |
| [proxy_bypass](api/00792-requests.utils.proxy_bypass.md) | function | Return True, if the host should be bypassed. |
| [proxy_bypass_registry](api/00793-requests.utils.proxy_bypass_registry.md) | function | No description supplied by the package. |
| [requote_uri](api/00794-requests.utils.requote_uri.md) | function | Re-quote the given URI. |
| [resolve_proxies](api/00795-requests.utils.resolve_proxies.md) | function | This method takes proxy information from a request and configuration |
| [rewind_body](api/00796-requests.utils.rewind_body.md) | function | Move file pointer back to its recorded starting position |
| [select_proxy](api/00797-requests.utils.select_proxy.md) | function | Select a proxy for the url, if applicable. |
| [set_environ](api/00798-requests.utils.set_environ.md) | function | Set the environment variable 'env_name' to 'value' |
| [should_bypass_proxies](api/00799-requests.utils.should_bypass_proxies.md) | function | Returns whether we should bypass proxies or not. |
| [stream_decode_response_unicode](api/00800-requests.utils.stream_decode_response_unicode.md) | function | Stream decodes an iterator. |
| [super_len](api/00801-requests.utils.super_len.md) | function | No description supplied by the package. |
| [to_key_val_list](api/00802-requests.utils.to_key_val_list.md) | function | Take an object and test to see if it can be represented as a |
| [to_native_string](api/00803-requests.utils.to_native_string.md) | function | Given a string object, regardless of type, returns a representation of |
| [unquote_header_value](api/00804-requests.utils.unquote_header_value.md) | function | Unquotes a header value.  (Reversal of :func:`quote_header_value`). |
| [unquote_unreserved](api/00805-requests.utils.unquote_unreserved.md) | function | Un-escape any percent-escape sequences in a URI that are unreserved |
| [urldefragauth](api/00806-requests.utils.urldefragauth.md) | function | Given a url remove the fragment and the authentication part. |
