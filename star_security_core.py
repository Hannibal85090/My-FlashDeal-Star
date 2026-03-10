import re
import hashlib

class FlashDealStarSecurity:
    def __init__(self):
        self.hoax_keywords = ["virus", "format", "urgent", "broadcast", "macron", "con"]
        self.version = "2.0.0"

    def validate_content(self, message):
        score = 0
        content_lower = message.lower()
        for word in self.hoax_keywords:
            if word in content_lower: score += 1
        url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        if re.search(url_pattern, content_lower): score += 2
        if score >= 3: return False, "BLOCK: Malicious content detected."
        return True, "SAFE"

    def generate_secure_token(self, data):
        raw_token = f"{data}{self.version}"
        return hashlib.sha256(raw_token.encode()).hexdigest()
