from oauthenticator.generic import GenericOAuthenticator

class MIAAuth(GenericOAuthenticator):
    
    def normalize_username(self, username):
        self.log.debug(f"[MIAAuth] In normalize username. Username = {username}"
        if isinstance(username, list):
            username = username[0]
        return super().normalize_username(username)