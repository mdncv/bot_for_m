from tortoise.models import Model
from tortoise import fields


class UserTable(Model):
    id = fields.BigIntField(pk=True)
    user_id = fields.BigIntField(unique=True)
    poll_id = fields.BigIntField()
    correct_option_id = fields.IntField()
    word = fields.CharField(max_length=50)
    correct_answers = fields.BigIntField()
    incorrect_answers = fields.BigIntField()
    learning_lang = fields.IntField()
    native_lang = fields.IntField()

    def __str__(self):
        return 'User with id ' + self.user_id

    def __dict__(self):
        return dict(user_id=self.user_id, poll_id=self.poll_id, correct_option_id=self.correct_option_id,
                    word=self.word, correct_answers=self.correct_answers, incorrect_answers=self.incorrect_answers,
                    learning_lang=self.learning_lang, native_lang=self.native_lang)


class DictTable(Model):
    id = fields.BigIntField(pk=True)
    user_id = fields.BigIntField()
    word = fields.CharField(max_length=50)
    description = fields.CharField(max_length=50)

    def __str__(self):
        return self.word + ': ' + self.description


class Cheers(Model):
    id = fields.IntField(pk=True)
    cheer = fields.CharField(unique=True, max_length=50)
    not_cheer = fields.CharField(unique=True, max_length=50)
