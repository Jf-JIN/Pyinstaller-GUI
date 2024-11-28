import wrapt
import traceback


def try_except_log(logger_error: callable = None, textbrowser: str = 'tb_console'):
    @wrapt.decorator
    def try_decorator(wrapped, instance, args, kwargs):
        try:
            return wrapped(*args, **kwargs)
        except Exception as e:
            e = traceback.format_exc()
            if instance and hasattr(instance, textbrowser):
                getattr(instance, textbrowser).append_text(e)
            print(e)
            if logger_error:
                logger_error(e, extra={'moduleName': wrapped.__module__, 'functionName': wrapped.__qualname__})
            return None
    return try_decorator
