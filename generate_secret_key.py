#!/usr/bin/env python3
"""
Generate a secure Django SECRET_KEY
"""

import secrets
import string

def generate_secret_key(length=50):
    """Generate a secure random secret key"""
    # Use a mix of letters, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    # Remove characters that might cause issues in environment variables
    characters = characters.replace('"', '').replace("'", '').replace('\\', '')
    
    # Generate the secret key
    secret_key = ''.join(secrets.choice(characters) for _ in range(length))
    return secret_key

if __name__ == "__main__":
    print("🔐 Generating secure Django SECRET_KEY...")
    print("=" * 50)
    
    # Generate a secure key
    secret_key = generate_secret_key()
    
    print("✅ Your secure SECRET_KEY:")
    print(f"SECRET_KEY={secret_key}")
    print()
    print("📝 Copy this key and use it in:")
    print("1. Railway/Render environment variables")
    print("2. Your .env file")
    print("3. Production settings")
    print()
    print("⚠️  Keep this key secret and don't share it!")
    print("⚠️  Use different keys for development and production")
