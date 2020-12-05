from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class UserTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        user_id = six.text_type(user.pk)
        ts = six.text_type(timestamp)
        active = six.text_type(user.active)
        return f"{user_id}{ts}{active}"

user_tokenizer = UserTokenGenerator()
