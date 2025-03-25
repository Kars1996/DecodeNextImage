from urllib.parse import urlparse, parse_qs, unquote
import pyperclip

def decode_url(url: str) -> str:    
    parsed = urlparse(url)
    query_params = parse_qs(parsed.query)
    
    if '_next/image' in parsed.path:
        if 'url' in query_params:
            original_url = unquote(query_params['url'][0])
            
            if original_url.startswith('/'):
                return f"{parsed.scheme}://{parsed.netloc}{original_url}"
            return original_url
            
    return url

if __name__ == '__main__':
    retry = True
    while retry:
        url = input("Enter the url to decode: ")
        decoded = decode_url(url)
        print(f"Decoded: {decoded}")
        pyperclip.copy(decoded)
        print("(Copied to clipboard!)")
        retry = input("Do you want to retry? (y/n): ").lower() == 'y'