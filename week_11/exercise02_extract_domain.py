from urllib.parse import urlparse

while True:
    url = input("Enter a URL: ").strip()
    if url:
        break
    print("Please enter a non-empty URL.")

# urlparse needs a scheme to recognize the hostname correctly.
if "://" not in url:
    url = f"https://{url}"

parsed_url = urlparse(url)
domain = parsed_url.hostname

if domain:
	print(f"Domain: {domain}")
else:
	print("The URL does not contain a valid domain.")
	print("")
