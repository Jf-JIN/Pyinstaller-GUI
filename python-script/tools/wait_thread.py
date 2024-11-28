from PyQt5.QtCore import QEventLoop, pyqtSignal


def wait_for_thread_result(outputsignal: pyqtSignal, default_value=None) -> bool:
    """
    等待线程完成并返回结果
    """
    def on_thread_finished(result: bool):
        
        result_container['value'] = result
        loop.quit()

    loop = QEventLoop()
    result_container = {}  # 使用字典是因为这个是引用，否则可能就要用nonlocal
    outputsignal.connect(on_thread_finished)
    loop.exec_()
    return result_container.get('value', default_value)
