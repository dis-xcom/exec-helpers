import typing
from exec_helpers import proc_enums, exec_result

class ExecHelperError(Exception):
    ...

class DeserializeValueError(ExecHelperError, ValueError):
    ...


class ExecCalledProcessError(ExecHelperError):
    ...


class ExecHelperTimeoutError(ExecCalledProcessError):

    result: exec_result.ExecResult = ...
    timeout: int = ...

    def __init__(
        self,
        result: exec_result.ExecResult,
        timeout: typing.Union[int, float],
    ) -> None: ...

    @property
    def cmd(self) -> str: ...

    @property
    def stdout(self) -> typing.Text: ...

    @property
    def stderr(self) -> typing.Text: ...


class CalledProcessError(ExecCalledProcessError):

    result: exec_result.ExecResult = ...

    expected: typing.List[typing.Union[int, proc_enums.ExitCodes]] = ...

    def __init__(
        self,
        result: exec_result.ExecResult,
        expected: typing.Optional[typing.List[typing.Union[int, proc_enums.ExitCodes]]]=...
    ) -> None: ...

    @property
    def returncode(self) -> typing.Union[int, proc_enums.ExitCodes]: ...

    @property
    def cmd(self) -> str: ...

    @property
    def stdout(self) -> typing.Text: ...

    @property
    def stderr(self) -> typing.Text: ...


class ParallelCallExceptions(ExecCalledProcessError):

    expected: typing.List[typing.Union[int, proc_enums.ExitCodes]] = ...
    cmd: str = ...
    exceptions: typing.Dict[typing.Tuple[str, int], Exception] = ...
    errors: typing.Dict[typing.Tuple[str, int], exec_result.ExecResult] = ...
    results: typing.Dict[typing.Tuple[str, int], exec_result.ExecResult] = ...

    def __init__(
        self,
        command: str,
        exceptions: typing.Dict[typing.Tuple[str, int], Exception],
        errors: typing.Dict[typing.Tuple[str, int], exec_result.ExecResult],
        results: typing.Dict[typing.Tuple[str, int], exec_result.ExecResult],
        expected: typing.Optional[typing.List[typing.Union[int, proc_enums.ExitCodes]]]=...
    ) -> None: ...

class ParallelCallProcessError(ExecCalledProcessError):

    expected: typing.List[typing.Union[int, proc_enums.ExitCodes]] = ...
    cmd: str = ...
    errors: typing.Dict[typing.Tuple[str, int], exec_result.ExecResult] = ...
    results: typing.Dict[typing.Tuple[str, int], exec_result.ExecResult] = ...

    def __init__(
        self,
        command: str,
        errors: typing.Dict[typing.Tuple[str, int], exec_result.ExecResult],
        results: typing.Dict[typing.Tuple[str, int], exec_result.ExecResult],
        expected: typing.Optional[typing.List[typing.Union[int, proc_enums.ExitCodes]]]=...
    ) -> None: ...
