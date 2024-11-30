
class StructEnvInfo(object):
    def __init__(self, name):
        self.__name = name
        self.env_name: str = ''
        self.path_python: str = ''
        self.path_pyinstaller: str = None
        self.version: str = ''
        self.path_error: bool = False  # 给 指定解释器路径 用的, 记录路径是否错误
        self.command_launch: str = ''  # 给 当前环境 用的, 记录启动路径

    @property
    def name(self) -> str:
        """获取环境名称"""
        return self.__name

    def __str__(self):
        return f"环境名称: {self.env_name}\n环境路径: {self.env_path}\n环境版本: {self.env_version}\n环境类型: {self.env_type}"
