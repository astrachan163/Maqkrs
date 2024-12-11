import re
import requests  # Added for optional link validation (commented out by default)

def find_and_replace_links(text, replacements):
    """Finds potential links in text and replaces them based on a dictionary.

    Args:
        text: The input text string.
        replacements: A dictionary mapping original URLs to replacement URLs.

    Returns:
        The text with URLs replaced according to the replacements dictionary.
    """

    # Regular expression to find URLs (this is a simplified version; more robust regexes exist)
    url_pattern = r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"
    urls = re.findall(url_pattern, text)

    #Optional: Check if links are functional (requires requests library)
    #functional_links = []
    #for url in urls:
    #    try:
    #        response = requests.head(url)  #Use HEAD request for efficiency
    #        if response.status_code == 200:
    #            functional_links.append(url)
    #    except requests.exceptions.RequestException as e:
    #        print(f"Error checking URL {url}: {e}")


    # Create a single regex pattern for replacement
    pattern_parts = [r"(" + re.escape(url) + r")" for url in replacements]
    pattern = re.compile("|".join(pattern_parts), re.IGNORECASE)

    def replace_func(match):
        original_url = match.group(1)
        replacement_url = replacements.get(original_url)
        return replacement_url if replacement_url else original_url

    modified_text = pattern.sub(replace_func, text)
    return modified_text


# Example usage:
text = "Visit our website at https://www.example.com/page1 and also see https://www.example.com/page2?param=value.  Another link: http://anothersite.com"
replacements = {
    "https://www.example.com/page1": "https://newsite.com/pageA",
    "https://www.example.com/page2": "https://newsite.com/pageB"
}

modified_text = find_and_replace_links(text, replacements)
print(f"Original text:\n{text}\n")
print(f"Modified text:\n{modified_text}")

if __name__ == "__main__":
    text = "Visit our website at https://www.example.com/page1 and also see https://www.example.com/page2?param=value.  Another link: http://anothersite.com"
    replacements = {
        "https://www.example.com/page1": "https://newsite.com/pageA",
        "https://www.example.com/page2": "https://newsite.com/pageB"
    }

    modified_text = find_and_replace_links(text, replacements)
    print(f"Original text:\n{text}\n")
    print(f"Modified text:\n{modified_text}")


