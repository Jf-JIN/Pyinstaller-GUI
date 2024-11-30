"""
常量枚举类

该枚举类支持唯一的枚举项, 且枚举项的值不能被修改. 
枚举项访问方法为: 枚举类名.枚举项名
无需实例化, 也无需使用 枚举类名.枚举项名.value 获取枚举项的值

"""


class _AnalogDefineDict(dict):
    """
    用于存储枚举项的字典类, 检查重复定义项
    """

    def __init__(self):
        super().__init__()
        self.cls_name = None
        self._member_names = {}

    def __setitem__(self, key, value):
        if key in self._member_names:
            raise ValueError(f'枚举项重复: 已存在\t< {key} > = {self._member_names[key]}')
        self._member_names[key] = value
        super().__setitem__(key, value)


class AnalogDefineMeta(type):
    """
    枚举类的元类
    """
    @classmethod
    def __prepare__(metacls, cls, bases, **kwds):
        """
        用于创建枚举项的字典类, 以便之后查找相同的枚举项
        """
        enum_dict = _AnalogDefineDict()
        enum_dict._cls_name = cls
        return enum_dict

    def __new__(mcs, name, bases, dct: dict):
        if len(bases) == 0:
            return super().__new__(mcs, name, bases, dct)
        dct['_members_'] = {}  # 用于存储枚举项的字典
        dct['isAllowedSetValue'] = False  # 用于允许赋值枚举项的标志, 允许内部赋值, 禁止外部赋值
        members = {key: value for key, value in dct.items() if not key.startswith('__')}
        cls = super().__new__(mcs, name, bases, dct)
        for key, value in members.items():
            if key == 'isAllowedSetValue' or key == '_members_':
                continue
            cls._members_['isAllowedSetValue'] = True
            cls._members_[key] = value
            setattr(cls, key, value)
            cls._members_['isAllowedSetValue'] = False
        return cls

    def __setattr__(cls, key, value):
        if key in cls._members_ and not cls._members_['isAllowedSetValue']:
            raise AttributeError(f'禁止外部修改枚举项\t< {key} > = {cls._members_[key]}')
        super().__setattr__(key, value)


class AnalogDefine(metaclass=AnalogDefineMeta):
    @classmethod
    def members(cls):
        temp = []
        for key, value in cls._members_.items():
            if key == 'isAllowedSetValue' or key == '_members_':
                continue
            temp.append((key, value))
        return temp


if __name__ == '__main__':
    class SubColor(AnalogDefine):
        BLACK = 5

    class Color(AnalogDefine):
        RED = 1
        GREEN = 2
        BLUE = 3
        YELLOW = SubColor()
        RED = 4

    print(Color.RED)
    print(Color.members())
    print(Color.YELLOW.BLACK)
    Color.RED = 2
    print(Color.RED)
