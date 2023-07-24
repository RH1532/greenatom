# Проблема в строке handlers.append(lambda: callback(step)) она всегда будет вызыватся со значением 4
# Для испрвления её нужно заменить на handlers.append(lambda step=step: callback(step))

from typing import List, Callable

def create_handlers(callback: Callable[[int], None]) -> List[Callable[[], None]]:
    handlers = []
    for step in range(5):
        # добавляем обработчики для каждого шага (от 0 до 4)
        handlers.append(lambda step=step: callback(step))
    return handlers

def execute_handlers(handlers: List[Callable[[], None]]) -> None:
    # запускаем добавленные обработчики (шаги от 0 до 4)
    for handler in handlers:
        handler()
