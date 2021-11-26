# Markdown Link Checker

A command-line utility written in Python that checks validity of links in a markdown file.

## Install

```
pip install markdown-link-checker
```

## Usage

```
link_checker "markdown-file.md"
```

## Output

Invalid links in document

| link             | reason                                                                                                                                                                                                                                                                    |
| :--------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| http://example.c | HTTPConnectionPool(host='example.c', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection. HTTPConnection object at 0x1066924d0>: Failed to establish a new connection: [Errno ] nodename nor servname provided, or not known')) |
| htp://google.com | No connection adapters were found for 'htp://google.com'                                                                                                                                                                                                                  |
| http//google.com | Invalid URL 'http//google.com': No schema supplied. Perhaps you meant http://http//google.com?                                                                                                                                                                            |

Valid links in document

| text  | link               |
| ----- | ------------------ |
| here  | http://example.com |
| Udemy | https://udemy.com  |

