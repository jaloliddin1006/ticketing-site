from django.db import models
import random


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class VerifyEmailCode:
    def __init__(self):
        self.SIGN = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        self.K = 12

    def new_code(self):

        self.code_list = random.sample(self.SIGN, k=self.K)
        self.code = ''.join(self.code_list)  # list to string
        return self.code