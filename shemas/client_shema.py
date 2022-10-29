from pydantic import BaseModel, validator
from pydantic import conint, constr
import re


class SearchClient(BaseModel):
    name: constr(max_length=32)
    phone_number: constr(max_length=32)


class AddClient(SearchClient):
    address: constr(max_length=256)

    @validator('phone_number')
    def rus_phone_validator(cls, v):
        mob_num = re.compile(r"(\+7|8)9\d{9}", flags=0)
        city_num = re.compile(r"(\+7|8)(3|4|8)\d{2,4}\d{6}", flags=0)
        match_tuple = (mob_num.fullmatch(v), city_num.fullmatch(v))
        if any(match_tuple):
            need_match = (match for match in match_tuple if match)[0]
            if need_match.string == v:
                v = v.replace('8', '+7', 1)
                return v
            else:
                raise ValueError('Wrong format of phone number.')
        else:
            raise ValueError('Wrong format of phone number.')
