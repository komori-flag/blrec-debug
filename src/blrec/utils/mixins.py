import os
from abc import ABC, abstractmethod
import asyncio
import threading
from typing import Awaitable, TypeVar, final


class SwitchableMixin(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._enabled = False
        self._enabled_lock = threading.Lock()

    @property
    def enabled(self) -> bool:
        with self._enabled_lock:
            return self._enabled

    @final
    def enable(self) -> None:
        with self._enabled_lock:
            if self._enabled:
                return
            self._enabled = True
            self._do_enable()

    @final
    def disable(self) -> None:
        with self._enabled_lock:
            if not self._enabled:
                return
            self._enabled = False
            self._do_disable()

    @abstractmethod
    def _do_enable(self) -> None:
        ...

    @abstractmethod
    def _do_disable(self) -> None:
        ...


class StoppableMixin(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._stopped = True
        self._stopped_lock = threading.Lock()

    @property
    def stopped(self) -> bool:
        with self._stopped_lock:
            return self._stopped

    @final
    def start(self) -> None:
        with self._stopped_lock:
            if not self._stopped:
                return
            self._stopped = False
            self._do_start()

    @final
    def stop(self) -> None:
        with self._stopped_lock:
            if self._stopped:
                return
            self._stopped = True
            self._do_stop()

    @abstractmethod
    def _do_start(self) -> None:
        ...

    @abstractmethod
    def _do_stop(self) -> None:
        ...


class AsyncStoppableMixin(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._stopped = True

    @property
    def stopped(self) -> bool:
        return self._stopped

    @final
    async def start(self) -> None:
        if not self._stopped:
            return
        self._stopped = False
        await self._do_start()

    @final
    async def stop(self) -> None:
        if self._stopped:
            return
        self._stopped = True
        await self._do_stop()

    @abstractmethod
    async def _do_start(self) -> None:
        ...

    @abstractmethod
    async def _do_stop(self) -> None:
        ...


_T = TypeVar('_T')


class AsyncCooperationMixin(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._loop = asyncio.get_running_loop()

    def _handle_exception(self, exc: BaseException) -> None:
        from ..exception import submit_exception

        async def wrapper() -> None:
            # call submit_exception in a coroutine
            # workaround for `RuntimeError: no running event loop`
            submit_exception(exc)
        self._run_coroutine(wrapper())

    def _run_coroutine(self, coro: Awaitable[_T]) -> _T:
        future = asyncio.run_coroutine_threadsafe(coro, self._loop)
        return future.result()


class SupportDebugMixin(ABC):
    def __init__(self) -> None:
        super().__init__()

    def _init_for_debug(self, room_id: int) -> None:
        if (
            (value := os.environ.get('DEBUG')) and
            (value == '*' or room_id in value.split(','))
        ):
            self._debug = True
            self._debug_dir = os.path.expanduser(f'~/.blrec/debug/{room_id}')
            self._debug_dir = os.path.normpath(self._debug_dir)
            os.makedirs(self._debug_dir, exist_ok=True)
        else:
            self._debug = False
            self._debug_dir = ''
