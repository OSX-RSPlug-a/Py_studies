import os
import sys
import json
import base64
import getpass
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
#pip install cryptography


class PasswordSafe:
    def __init__(self, vault_path="password_vault.json", master_password=""):
        self.vault_path = vault_path
        self.vault = {}
        self.salt = None
        self.fernet = None


        if os.path.exists(self.vault_path):
            self._load_vault(master_password)
        else:
            self._create_vault(master_password)

        del master_password

    def _derive_key(self, password: bytes) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=600_000,
        )
        return base64.urlsafe_b64encode(kdf.derive(password))

    def _create_vault(self, master_password: str):
        self.salt = os.urandom(16)
        key = self._derive_key(master_password.encode())
        self.fernet = Fernet(key)
        self._save_vault()

    def _load_vault(self, master_password: str):
        try:
            with open(self.vault_path, 'r') as f:
                data = json.load(f)
        except json.JSONDecodeError:
            print("\n[ERROR] Vault file is corrupted.")
            sys.exit(1)

        self.salt = base64.b64decode(data['salt'])
        key = self._derive_key(master_password.encode())
        self.fernet = Fernet(key)

        try:
            decrypted = self.fernet.decrypt(data['encrypted_data'].encode())
            self.vault = json.loads(decrypted.decode())
        except InvalidToken:
            print("\n[ERROR] Decryption failed. Wrong master password or corrupted vault.")
            sys.exit(1)

    def _save_vault(self):
        vault_json = json.dumps(self.vault, indent=2).encode()
        encrypted_data = self.fernet.encrypt(vault_json)

        save_data = {
            'version': 1,
            'salt': base64.b64encode(self.salt).decode(),
            'encrypted_data': encrypted_data.decode()
        }
        with open(self.vault_path, 'w') as f:
            json.dump(save_data, f, indent=2)

    def add(self, service: str, password: str):
        self.vault[service] = password
        self._save_vault()
        print(f"[+] Password for '{service}' saved.")

    def get(self, service: str) -> str | None:
        return self.vault.get(service)

    def delete(self, service: str) -> bool:
        if service in self.vault:
            del self.vault[service]
            self._save_vault()
            print(f"[-] Password for '{service}' deleted.")
            return True
        print(f"[!] '{service}' not found.")
        return False

    def list_services(self) -> list:
        return list(self.vault.keys())


def main():
    print("=== Simple Password Safe ===")
    vault_file = input("Vault file path (default: password_vault.json): ").strip() or "password_vault.json"
    
    if os.path.exists(vault_file):
        master_pw = getpass.getpass("Enter master password: ")
    else:
        master_pw = getpass.getpass("Create master password: ")
        confirm = getpass.getpass("Confirm master password: ")
        if master_pw != confirm:
            print("\n[ERROR] Passwords do not match.")
            sys.exit(1)
        if len(master_pw) < 8:
            print("\n[WARNING] Master password is short. Consider using a longer, stronger passphrase.")

    try:
        safe = PasswordSafe(vault_file, master_pw)
    except Exception as e:
        print(f"\n[ERROR] Failed to initialize vault: {e}")
        sys.exit(1)

    while True:
        print("\n--- Menu ---")
        print("1. Add password")
        print("2. Get password")
        print("3. Delete password")
        print("4. List services")
        print("5. Exit")
        
        choice = input("Choose: ").strip()

        if choice == '1':
            svc = input("Service name: ").strip()
            pw = getpass.getpass("Password: ").strip()
            safe.add(svc, pw)
        elif choice == '2':
            svc = input("Service name: ").strip()
            pw = safe.get(svc)
            if pw:
                print(f"🔑 Password: {pw}")
            else:
                print("❌ Service not found.")
        elif choice == '3':
            svc = input("Service name to delete: ").strip()
            safe.delete(svc)
        elif choice == '4':
            svcs = safe.list_services()
            print("📂 Services:", ", ".join(svcs) if svcs else "None")
        elif choice == '5':
            print("🔒 Exiting securely...")
            break
        else:
            print("⚠️ Invalid choice.")



if __name__ == "__main__":
    main()