class AuthenticationService:
    def login(self, phone_number: str, password: str) -> bool:
        # Simplified placeholder for authentication.
        # In a real banking system this must use hashing, MFA, and secure sessions.
        return bool(phone_number and password)

    def authorize_customer(self, authenticated_customer_id: int, requested_customer_id: int) -> bool:
        return authenticated_customer_id == requested_customer_id
